from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages

from .models import SkillAnalysis, REQUIRED_SKILLS, JOB_ROLES, EXPERIENCE_LEVELS, LEARNING_RESOURCES


def home(request):
    total_analyses = SkillAnalysis.objects.count()
    context = {
        'total_analyses': total_analyses,
        'job_roles': JOB_ROLES,
    }
    return render(request, 'analyzer/home.html', context)


def analyze(request):
    context = {
        'job_roles': JOB_ROLES,
        'experience_levels': EXPERIENCE_LEVELS,
    }
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        job_role = request.POST.get('job_role', '')
        experience_level = request.POST.get('experience_level', '')
        skills_input = request.POST.get('skills', '')

        if not name or not job_role or not experience_level or not skills_input:
            messages.error(request, 'Please fill in all required fields.')
            context.update(request.POST)
            return render(request, 'analyzer/analyze.html', context)

        current_skills = [s.strip().lower() for s in skills_input.split(',') if s.strip()]
        role_data = REQUIRED_SKILLS.get(job_role, {})
        all_required = []
        for cat in ['core', 'tools', 'soft']:
            all_required.extend(role_data.get(cat, []))

        matched = [r for r in all_required if any(r.lower() in s or s in r.lower() for s in current_skills)]
        gap_skills_raw = [r for r in all_required if r not in matched]
        score = round((len(matched) / len(all_required)) * 100, 1) if all_required else 0

        analysis = SkillAnalysis.objects.create(
            name=name,
            email=email,
            job_role=job_role,
            experience_level=experience_level,
            current_skills=', '.join([s.strip() for s in skills_input.split(',') if s.strip()]),
            skill_score=score,
            gap_skills=', '.join(gap_skills_raw),
        )
        return redirect('result', pk=analysis.pk)

    return render(request, 'analyzer/analyze.html', context)


def result(request, pk):
    analysis = get_object_or_404(SkillAnalysis, pk=pk)
    role_data = REQUIRED_SKILLS.get(analysis.job_role, {})
    current_skills_lower = [s.lower() for s in analysis.get_current_skills_list()]

    def is_matched(skill):
        return any(skill.lower() in s or s in skill.lower() for s in current_skills_lower)

    core_skills = [(s, is_matched(s)) for s in role_data.get('core', [])]
    tool_skills = [(s, is_matched(s)) for s in role_data.get('tools', [])]
    soft_skills = [(s, is_matched(s)) for s in role_data.get('soft', [])]

    gap_list = analysis.get_gap_skills_list()
    resources = []
    for skill in gap_list[:8]:
        matched_resource = None
        for key, val in LEARNING_RESOURCES.items():
            if key.lower() in skill.lower() or skill.lower() in key.lower():
                matched_resource = {'skill': skill, **val}
                break
        if not matched_resource:
            matched_resource = {
                'skill': skill,
                'platform': 'YouTube / Udemy',
                'url': f'https://www.youtube.com/results?search_query={skill.replace(" ", "+")}+tutorial+for+beginners',
                'duration': '2-4 weeks'
            }
        resources.append(matched_resource)

    score = analysis.skill_score
    if score >= 80:
        badge = ('Placement Ready', 'success', '🎯')
        badge_msg = "You're well-prepared for this role. Start applying!"
    elif score >= 60:
        badge = ('Almost There', 'warning', '📈')
        badge_msg = "A few more skills and you're good to go!"
    elif score >= 40:
        badge = ('Skill Building', 'info', '🔨')
        badge_msg = "Keep learning — you're on the right path!"
    else:
        badge = ('Just Starting', 'danger', '🚀')
        badge_msg = "Great time to start your learning journey!"

    # Score circle stroke-dashoffset: circumference = 2 * pi * 54 ≈ 339.3
    circumference = 339.3
    offset = round(circumference - (score / 100) * circumference, 2)

    context = {
        'analysis': analysis,
        'core_skills': core_skills,
        'tool_skills': tool_skills,
        'soft_skills': soft_skills,
        'resources': resources,
        'badge': badge,
        'badge_msg': badge_msg,
        'job_role_display': dict(JOB_ROLES).get(analysis.job_role, analysis.job_role),
        'exp_display': dict(EXPERIENCE_LEVELS).get(analysis.experience_level, analysis.experience_level),
        'score_int': int(score),
        'score_offset': offset,
        'circumference': circumference,
        'matched_count': len([s for s in core_skills + tool_skills + soft_skills if s[1]]),
        'gap_count': len([s for s in core_skills + tool_skills + soft_skills if not s[1]]),
    }
    return render(request, 'analyzer/result.html', context)


def get_skills_for_role(request):
    role = request.GET.get('role', '')
    role_data = REQUIRED_SKILLS.get(role, {})
    all_skills = []
    for cat in ['core', 'tools', 'soft']:
        all_skills.extend(role_data.get(cat, []))
    return JsonResponse({'skills': all_skills})


def leaderboard(request):
    analyses = SkillAnalysis.objects.order_by('-skill_score')[:20]
    job_roles_dict = dict(JOB_ROLES)
    context = {
        'analyses': analyses,
        'job_roles_dict': job_roles_dict,
    }
    return render(request, 'analyzer/leaderboard.html', context)

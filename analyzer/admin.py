from django.contrib import admin
from .models import SkillAnalysis

@admin.register(SkillAnalysis)
class SkillAnalysisAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_job_role_display', 'experience_level', 'skill_score', 'created_at']
    list_filter = ['job_role', 'experience_level']
    search_fields = ['name', 'email']
    readonly_fields = ['created_at', 'skill_score']

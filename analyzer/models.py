from django.db import models

JOB_ROLES = [
    ('software_engineer', 'Software Engineer'),
    ('data_scientist', 'Data Scientist'),
    ('web_developer', 'Web Developer'),
    ('devops_engineer', 'DevOps Engineer'),
    ('ml_engineer', 'Machine Learning Engineer'),
    ('product_manager', 'Product Manager'),
    ('ui_ux_designer', 'UI/UX Designer'),
    ('cybersecurity_analyst', 'Cybersecurity Analyst'),
    ('cloud_architect', 'Cloud Architect'),
    ('data_analyst', 'Data Analyst'),
    ('android_developer', 'Android Developer'),
    ('ios_developer', 'iOS Developer'),
    ('blockchain_developer', 'Blockchain Developer'),
    ('full_stack_developer', 'Full Stack Developer'),
    ('backend_developer', 'Backend Developer'),
]

EXPERIENCE_LEVELS = [
    ('fresher', 'Fresher (0-1 year)'),
    ('junior', 'Junior (1-3 years)'),
    ('mid', 'Mid-Level (3-5 years)'),
    ('senior', 'Senior (5+ years)'),
]

REQUIRED_SKILLS = {
    'software_engineer': {
        'core': ['Python', 'Java', 'C++', 'Data Structures', 'Algorithms', 'OOP', 'Git'],
        'tools': ['Linux', 'Docker', 'CI/CD', 'REST APIs', 'SQL'],
        'soft': ['Problem Solving', 'Team Collaboration', 'Communication'],
    },
    'data_scientist': {
        'core': ['Python', 'R', 'Machine Learning', 'Statistics', 'SQL', 'Data Visualization'],
        'tools': ['TensorFlow', 'PyTorch', 'Pandas', 'NumPy', 'Jupyter', 'Scikit-learn'],
        'soft': ['Analytical Thinking', 'Research Skills', 'Storytelling with Data'],
    },
    'web_developer': {
        'core': ['HTML', 'CSS', 'JavaScript', 'React', 'Node.js', 'SQL'],
        'tools': ['Git', 'REST APIs', 'Webpack', 'npm', 'MongoDB'],
        'soft': ['Attention to Detail', 'UI Sense', 'Problem Solving'],
    },
    'devops_engineer': {
        'core': ['Linux', 'Docker', 'Kubernetes', 'CI/CD', 'Python', 'Cloud'],
        'tools': ['Jenkins', 'Terraform', 'Ansible', 'Prometheus', 'Git'],
        'soft': ['Automation Mindset', 'Troubleshooting', 'Communication'],
    },
    'ml_engineer': {
        'core': ['Python', 'Machine Learning', 'Deep Learning', 'MLOps', 'SQL', 'Cloud'],
        'tools': ['TensorFlow', 'PyTorch', 'Kubeflow', 'Docker', 'Spark'],
        'soft': ['Research Orientation', 'Problem Decomposition', 'Documentation'],
    },
    'product_manager': {
        'core': ['Product Strategy', 'User Research', 'Roadmapping', 'Analytics', 'Wireframing'],
        'tools': ['Jira', 'Figma', 'Google Analytics', 'SQL'],
        'soft': ['Leadership', 'Communication', 'Empathy', 'Prioritization'],
    },
    'ui_ux_designer': {
        'core': ['UI Design', 'UX Research', 'Wireframing', 'Prototyping', 'Design Systems'],
        'tools': ['Figma', 'Adobe XD', 'Sketch', 'InVision', 'Zeplin'],
        'soft': ['Empathy', 'Attention to Detail', 'Communication', 'Creativity'],
    },
    'cybersecurity_analyst': {
        'core': ['Network Security', 'Ethical Hacking', 'SIEM', 'Incident Response', 'Python'],
        'tools': ['Wireshark', 'Metasploit', 'Nmap', 'Burp Suite', 'Splunk'],
        'soft': ['Critical Thinking', 'Attention to Detail', 'Ethical Mindset'],
    },
    'cloud_architect': {
        'core': ['AWS', 'GCP', 'Azure', 'Docker', 'Kubernetes', 'Networking', 'IaC'],
        'tools': ['Terraform', 'CloudFormation', 'Ansible', 'CI/CD'],
        'soft': ['Systems Thinking', 'Communication', 'Cost Optimization'],
    },
    'data_analyst': {
        'core': ['SQL', 'Excel', 'Python', 'Data Visualization', 'Statistics'],
        'tools': ['Power BI', 'Tableau', 'Google Analytics', 'Pandas'],
        'soft': ['Analytical Thinking', 'Storytelling', 'Attention to Detail'],
    },
    'android_developer': {
        'core': ['Java', 'Kotlin', 'Android SDK', 'REST APIs', 'SQLite', 'Git'],
        'tools': ['Android Studio', 'Firebase', 'Jetpack Compose', 'Gradle'],
        'soft': ['Problem Solving', 'UX Awareness', 'Performance Mindset'],
    },
    'ios_developer': {
        'core': ['Swift', 'Objective-C', 'iOS SDK', 'REST APIs', 'Core Data', 'Git'],
        'tools': ['Xcode', 'CocoaPods', 'Firebase', 'TestFlight'],
        'soft': ['Attention to Detail', 'UI Sensibility', 'Problem Solving'],
    },
    'blockchain_developer': {
        'core': ['Solidity', 'Web3.js', 'Ethereum', 'Smart Contracts', 'Cryptography', 'JavaScript'],
        'tools': ['Truffle', 'Hardhat', 'MetaMask', 'IPFS', 'Ganache'],
        'soft': ['Security Mindset', 'Continuous Learning', 'Research Skills'],
    },
    'full_stack_developer': {
        'core': ['HTML', 'CSS', 'JavaScript', 'React', 'Node.js', 'SQL', 'Git'],
        'tools': ['Docker', 'REST APIs', 'Redis', 'MongoDB', 'AWS'],
        'soft': ['Versatility', 'Problem Solving', 'Time Management'],
    },
    'backend_developer': {
        'core': ['Python', 'Java', 'Node.js', 'SQL', 'REST APIs', 'Authentication', 'Git'],
        'tools': ['Docker', 'Redis', 'RabbitMQ', 'Linux', 'CI/CD'],
        'soft': ['Problem Solving', 'Scalability Thinking', 'Code Quality'],
    },
}

LEARNING_RESOURCES = {
    'Python': {'platform': 'Python.org', 'url': 'https://docs.python.org/3/tutorial/', 'duration': '4-6 weeks'},
    'Java': {'platform': 'Oracle Docs', 'url': 'https://dev.java/learn/', 'duration': '6-8 weeks'},
    'JavaScript': {'platform': 'MDN Web Docs', 'url': 'https://developer.mozilla.org/en-US/docs/Learn/JavaScript', 'duration': '4-6 weeks'},
    'React': {'platform': 'React Docs', 'url': 'https://react.dev/learn', 'duration': '4-6 weeks'},
    'Machine Learning': {'platform': 'Coursera', 'url': 'https://www.coursera.org/specializations/machine-learning-introduction', 'duration': '8-12 weeks'},
    'SQL': {'platform': 'SQLZoo', 'url': 'https://sqlzoo.net', 'duration': '2-3 weeks'},
    'Docker': {'platform': 'Docker Docs', 'url': 'https://docs.docker.com/get-started/', 'duration': '2-3 weeks'},
    'Kubernetes': {'platform': 'Kubernetes.io', 'url': 'https://kubernetes.io/docs/tutorials/', 'duration': '4-6 weeks'},
    'Git': {'platform': 'Pro Git Book', 'url': 'https://git-scm.com/book/en/v2', 'duration': '1-2 weeks'},
    'AWS': {'platform': 'AWS Training', 'url': 'https://aws.amazon.com/training/', 'duration': '8-12 weeks'},
    'Data Structures': {'platform': 'GeeksforGeeks', 'url': 'https://www.geeksforgeeks.org/data-structures/', 'duration': '6-8 weeks'},
    'Algorithms': {'platform': 'LeetCode', 'url': 'https://leetcode.com/explore/', 'duration': '8-12 weeks'},
    'HTML': {'platform': 'MDN Web Docs', 'url': 'https://developer.mozilla.org/en-US/docs/Learn/HTML', 'duration': '1-2 weeks'},
    'CSS': {'platform': 'CSS Tricks', 'url': 'https://css-tricks.com/guides/', 'duration': '2-3 weeks'},
    'Node.js': {'platform': 'Node.js Docs', 'url': 'https://nodejs.org/en/learn', 'duration': '3-4 weeks'},
    'TensorFlow': {'platform': 'TensorFlow.org', 'url': 'https://www.tensorflow.org/tutorials', 'duration': '6-8 weeks'},
    'Figma': {'platform': 'Figma Learn', 'url': 'https://help.figma.com/hc/en-us', 'duration': '2-3 weeks'},
    'Solidity': {'platform': 'CryptoZombies', 'url': 'https://cryptozombies.io', 'duration': '4-6 weeks'},
    'Swift': {'platform': 'Apple Developer', 'url': 'https://developer.apple.com/tutorials/swiftui', 'duration': '6-8 weeks'},
    'Kotlin': {'platform': 'JetBrains', 'url': 'https://play.kotlinlang.org', 'duration': '4-6 weeks'},
    'Linux': {'platform': 'Linux Foundation', 'url': 'https://training.linuxfoundation.org/training/introduction-to-linux/', 'duration': '2-4 weeks'},
    'Deep Learning': {'platform': 'fast.ai', 'url': 'https://www.fast.ai', 'duration': '8-12 weeks'},
    'CI/CD': {'platform': 'GitHub Docs', 'url': 'https://docs.github.com/en/actions', 'duration': '2-3 weeks'},
    'Terraform': {'platform': 'HashiCorp Learn', 'url': 'https://developer.hashicorp.com/terraform/tutorials', 'duration': '3-4 weeks'},
    'MongoDB': {'platform': 'MongoDB University', 'url': 'https://university.mongodb.com', 'duration': '3-4 weeks'},
    'Statistics': {'platform': 'Khan Academy', 'url': 'https://www.khanacademy.org/math/statistics-probability', 'duration': '6-8 weeks'},
}


class SkillAnalysis(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    job_role = models.CharField(max_length=50, choices=JOB_ROLES)
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_LEVELS)
    current_skills = models.TextField()
    skill_score = models.FloatField(default=0)
    gap_skills = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-skill_score', '-created_at']
        verbose_name_plural = 'Skill Analyses'

    def __str__(self):
        return f"{self.name} — {self.get_job_role_display()} ({self.skill_score}%)"

    def get_current_skills_list(self):
        return [s.strip() for s in self.current_skills.split(',') if s.strip()]

    def get_gap_skills_list(self):
        return [s.strip() for s in self.gap_skills.split(',') if s.strip()]

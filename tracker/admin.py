from django.contrib import admin
from .models import ResumeProfile, JobApplication


@admin.register(ResumeProfile)
class ResumeProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "updated_at")


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ("company", "role", "user", "status", "match_score", "applied_date")
    list_filter = ("status", "applied_date")
    search_fields = ("company", "role", "missing_skills")
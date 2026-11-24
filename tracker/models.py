from django.db import models
from django.contrib.auth.models import User
from .matcher import calculate_match


class ResumeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="resume_profile")
    skills_text = models.TextField(
        default="Python, Django, DRF, PostgreSQL, TypeScript, React, Next.js, Node.js, Git",
        help_text="Comma-separated list of your skills"
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Skills"


class JobApplication(models.Model):
    class Status(models.TextChoices):
        APPLIED = "APPLIED", "Applied"
        INTERVIEW = "INTERVIEW", "Interview"
        OFFER = "OFFER", "Offer"
        REJECTED = "REJECTED", "Rejected"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")
    company = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    job_description = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.APPLIED)
    match_score = models.PositiveIntegerField(default=0, editable=False)
    missing_skills = models.CharField(max_length=255, blank=True, editable=False)
    applied_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-applied_date", "-id"]

    def save(self, *args, **kwargs):
        profile = getattr(self.user, "resume_profile", None)
        skills = profile.skills_text if profile else ""
        score, missing = calculate_match(skills, self.job_description)
        self.match_score = score
        self.missing_skills = ", ".join(missing)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.role} at {self.company} ({self.match_score}%)"
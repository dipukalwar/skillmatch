from django import forms
from .models import JobApplication, ResumeProfile


class ResumeProfileForm(forms.ModelForm):
    class Meta:
        model = ResumeProfile
        fields = ["skills_text"]
        widgets = {
            "skills_text": forms.Textarea(attrs={
                "rows": 2,
                "class": "form-control",
                "placeholder": "Python, Django, DRF, PostgreSQL, TypeScript, React, Next.js..."
            })
        }


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ["company", "role", "status", "job_description"]
        widgets = {
            "company": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. Websoft Technology Nepal"}),
            "role": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. Python Developer Intern"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "job_description": forms.Textarea(attrs={
                "rows": 4,
                "class": "form-control",
                "placeholder": "Paste the job description here to auto-calculate your skill match score..."
            }),
        }
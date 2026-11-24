from rest_framework import serializers
from .models import JobApplication


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = [
            "id", "company", "role", "status",
            "match_score", "missing_skills", "applied_date", "job_description"
        ]
        read_only_fields = ["match_score", "missing_skills", "applied_date"]
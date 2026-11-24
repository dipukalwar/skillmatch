from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from rest_framework import generics, permissions

from .models import JobApplication, ResumeProfile
from .forms import JobApplicationForm, ResumeProfileForm
from .serializers import JobApplicationSerializer


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        ResumeProfile.objects.create(user=user)
        login(request, user)
        return redirect("dashboard")
    return render(request, "tracker/signup.html", {"form": form})


@login_required
def dashboard(request):
    profile, _ = ResumeProfile.objects.get_or_create(user=request.user)
    applications = JobApplication.objects.filter(user=request.user)

    status_filter = request.GET.get("status", "")
    if status_filter:
        applications = applications.filter(status=status_filter)

    profile_form = ResumeProfileForm(instance=profile)
    app_form = JobApplicationForm()

    if request.method == "POST":
        if "update_skills" in request.POST:
            profile_form = ResumeProfileForm(request.POST, instance=profile)
            if profile_form.is_valid():
                profile_form.save()
                # Recalculate match scores for existing applications
                for app in JobApplication.objects.filter(user=request.user):
                    app.save()
                return redirect("dashboard")

        elif "add_application" in request.POST:
            app_form = JobApplicationForm(request.POST)
            if app_form.is_valid():
                application = app_form.save(commit=False)
                application.user = request.user
                application.save()
                return redirect("dashboard")

    return render(request, "tracker/dashboard.html", {
        "profile_form": profile_form,
        "app_form": app_form,
        "applications": applications,
        "status_filter": status_filter,
    })


@login_required
def update_status(request, pk):
    application = get_object_or_404(JobApplication, pk=pk, user=request.user)
    if request.method == "POST":
        new_status = request.POST.get("status")
        if new_status in JobApplication.Status.values:
            application.status = new_status
            application.save()
    return redirect("dashboard")


@login_required
def delete_application(request, pk):
    application = get_object_or_404(JobApplication, pk=pk, user=request.user)
    if request.method == "POST":
        application.delete()
    return redirect("dashboard")


# DRF REST API View (Browsable JSON API at /api/applications/)
class ApplicationListCreateAPI(generics.ListCreateAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# User Profile to store role
class UserProfile(models.Model):
    USER_ROLES = (
        ('seeker', 'Job Seeker'),
        ('employer', 'Employer'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=USER_ROLES)

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"

# Job Model
class Job(models.Model):
    JOB_TYPES = (
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary_range = models.CharField(max_length=50, blank=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPES)
    created_date = models.DateTimeField(auto_now_add=True)
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# Application Model
class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    cover_letter = models.TextField(blank=True)
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.username} applied to {self.job.title}"

    def clean(self):
        if Application.objects.filter(job=self.job, applicant=self.applicant).exists():
            raise ValidationError("You have already applied to this job.")

    class Meta:
        unique_together = ('job', 'applicant')
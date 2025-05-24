from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Job, Application

class UserSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=UserProfile.USER_ROLES, source='profile.role')

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class RegisterSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=UserProfile.USER_ROLES)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']

    def create(self, validated_data):
        role = validated_data.pop('role')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user, role=role)
        return user

class JobSerializer(serializers.ModelSerializer):
    employer = UserSerializer(read_only=True)

    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'location', 'salary_range', 'job_type', 'created_date', 'employer', 'is_active']
        read_only_fields = ['employer', 'created_date']

class ApplicationSerializer(serializers.ModelSerializer):
    job = JobSerializer(read_only=True)
    applicant = UserSerializer(read_only=True)

    class Meta:
        model = Application
        fields = ['id', 'job', 'applicant', 'cover_letter', 'date_applied']
        read_only_fields = ['applicant', 'date_applied']
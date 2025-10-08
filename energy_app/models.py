from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"


class EnergyPrediction(models.Model):
    MODEL_CHOICES = [
        ('linear', 'Linear Regression'),
        ('xgboost', 'XGBoost'),
        ('random_forest', 'Random Forest'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_datetime = models.DateTimeField()
    predicted_consumption = models.FloatField()
    model_used = models.CharField(max_length=50, choices=MODEL_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.predicted_consumption:.2f} MW"


class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    description = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.user.username} - {self.activity_type}"
from django.contrib import admin
from .models import UserProfile, EnergyPrediction, UserActivity


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'location', 'created_at']
    list_filter = ['created_at', 'location']
    search_fields = ['user__username', 'user__email', 'location']


@admin.register(EnergyPrediction)
class EnergyPredictionAdmin(admin.ModelAdmin):
    list_display = ['user', 'input_datetime', 'predicted_consumption', 'model_used', 'created_at']
    list_filter = ['model_used', 'created_at']
    search_fields = ['user__username']
    date_hierarchy = 'created_at'


@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ['user', 'activity_type', 'timestamp']
    list_filter = ['activity_type', 'timestamp']
    search_fields = ['user__username', 'activity_type', 'description']
    date_hierarchy = 'timestamp'
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.db.models import Count, Avg
from django.utils import timezone
from datetime import timedelta

from .models import UserProfile, UserActivity, EnergyPrediction
from .forms import UserProfileForm, CustomUserCreationForm, EnergyPredictionForm
from .ml_predictor import EnergyPredictor


@login_required
def dashboard_view(request):
    """Main dashboard showing user statistics."""
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    # Get user statistics
    total_predictions = EnergyPrediction.objects.filter(user=request.user).count()
    
    week_ago = timezone.now() - timedelta(days=7)
    weekly_predictions = EnergyPrediction.objects.filter(
        user=request.user, 
        created_at__gte=week_ago
    ).count()
    
    avg_consumption = EnergyPrediction.objects.filter(user=request.user).aggregate(
        avg=Avg('predicted_consumption')
    )['avg'] or 0
    
    recent_predictions = EnergyPrediction.objects.filter(user=request.user)[:5]
    recent_activities = UserActivity.objects.filter(user=request.user)[:5]
    
    context = {
        'profile': profile,
        'total_predictions': total_predictions,
        'weekly_predictions': weekly_predictions,
        'avg_consumption': round(avg_consumption, 2),
        'recent_predictions': recent_predictions,
        'recent_activities': recent_activities,
    }
    
    return render(request, 'dashboard.html', context)


@login_required
def predict_energy(request):
    """Energy prediction page."""
    if request.method == 'POST':
        form = EnergyPredictionForm(request.POST)
        if form.is_valid():
            input_datetime = form.cleaned_data['input_datetime']
            model_choice = form.cleaned_data['model_choice']
            
            # Make prediction using our simple ML predictor
            predictor = EnergyPredictor()
            predicted_consumption = predictor.predict(input_datetime, model_choice)
            
            # Save prediction
            prediction = EnergyPrediction.objects.create(
                user=request.user,
                input_datetime=input_datetime,
                predicted_consumption=predicted_consumption,
                model_used=model_choice
            )
            
            # Log activity
            UserActivity.objects.create(
                user=request.user,
                activity_type='energy_prediction',
                description=f'Predicted {predicted_consumption:.2f} MW for {input_datetime.strftime("%Y-%m-%d %H:%M")}'
            )
            
            messages.success(request, f'Energy consumption predicted: {predicted_consumption:.2f} MW')
            return redirect('predict_energy')
    else:
        form = EnergyPredictionForm()
    
    recent_predictions = EnergyPrediction.objects.filter(user=request.user)[:10]
    
    return render(request, 'predict_energy.html', {
        'form': form,
        'recent_predictions': recent_predictions
    })


@login_required
def analytics_view(request):
    """Analytics dashboard."""
    predictions_by_model = EnergyPrediction.objects.filter(user=request.user).values('model_used').annotate(count=Count('id'))
    
    thirty_days_ago = timezone.now() - timedelta(days=30)
    daily_predictions = EnergyPrediction.objects.filter(
        user=request.user,
        created_at__gte=thirty_days_ago
    ).extra({'date': 'date(created_at)'}).values('date').annotate(count=Count('id'))
    
    consumption_trends = EnergyPrediction.objects.filter(user=request.user).order_by('created_at')[:20]
    
    context = {
        'predictions_by_model': predictions_by_model,
        'daily_predictions': daily_predictions,
        'consumption_trends': consumption_trends,
    }
    
    return render(request, 'analytics.html', context)


@login_required
def profile_view(request):
    """User profile management."""
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            
            UserActivity.objects.create(
                user=request.user,
                activity_type='profile_update',
                description='Updated user profile information'
            )
            
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile, user=request.user)
    
    return render(request, 'profile.html', {'form': form, 'profile': profile})


def register_view(request):
    """User registration."""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            UserProfile.objects.create(user=user)
            
            UserActivity.objects.create(
                user=user,
                activity_type='registration',
                description=f'User {username} registered for the energy prediction platform'
            )
            
            messages.success(request, f'Account created successfully for {username}!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from energy_app.models import EnergyPrediction, UserActivity
from django.utils import timezone
from datetime import timedelta
import random

class Command(BaseCommand):
    help = 'Create test prediction data for analytics'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, help='Username to create data for', default='admin')

    def handle(self, *args, **options):
        username = options['username']
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(f'User "{username}" does not exist. Please create the user first.')
            )
            return

        # Delete existing predictions for this user
        EnergyPrediction.objects.filter(user=user).delete()
        
        # Create test predictions
        models = ['linear', 'xgboost', 'random_forest']
        
        for i in range(15):
            # Create predictions for the last 15 days
            prediction_date = timezone.now() - timedelta(days=i)
            model_choice = random.choice(models)
            
            # Create 1-3 predictions per day
            for j in range(random.randint(1, 3)):
                prediction_time = prediction_date + timedelta(hours=random.randint(0, 23))
                consumption = random.uniform(12000, 18000)
                
                EnergyPrediction.objects.create(
                    user=user,
                    input_datetime=prediction_time,
                    predicted_consumption=consumption,
                    model_used=model_choice,
                    created_at=prediction_date + timedelta(hours=j)
                )
        
        # Create some activities
        for i in range(10):
            UserActivity.objects.create(
                user=user,
                activity_type='energy_prediction',
                description=f'Test prediction {i+1}',
                timestamp=timezone.now() - timedelta(days=random.randint(0, 7))
            )
        
        total_predictions = EnergyPrediction.objects.filter(user=user).count()
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {total_predictions} test predictions for user "{username}"')
        )
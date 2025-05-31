from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Users
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='password1')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='password2')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='password3')

        # Teams
        team1 = Team.objects.create(name='Team Octopus')
        team1.members.add(user1, user2)
        team2 = Team.objects.create(name='Team Squid')
        team2.members.add(user3)

        # Workouts
        workout1 = Workout.objects.create(name='5K Run', description='Run 5 kilometers', points=50)
        workout2 = Workout.objects.create(name='Pushups', description='Do 50 pushups', points=20)

        # Activities
        Activity.objects.create(user=user1, activity_type='run', duration=30)
        Activity.objects.create(user=user2, activity_type='pushups', duration=10)
        Activity.objects.create(user=user3, activity_type='run', duration=25)

        # Leaderboard
        Leaderboard.objects.create(user=user1, points=70)
        Leaderboard.objects.create(user=user2, points=20)
        Leaderboard.objects.create(user=user3, points=50)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))

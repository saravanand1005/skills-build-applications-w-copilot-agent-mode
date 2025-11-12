from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team', description='desc')
        self.assertEqual(str(team), 'Test Team')
    def test_user_create(self):
        team = Team.objects.create(name='T', description='d')
        user = User.objects.create(name='U', email='u@test.com', team=team)
        self.assertEqual(str(user), 'U')
    def test_workout_create(self):
        workout = Workout.objects.create(name='W', description='d', difficulty='Easy')
        self.assertEqual(str(workout), 'W')
    def test_leaderboard_create(self):
        team = Team.objects.create(name='T2', description='d2')
        user = User.objects.create(name='U2', email='u2@test.com', team=team)
        lb = Leaderboard.objects.create(user=user, score=10, rank=1)
        self.assertEqual(str(lb), 'U2 - Rank 1')
    def test_activity_create(self):
        team = Team.objects.create(name='T3', description='d3')
        user = User.objects.create(name='U3', email='u3@test.com', team=team)
        act = Activity.objects.create(user=user, type='Run', duration=10, date='2025-11-12')
        self.assertEqual(str(act), 'U3 - Run')

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import date


class UserAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        User.objects.all().delete()
        self.user = User.objects.create(
            username='ironman',
            email='tony@avengers.com',
            password='starktech123',
        )

    def test_list_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_user(self):
        response = self.client.post('/api/users/', {
            'username': 'spiderman',
            'email': 'peter@avengers.com',
            'password': 'webslinger123',
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_user(self):
        response = self.client.get(f'/api/users/{self.user.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'ironman')


class TeamAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        Team.objects.all().delete()
        self.team = Team.objects.create(name='Team Marvel', members=['ironman', 'spiderman'])

    def test_list_teams(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_team(self):
        response = self.client.post('/api/teams/', {
            'name': 'Team DC',
            'members': ['batman', 'superman'],
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_team(self):
        response = self.client.get(f'/api/teams/{self.team.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Team Marvel')


class ActivityAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        Activity.objects.all().delete()
        self.activity = Activity.objects.create(
            user='ironman',
            activity_type='Flight Training',
            duration=45.0,
            date=date(2024, 1, 10),
        )

    def test_list_activities(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_activity(self):
        response = self.client.post('/api/activities/', {
            'user': 'thor',
            'activity_type': 'Hammer Throwing',
            'duration': 30.0,
            'date': '2024-01-12',
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_activity(self):
        response = self.client.get(f'/api/activities/{self.activity.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], 'ironman')


class LeaderboardAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        Leaderboard.objects.all().delete()
        self.entry = Leaderboard.objects.create(user='superman', score=1000)

    def test_list_leaderboard(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_leaderboard_entry(self):
        response = self.client.post('/api/leaderboard/', {
            'user': 'thor',
            'score': 990,
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_leaderboard_entry(self):
        response = self.client.get(f'/api/leaderboard/{self.entry.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], 'superman')


class WorkoutAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        Workout.objects.all().delete()
        self.workout = Workout.objects.create(
            name='Avengers Strength Training',
            description='Full-body workout inspired by Earth\'s Mightiest Heroes',
            exercises=['Iron Man Bench Press', 'Thor Hammer Curls'],
        )

    def test_list_workouts(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_workout(self):
        response = self.client.post('/api/workouts/', {
            'name': 'JLA Speed & Agility',
            'description': 'High-intensity workout for Justice League members',
            'exercises': ['Flash Sprint Intervals', 'Superman Flying Push-Ups'],
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_workout(self):
        response = self.client.get(f'/api/workouts/{self.workout.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Avengers Strength Training')


class ApiRootTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_api_root(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)

    def test_root_redirects_to_api(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

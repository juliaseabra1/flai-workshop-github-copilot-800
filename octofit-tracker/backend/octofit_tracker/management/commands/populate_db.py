from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Cleared existing data.')

        # Create users - Marvel heroes
        users_data = [
            {'username': 'ironman', 'email': 'tony@avengers.com', 'password': 'starktech123', 'first_name': 'Tony', 'last_name': 'Stark', 'team': 'Team Marvel'},
            {'username': 'spiderman', 'email': 'peter@avengers.com', 'password': 'webslinger123', 'first_name': 'Peter', 'last_name': 'Parker', 'team': 'Team Marvel'},
            {'username': 'thor', 'email': 'thor@avengers.com', 'password': 'mjolnir123', 'first_name': 'Thor', 'last_name': 'Odinson', 'team': 'Team Marvel'},
            {'username': 'blackwidow', 'email': 'natasha@avengers.com', 'password': 'shield123', 'first_name': 'Natasha', 'last_name': 'Romanoff', 'team': 'Team Marvel'},
            {'username': 'hulk', 'email': 'bruce@avengers.com', 'password': 'smash123', 'first_name': 'Bruce', 'last_name': 'Banner', 'team': 'Team Marvel'},
            # DC heroes
            {'username': 'batman', 'email': 'bruce@jla.com', 'password': 'darknight123', 'first_name': 'Bruce', 'last_name': 'Wayne', 'team': 'Team DC'},
            {'username': 'superman', 'email': 'clark@jla.com', 'password': 'krypton123', 'first_name': 'Clark', 'last_name': 'Kent', 'team': 'Team DC'},
            {'username': 'wonderwoman', 'email': 'diana@jla.com', 'password': 'lasso123', 'first_name': 'Diana', 'last_name': 'Prince', 'team': 'Team DC'},
            {'username': 'flash', 'email': 'barry@jla.com', 'password': 'speed123', 'first_name': 'Barry', 'last_name': 'Allen', 'team': 'Team DC'},
            {'username': 'aquaman', 'email': 'arthur@jla.com', 'password': 'atlantis123', 'first_name': 'Arthur', 'last_name': 'Curry', 'team': 'Team DC'},
        ]
        users = []
        for u in users_data:
            user = User.objects.create(**u)
            users.append(user)
        self.stdout.write(f'Created {len(users)} users.')

        # Create teams
        marvel_members = [u.username for u in users[:5]]
        dc_members = [u.username for u in users[5:]]

        team_marvel = Team.objects.create(name='Team Marvel', members=marvel_members)
        team_dc = Team.objects.create(name='Team DC', members=dc_members)
        self.stdout.write('Created Team Marvel and Team DC.')

        # Create activities
        activities_data = [
            {'user': 'ironman', 'activity_type': 'Flight Training', 'duration': 45.0, 'date': date(2024, 1, 10)},
            {'user': 'spiderman', 'activity_type': 'Web Slinging', 'duration': 60.0, 'date': date(2024, 1, 11)},
            {'user': 'thor', 'activity_type': 'Hammer Throwing', 'duration': 30.0, 'date': date(2024, 1, 12)},
            {'user': 'blackwidow', 'activity_type': 'Martial Arts', 'duration': 90.0, 'date': date(2024, 1, 13)},
            {'user': 'hulk', 'activity_type': 'Smashing', 'duration': 20.0, 'date': date(2024, 1, 14)},
            {'user': 'batman', 'activity_type': 'Cape Gliding', 'duration': 50.0, 'date': date(2024, 1, 10)},
            {'user': 'superman', 'activity_type': 'Flying', 'duration': 75.0, 'date': date(2024, 1, 11)},
            {'user': 'wonderwoman', 'activity_type': 'Lasso Training', 'duration': 55.0, 'date': date(2024, 1, 12)},
            {'user': 'flash', 'activity_type': 'Speed Running', 'duration': 15.0, 'date': date(2024, 1, 13)},
            {'user': 'aquaman', 'activity_type': 'Swimming', 'duration': 80.0, 'date': date(2024, 1, 14)},
        ]
        for a in activities_data:
            Activity.objects.create(**a)
        self.stdout.write(f'Created {len(activities_data)} activities.')

        # Create leaderboard
        leaderboard_data = [
            {'user': 'ironman', 'score': 950},
            {'user': 'spiderman', 'score': 870},
            {'user': 'thor', 'score': 990},
            {'user': 'blackwidow', 'score': 920},
            {'user': 'hulk', 'score': 830},
            {'user': 'batman', 'score': 960},
            {'user': 'superman', 'score': 1000},
            {'user': 'wonderwoman', 'score': 940},
            {'user': 'flash', 'score': 850},
            {'user': 'aquaman', 'score': 810},
        ]
        for entry in leaderboard_data:
            Leaderboard.objects.create(**entry)
        self.stdout.write(f'Created {len(leaderboard_data)} leaderboard entries.')

        # Create workouts
        workouts_data = [
            {
                'name': 'Avengers Strength Training',
                'description': 'Full-body workout inspired by Earth\'s Mightiest Heroes',
                'exercises': ['Iron Man Bench Press', 'Thor Hammer Curls', 'Hulk Squat', 'Spider-Man Pull-Ups', 'Black Widow Planks'],
                'difficulty_level': 'Advanced',
                'duration_minutes': 45,
                'calories_target': 450,
            },
            {
                'name': 'JLA Speed & Agility',
                'description': 'High-intensity workout for Justice League members',
                'exercises': ['Flash Sprint Intervals', 'Superman Flying Push-Ups', 'Batman Stealth Burpees', 'Wonder Woman Rope Training', 'Aquaman Swim Laps'],
                'difficulty_level': 'Intermediate',
                'duration_minutes': 40,
                'calories_target': 400,
            },
            {
                'name': 'Hero Cardio Blast',
                'description': 'Cardio circuit for all superheroes',
                'exercises': ['Web Slinging Jumps', 'Cape Gliding Planks', 'Mjolnir Swings', 'Lasso Jumps', 'Trident Rows'],
                'difficulty_level': 'Beginner',
                'duration_minutes': 30,
                'calories_target': 300,
            },
            {
                'name': 'Marvel HIIT',
                'description': 'High-intensity interval training Marvel-style',
                'exercises': ['Arc Reactor Crunches', 'Shield Throws', 'Web Crawl', 'Gamma Radiation Lunges', 'Quantum Realm Jumps'],
                'difficulty_level': 'Advanced',
                'duration_minutes': 35,
                'calories_target': 420,
            },
            {
                'name': 'DC Power Circuit',
                'description': 'Power circuit for DC heroes',
                'exercises': ['Kryptonian Deadlift', 'Dark Knight Push-Ups', 'Amazonian Warrior Row', 'Speed Force Shuttle Run', 'Atlantean Dive'],
                'difficulty_level': 'Intermediate',
                'duration_minutes': 50,
                'calories_target': 500,
            },
        ]
        for w in workouts_data:
            Workout.objects.create(**w)
        self.stdout.write(f'Created {len(workouts_data)} workouts.')

        self.stdout.write(self.style.SUCCESS('Successfully populated octofit_db with superhero test data!'))

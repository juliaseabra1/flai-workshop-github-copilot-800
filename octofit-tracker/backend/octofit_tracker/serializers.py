from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    team_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'team', 'team_name', 'date_joined']
        extra_kwargs = {'password': {'write_only': True}}

    def get_id(self, obj):
        return str(obj._id) if obj._id else None

    def get_team_name(self, obj):
        if obj.team:
            try:
                team = Team.objects.get(name=obj.team)
                return team.name
            except Team.DoesNotExist:
                return obj.team
        return None


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    members = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ['id', 'name', 'members']

    def get_id(self, obj):
        return str(obj._id) if obj._id else None

    def get_members(self, obj):
        if isinstance(obj.members, str):
            # If members is stored as a string, parse it
            import ast
            try:
                return ast.literal_eval(obj.members)
            except:
                return []
        return obj.members if obj.members else []


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration', 'date']

    def get_id(self, obj):
        return str(obj._id) if obj._id else None


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()
    team_name = serializers.SerializerMethodField()
    total_calories = serializers.SerializerMethodField()

    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'user_name', 'team_name', 'total_calories']

    def get_id(self, obj):
        return str(obj._id) if obj._id else None

    def get_user_name(self, obj):
        return obj.user

    def get_team_name(self, obj):
        # Find the team this user belongs to
        try:
            teams = Team.objects.all()
            for team in teams:
                members = team.members
                if isinstance(members, str):
                    import ast
                    try:
                        members = ast.literal_eval(members)
                    except:
                        members = []
                if obj.user in members:
                    return team.name
            return 'N/A'
        except:
            return 'N/A'

    def get_total_calories(self, obj):
        # Calculate total calories from activities
        # For now, use score as calories (can be enhanced to calculate from activities)
        return obj.score if obj.score else 0


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'exercises', 'difficulty_level', 'duration_minutes', 'calories_target']

    def get_id(self, obj):
        return str(obj._id) if obj._id else None

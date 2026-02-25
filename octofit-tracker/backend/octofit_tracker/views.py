from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import (
    UserSerializer,
    TeamSerializer,
    ActivitySerializer,
    LeaderboardSerializer,
    WorkoutSerializer,
)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'teams': reverse('team-list', request=request, format=format),
        'activities': reverse('activity-list', request=request, format=format),
        'leaderboard': reverse('leaderboard-list', request=request, format=format),
        'workouts': reverse('workout-list', request=request, format=format),
    })


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def get_object(self):
        """Override to handle MongoDB ObjectID lookups"""
        from bson import ObjectId
        try:
            obj_id = self.kwargs.get(self.lookup_field)
            # Try to convert to ObjectId if it's a valid hex string
            if len(obj_id) == 24:
                return self.queryset.get(_id=ObjectId(obj_id))
        except:
            pass
        return super().get_object()


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

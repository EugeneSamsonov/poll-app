from rest_framework.serializers import ModelSerializer

from users.models import PollUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = PollUser
        fields = ("id", "username", "email", "first_name", "last_name", "is_staff")

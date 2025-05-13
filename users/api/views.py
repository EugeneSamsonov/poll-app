from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from users.api.permissions import IsOwnerOrReadOnly

from .serializers import UserSerializer
from users.models import PollUser


class UserViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = PollUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]

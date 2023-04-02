from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from users.serializers import UserSerializer, UserModel


# Create your views here.

class UserLCView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects
    permission_classes = (AllowAny,)

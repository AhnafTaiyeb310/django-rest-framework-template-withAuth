from djoser.serializers import UserCreatePasswordRetypeSerializer as BaseUserUserCreatePasswordRetypeSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer

class UserCreatePasswordRetypeSerializer(BaseUserUserCreatePasswordRetypeSerializer):
    class Meta(BaseUserUserCreatePasswordRetypeSerializer.Meta):
        fields = ["id", "first_name", "last_name", "username", "email", "password", ]
        ref_name = "CustomUserCreateSerializer"

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ["id", "username", "email", "first_name", "last_name"]
        ref_name = "CustomUserSerializer"
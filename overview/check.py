from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class SuperuserGoogleBackend(ModelBackend):
    def authenticate(self, request, socialaccount=None, **kwargs):
        if socialaccount:
            user = socialaccount.user
            if user.is_superuser:
                return user
        return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel._default_manager.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
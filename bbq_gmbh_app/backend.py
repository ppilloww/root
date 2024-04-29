from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

#this is my custom backend for authentication

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            print("User does not exist")
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            print("User authenticated")
            return user
        else:
            print("Incorrect password or user cannot authenticate")  # Add this line
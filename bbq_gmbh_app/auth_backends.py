# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth import get_user_model

# #this is my custom backend for authentication

# class EmailBackend(ModelBackend):
#     def authenticate(self, request, email=None, password=None, **kwargs):
#         User = get_user_model()
#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             print("User does not exist")
#             return None

#         if user.check_password(password) and self.user_can_authenticate(user):
#             print("User authenticated")
#             return user
#         else:
#             print("Incorrect password or user cannot authenticate")  # Add this line

# from django.contrib.auth.backends import BaseBackend
# from .models import Mitarbeiter  # Import your custom user model

# class CustomAuthBackend(BaseBackend):
#     def authenticate(self, request, email=None, password=None):
#         try:
#             user = Mitarbeiter.objects.get(email=email, passwort=password)
#             return user
#         except Mitarbeiter.DoesNotExist:
#             return None

#     def get_user(self, user_id):
#         try:
#             return Mitarbeiter.objects.get(pk=user_id)
#         except Mitarbeiter.DoesNotExist:
#             return None

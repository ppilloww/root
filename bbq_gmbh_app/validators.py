from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password

class OldPasswordValidator:
    def validate(self, password, user=None):
        if user is not None and check_password(password, user.password):
            raise ValidationError("You can't use your old password.")

    def get_help_text(self):
        return "Your new password can't be the same as your old password."
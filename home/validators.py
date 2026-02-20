import re
from django.core.exceptions import ValidationError

class StrongPasswordValidator:
    def validate(self, password, user=None):
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password):
            raise ValidationError("Password must contain at least one digit.")
        if not any(char.isupper() for char in password):
            raise ValidationError("Password must contain at least one uppercase letter.")
        if not any(char in "!@#$%^&*()_+" for char in password):
            raise ValidationError("Password must contain at least one special character (!@#$%^&*()_+).")

    def get_help_text(self):
        return "Your password must be at least 8 characters long, include at least one number, one uppercase letter, and one special character."

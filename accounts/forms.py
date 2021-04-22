# We import the CustomUser model via get_user_model which looks to our AUTH_USER_MODEL config in settings.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

"""
    We create two new forms–CustomUserCreationForm and CustomUserChangeForm–that extend
    the base user forms imported above and specify swapping in our CustomUser model and
    displaying the fields email and username. The password field is implicitly included by default
    and so does not need to be explicitly named here as well.
"""


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "username")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "username")

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password1', 'password2']
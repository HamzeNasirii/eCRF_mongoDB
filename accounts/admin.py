from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import AbstractUser


class CustomUserAdmin(UserAdmin):
    model = AbstractUser
    add_form = CustomUserCreationForm
    list_display = ('username', 'password1', 'password2')
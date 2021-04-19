# https://stackoverflow.com/questions/51674627/insufficient-permissions-in-vscode
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    pass
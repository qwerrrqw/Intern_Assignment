from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.permissions import UserRole

class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True)
    nickname = models.CharField(max_length=15, unique=True)
    roles = models.CharField(max_length=10, choices=UserRole.choices(), default=UserRole.USER.value)

    def has_role(self, role: UserRole) -> bool:
        return self.roles == role.value


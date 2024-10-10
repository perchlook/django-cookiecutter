from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from db.models import CreatedUpdatedMixin


class User(AbstractUser, CreatedUpdatedMixin):
    id = models.AutoField(primary_key=True)
    objects: UserManager = UserManager()

    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.name}: {self.email}'

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

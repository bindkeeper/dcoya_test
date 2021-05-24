from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import logging

# Create your models here.

logger = logging.getLogger(__name__)


class UserManager(BaseUserManager):

    def create_user(self, username, password):
        if not username:
            raise ValueError('username is required')
        if not password:
            raise ValueError('password is required')
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        logger.info("create_superuser called")
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    jwt = models.TextField(blank=True, null=True)
    jwt_expiration = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True




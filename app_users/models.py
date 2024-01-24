from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone


class MyUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """Creates and saves a User with the given email and password."""

        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email).lower()
        if not password:
            raise ValueError("The given password must be set")
        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=250)
    email = models.EmailField("email", unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField("staff status", default=False)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    friends = models.ManyToManyField("self")
    profile_pic = models.ImageField(upload_to="profile_pics", null=True, blank=True)
    is_online = models.BooleanField(default=False)
    last_online = models.DateTimeField(null=True, blank=True)
    last_position = models.DateTimeField(null=True, blank=True)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def save(self, *args, **kwargs):
        if self.id:
            old_user = User.objects.get(id=self.id)
            if old_user.is_online is True and old_user.is_onlin != self.email:
                self.last_online = timezone.now()
        super(User, self).save()

    # def activate(self, *args, **kwargs):
    #     self.is_active = True
    #     self.save()

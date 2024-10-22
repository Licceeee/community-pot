from uuid import uuid4
import time
import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.cache import cache
from django.conf import settings


def img_dir_path(instance, filename):
    ext = filename.split(".")[-1]
    if instance.pk:
        filename = f"{instance.pk}.{ext}"
    else:
        # set filename as random string
        filename = f"{uuid4().hex}.{ext}"
    return f"user/{filename}"


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(
        max_length=255,
        null=True,
        verbose_name=_("Firstname"),
    )
    last_name = models.CharField(
        max_length=255,
        null=True,
        verbose_name=_("Lastname"),
    )
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_groups(self):
        return [group.name for group in self.groups.all()]

    get_groups.short_description = _("Groups")


class LastActiveManager(models.Manager):
    """
    Manager for LastActive objects
    Provides 2 utility methods
    """

    def seen(self, user, force=False):
        """
        Mask an user last on database seen
        The last seen object is only updates is LAST_SEEN_INTERVAL seconds
        passed from last update or force=True
        """
        args = {"user": user}
        seen, created = self.get_or_create(**args)
        if created:
            return seen

        # if we get the object, see if we need to update
        limit = timezone.now() - datetime.timedelta(
            seconds=settings.LAST_SEEN_INTERVAL,
        )
        if seen.last_active < limit or force:
            seen.last_active = timezone.now()
            seen.save()

        return seen

    def when(self, user):
        args = {"user": user}
        return self.filter(**args).latest("last_active").last_active


class LastActive(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    last_active = models.DateTimeField(default=timezone.now)

    objects = LastActiveManager()

    class Meta:
        ordering = ("-last_active",)

    def __unicode__(self):
        return f"{self.user} on {self.last_active}"


def get_cache_key(user):
    """
    Get cache database to cache last database write timestamp
    """
    return f"last_active:{user.pk}"


def user_seen(user):
    """
    Mask an user last seen on database if LAST_SEEN_INTERVAL seconds
    have passed from last database write.
    """
    cache_key = get_cache_key(user)
    # compute limit to update db
    limit = time.time() - settings.LAST_SEEN_INTERVAL
    seen = cache.get(cache_key)
    if not seen or seen < limit:
        # mark the database and the cache, if interval is cleared force
        # database write
        if seen == -1:
            LastActive.objects.seen(user, force=True)
        else:
            LastActive.objects.seen(user)
        timeout = settings.LAST_SEEN_INTERVAL
        cache.set(cache_key, time.time(), timeout)


def clear_interval(user):
    """
    Clear cached interval from last database write timestamp
    Usefuf if you want to force a database write for an user
    """
    keys = {}
    for last_active in LastActive.objects.filter(user=user):
        cache_key = get_cache_key(user)
        keys[cache_key] = -1

    if keys:
        cache.set_many(keys)

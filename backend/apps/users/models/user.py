from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    """
    Пользователь системы
    """

    class Gender(models.IntegerChoices):
        MALE = 0, _("Мужчина")
        FEMALE = 1, _("Женщина")

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, "
            "digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("Имя"), max_length=30, blank=True)
    last_name = models.CharField(_("Фамилия"), max_length=150, blank=True)
    second_name = models.CharField(_("Отчество"), max_length=150, blank=True)
    gender = models.IntegerField(
        _("Пол"), choices=Gender.choices, null=True, blank=True
    )
    is_sportsman = models.BooleanField(
        _("Пользователь является спортсменом"), default=False
    )
    is_employee = models.BooleanField(
        _("Пользователь является сотрудником"), default=False
    )
    is_examination_templates_manager = models.BooleanField(
        _("User is examination templates manager"), default=False
    )

    email = models.EmailField(_("Адрес электронной почты"), blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Имеет допуск к django-admin"),
    )
    birthday = models.DateField(_("Дата рождения"), blank=True, null=True)
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_("Является активныи"),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
        "last_name",
        "first_name",
        "email",
        "is_staff",
        "is_active",
    ]

    class Meta:
        swappable = "AUTH_USER_MODEL"
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

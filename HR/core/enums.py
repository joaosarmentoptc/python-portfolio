from django.utils.translation import gettext_lazy as _
from django.db import models


class PersonalTitle(models.TextChoices):
    EMPTY = "", _("---------")
    MISTER = "MR", _("Mister")
    MISS = "MS", _("Miss")


class MaritalStatus(models.TextChoices):
    EMPTY = "", _("---------")
    MARRIED = "MARRIED", _("Married")
    SINGLE = "SINGLE", _("Single")
    DIVORCED = "DIVORCED", _("Divorced")
    WIDOWED = "WIDOWED", _("Widowed")
    PARTNERSHIP = "PARTNERSHIP", _("Partnership")


class Gender(models.TextChoices):
    EMPTY = "", _("---------")
    MALE = "M", _("Male")
    FEMALE = "F", _("Female")
    OTHER = "O", _("Other")


class SupervisorType(models.TextChoices):
    DIRECT = "D", _("Direct")
    FUNCTIONAL = "F", _("Functional")


class UserStates(models.TextChoices):
    DRAFT = "draft", _("Draft"),
    MARKED_AS_JOINER = "marked_as_joiner", _("Marked as Joiner")
    FUTURE_JOINER = "future_joiner", _("Future Joiner")
    ACTIVE = "active", _("Active")
    MARKED_AS_LEAVER = "marked_as_leaver", _("Marked as Leaver")
    FUTURE_LEAVER = "future_leaver", _("Future Leaver")
    INACTIVE = "inactive", _("Inactive")


class EmployeeType(models.TextChoices):
    INTERNAL = "INT", _("Internal")

from django.utils.translation import gettext_lazy as _
from django.db import models


class MaritalStatus(models.TextChoices):
    SINGLE = "SINGLE", _("Single")
    MARRIED = "MARRIED", _("Married")
    DIVORCED = "DIVORCED", _("Divorced")
    WIDOWED = "WIDOWED", _("Widowed")
    PARTNERSHIP = "PARTNERSHIP", _("Partnership")


class Gender(models.TextChoices):
    OTHER = "O", _("Other")
    MALE = "M", _("Male")
    FEMALE = "F", _("Female")


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


class Company(models.TextChoices):
    JUMIA = "JUMIA", _("Jumia")


class ProbationPeriod(models.TextChoices):
    _NA = "NA", _("N/A")
    _15D = "15D", _("15 Days")
    _30D = "30D", _("30 Days")
    _60D = "60D", _("60 Days")


class NetOrGross(models.TextChoices):
    NET = "N", _("NET")
    GROSS = "G", _("GROSS")

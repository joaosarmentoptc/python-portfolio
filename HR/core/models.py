from django.db import models

# Create your models here.
class Timestampable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class SoftDeletes(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        abstract = True


class Model(Timestampable, SoftDeletes, models.Model):
    class Meta:
        abstract = True
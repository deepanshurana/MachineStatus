from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class MOD(models.Model):
    owner = models.CharField(max_length=200)
    data = JSONField(default=dict)
    updatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.owner)


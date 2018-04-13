from django.db import models
from django.db.models import (
  CharField,
  IntegerField,
  DateTimeField
)

class Course(models.Model):
    code = CharField(primary_key=True, max_length=10)
    name = CharField(max_length=200)
    credits = IntegerField()
    created = DateTimeField(auto_now_add=True)

class Meta:
    model = Course
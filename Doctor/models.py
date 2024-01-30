from django.db import models
from django.db import models


class Doctor():
    Username = models.CharField(max_length=50, blank=True)
    Email = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=True)

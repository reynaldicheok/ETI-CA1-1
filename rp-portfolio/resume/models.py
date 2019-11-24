from django.db import models


class Resume(models.Model):
    title = models.CharField(max_length=100)
    profile = models.TextField()
    education = models.TextField()
    experience = models.TextField()
    cca = models.TextField()
    languages = models.TextField()
    image = models.FilePathField(path="/img")

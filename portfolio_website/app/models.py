from django.db import models


class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Myproject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=10000, null=True, blank=True)
    image_profile = models.ImageField(
        upload_to="media/images/", unique=True, null=True, blank=True
    )
    surl = models.URLField(null=True, blank=True)
    giturl = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Contribproject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=10000, null=True, blank=True)
    image_profile = models.ImageField(
        upload_to="media/images/", unique=True, null=True, blank=True
    )
    surl = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

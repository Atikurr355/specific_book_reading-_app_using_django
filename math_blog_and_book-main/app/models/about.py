from django.db import models


class About(models.Model):
    name = models.CharField(max_length=150)
    info = models.TextField()
    qualifications = models.TextField()
    links = models.URLField()

    def __str__(self):
        return self.name

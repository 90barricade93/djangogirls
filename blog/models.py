from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titel = models.CharField(max_length=200)
    tekst = models.TextField()
    aanmaak_datum = models.DateTimeField(default=timezone.now)
    publiceer_datum = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publiceer_datum = timezone.now()
        self.save()

    def __str__(self):
        return self.titel
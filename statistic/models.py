from django.db import models


class Statistics(models.Model):
    data = models.CharField(max_length=255)
    usd = models.CharField(max_length=255)
    eur = models.CharField(max_length=255)
    jpy = models.CharField(max_length=255)
    cny = models.CharField(max_length=255)

    def __str__(self):
        return self.date

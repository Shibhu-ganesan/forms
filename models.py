from django.db import models


class StartUp(models.Model):
    Name = models.CharField(max_length=50, null=False)
    Field = models.CharField(max_length=50, null=False)
    Email = models.EmailField(null=False)
    Description = models.TextField(max_length=500, blank=False, null=False)

    def __str__(self):
        return self.Name


class Member(models.Model):
    Name = models.CharField(max_length=50, null=False)
    Field = models.CharField(max_length=50, null=False)
    Email = models.EmailField(null=False)
    Query = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.Name


class Investor(models.Model):
    Name = models.CharField(max_length=50, null=False)
    Email = models.EmailField(null=False)
    Field = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.Name

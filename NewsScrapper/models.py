from django.db import models

# Create your models here.

language_choices = (
    ('Turkish','Turkish'),
    ('English', 'English'),
    ('Arabic', 'Arabic'),
    ('Farsi', 'Farsi')
)

class NewsArticle(models.Model):
    headlineOrg = models.CharField(max_length=300)
    headlineEng = models.CharField(max_length=300)
    date = models.CharField(max_length=30)
    articleUrl = models.CharField(max_length=300)

class News(models.Model):
    source = models.CharField(max_length=30)
    webisteUrl = models.CharField(max_length=300)
    artilce = models.ManyToManyField(NewsArticle, blank=True)
    language = models.CharField(max_length=30, choices=language_choices)

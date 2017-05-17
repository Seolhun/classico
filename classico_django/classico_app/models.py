from django.db import models


class Topic(models.Model):
    topic_name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.topic_name
    
class WebPage(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length= 255, unique=True)
    url = models.URLField(unique=True)
    
    def __str__(self):
        return self.name
    
class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage)
    date = models.DateField()
    
    def __str__(self):
        return self.date
        
    
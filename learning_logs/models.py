from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    text = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    @property
    def uppercase(self):
        return self.text.capitalize()


    def __str__(self):
        return self.text
 

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        return self.text[:50] + "..."
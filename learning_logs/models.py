from django.db import models

class Topic(models.Model):
    """ The model for the topic user is learning currently."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

class Entry(models.Model):
    """ more text field for other things about a topic """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """ Return the string representation of the created model"""
        return f"{self.text[:50]}..."
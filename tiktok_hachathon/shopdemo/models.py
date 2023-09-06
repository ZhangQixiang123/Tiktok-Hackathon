from django.db import models

# Create your models here.

from django.urls import reverse
import uuid

class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, 
                          help_text='Unique ID for this video')
    name = models.CharField(max_length=200)
    photo = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    tag = models.CharField(max_length=200)

    # Metadata
    class Meta:
        ordering = ['name']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of Video."""
        return reverse('video_detail', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name



class Commodity(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, 
                          help_text='Unique ID for this commodity')
    name = models.CharField(max_length=200)
    photo = models.CharField(max_length=255)
    month_sell = models.IntegerField()
    seller = models.CharField(max_length=200)
    rec_from_followed = models.IntegerField()
    rec_from_friend = models.IntegerField()
    video = models.ManyToManyField(Video, help_text='Select a genre for this book', null = False)

    # Metadata
    class Meta:
        ordering = ['name']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a commodity."""
        return reverse('commodity_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name
    

from django.db import models
from django.utils.text import slugify
from django.utils import timezone


class Country(models.Model):
    COUNTRY_CHOICES = [
        # Add or update country choices as needed
        ('Argentina', 'Argentina'),
        ('Brazil', 'Brazil'),
        ('Chile', 'Chile'),
        ('Colombia', 'Colombia'),
        ('Mexico', 'Mexico'),
        ('Peru', 'Peru'),
        ('Russia', 'Russia'),
        ('United States', 'United States'), 
        ('Sweden', 'Sweden'),
        ('Norway', 'Norway'),
        ('Finland', 'Finland'),
        ('France', 'France'),
        ('Denmark', 'Denmark'),
        ('Switzerland', 'Switzerland'),
        ('Austria', 'Austria'),
        ('Belgium', 'Belgium'),
        ('Netherlands', 'Netherlands'),
        ('Portugal', 'Portugal'),
        ('Iceland', 'Iceland'),
        ('Philippines', 'Philippines'),
        ('Vietnam', 'Vietnam'),
        ('United Arab Emirates', 'United Arab Emirates'),
        ('Saudi Arabia', 'Saudi Arabia'),
        ('Canada', 'Canada'),
    ]

    country = models.CharField(choices=COUNTRY_CHOICES, max_length=30, unique=True)
    
    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.country

class Destination(models.Model):
    CATEGORY_CHOICES = [
    ('flight', 'Flight'),
    ('accommodation', 'Accommodation'),
    ('sightseeing', 'Sightseeing'),
    ('outdoor_adventure', 'Outdoor Adventure'),
    ('water_activity', 'Water Activity'),
    ('cultural_experience', 'Cultural Experience'),
    ('leisure', 'Leisure'),
    ('sports_recreation', 'Sports & Recreation'),
    ('nightlife', 'Nightlife'),
    ('workshop', 'Workshop & Learning'),
    ('wildlife_experience', 'Wildlife Experience'),
    ('adventure_sports', 'Adventure Sports'),
]


    location_name = models.CharField(max_length=100, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='destination_image')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='sightseeing')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)  # New field to track updates

    class Meta:
        verbose_name_plural = "Destinations"
        ordering = ['location_name']  # Order destinations alphabetically by name

    def __str__(self):
        return self.location_name

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.location_name):
            self.slug = slugify(self.location_name)
            print(f"Generated slug: {self.slug}")  # Debugging line
        super().save(*args, **kwargs)


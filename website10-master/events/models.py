from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.


class events(models.Model):
    eventtype = (
        ('Select the type of event', 'Select the type of event'),
        ('Appearance or Signing', 'Appearance or Signing'),
        ('Attraction', 'Attraction'),
        ('Camp, Trip or Retreat', 'Camp, Trip or Retreat'),
        ('Concert or Performance', 'Concert or Performance'),
        ('Conference', 'Conference'),
        ('Course, Training or Workshop', 'Course, Training or Workshop'),
        ('Dinner or Gala', 'Dinner or Gala'),
        ('Festival or Fair', 'Festival or Fair'),
        ('Meeting or Networking Event', 'Meeting or Networking Event'),
        ('Party or Social Gathering', 'Party or Social Gathering'),
        ('Race or Endurance Event', 'Race or Endurance Event'),
        ('Tournament', 'Tournament'),
        ('Rally', 'Rally'),
        ('Seminar or Talk', 'Seminar or Talk'),
        ('Tour', 'Tour'),
        ('Tradeshow, Consumer Show..', 'Tradeshow, Consumer Show..'),
    )
    eventtopic = (
        ('Select a topic', 'Select a topic'),
        ('Auto, Boat & Air', 'Auto, Boat & Air'),
        ('Business & Professional', 'Business & Professional'),
        ('Charities & Causes', 'Charities & Causes'),
        ('Community & Culture', 'Community & Culture'),
        ('Family & Education', 'Family & Education'),
        ('Fashion & Beauty', 'Fashion & Beauty'),
        ('Film, Media & Entertainment', 'Film, Media & Entertainment'),
        ('Food & Drink', 'Food & Drink'),
        ('Government & Politics', 'Government & Politics'),
        ('Health & Wellness', 'Health & Wellness'),
        ('Hobbies & Special Interests', 'Hobbies & Special Interests'),
        ('Home & Lifestyle', 'Home & Lifestyle'),
        ('Music', 'Music'),
        ('Other', 'Other'),
        ('Performing & Visual Arts', 'Performing & Visual Arts'),
        ('Religion & Spirituality', 'Religion & Spirituality'),
        ('School Activities', 'School Activities'),
        ('Science & Technology', 'Science & Technology'),
        ('Seasonal', 'Seasonal'),
        ('Sports & Fitness', 'Sports & Fitness'),
        ('Travel & Outdoor', 'Travel & Outdoor'),
    )
    title = models.CharField(verbose_name='Event Title', max_length=200)
    location = models.CharField(verbose_name='Location', max_length=200)
    types = models.CharField(verbose_name='Event Type', choices=eventtype, default='01', null=True, max_length=50)
    topic = models.CharField(verbose_name='Event Topic', choices=eventtopic, default='01', null=True, max_length=50)
    image = models.ImageField(verbose_name='Event Image', upload_to='media')
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='Posted')
    description = RichTextField()
    starts = models.CharField(verbose_name='Event date & time, Starts', max_length=200, null=True)
    ends = models.CharField(verbose_name='Event date & time, Ends', max_length=200, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='User', max_length=40)
    organiser = models.CharField(verbose_name='Organiser Name', null=True, max_length=200)
    description2 = models.CharField(verbose_name='Organiser Description', null=True,  max_length=200)
    tickets = models.CharField(verbose_name='Tickets info', null=True, max_length=50)
    contact = models.IntegerField(null=True, verbose_name='Phone Number')
    email = models.EmailField(max_length=50, null=True, verbose_name='Email id')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event-post-detail', kwargs={'pk': self.pk})

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class recruiter(models.Model):
    industrys = (
        ('Accounting Jobs', 'Accounting Jobs'),
        ('Interior Design Jobs', 'Interior Design Jobs'),
        ('Bank Jobs Content', 'Bank Jobs Content'),
        ('Writing Jobs', 'Writing Jobs'),
        ('Consultant Jobs', 'Consultant Jobs'),
        ('Engineering Jobs', 'Engineering Jobs'),
        ('Export Import Jobs', 'Export Import Jobs'),
        ('Merchandiser Jobs', 'Merchandiser Jobs'),
        ('Security Jobs', 'Security Jobs'),
        ('HR Jobs', 'HR Jobs'),
        ('Hotel Jobs', 'Hotel Jobs'),
        ('Ecommerce Jobs', 'Ecommerce Jobs'),
        ('Mobile Jobs', 'Mobile Jobs'),
        ('Network administrator Jobs', 'Network administrator Jobs'),
        ('IT Jobs', 'IT Jobs'),
        ('BPO Jobs', 'BPO Jobs'),
        ('Legal Jobs', 'Legal Jobs'),
        ('Marketing Jobs', 'Marketing Jobs'),
        ('Packaging Jobs', 'Packaging Jobs'),
        ('Pharma Jobs', 'Pharma Jobs'),
        ('Maintenance Jobs', 'Maintenance Jobs'),
        ('Logistics Jobs', 'Logistics Jobs'),
        ('Sales Jobs', 'Sales Jobs'),
        ('Secretary Jobs', 'Secretary Jobs'),
        ('Film Jobs', 'Film Jobs'),
        ('Teacher Jobs', 'Teacher Jobs'),
        ('Graphic Designer Jobs', 'Graphic Designer Jobs'),
        ('Other', 'Other'),
    )
    experience = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('Fresher', 'Fresher'),
        ('Any', 'Any'),
    )
    name = models.CharField(verbose_name='Recruiter name', max_length=25)
    designation = models.CharField(verbose_name='Recruiters designation', null=True, max_length=25)
    starts = models.CharField(verbose_name='Interview Date',  null=True, max_length=25)
    ends = models.CharField(verbose_name='Interview Ends Date', null=True, max_length=25)
    company = models.CharField(verbose_name='Company Name', max_length=50)
    image = models.ImageField(verbose_name='Profile Pic', upload_to='media')
    industry = models.CharField(verbose_name='Type of Industry', choices=industrys, max_length=50)
    location = models.CharField(verbose_name='Job Location', max_length=100)
    job_title = models.CharField(verbose_name='Job Title', max_length=50)
    job_details = models.CharField(verbose_name='Job Description', null=True,  max_length=200)
    job_exp = models.CharField(verbose_name='Required experience in years', choices=experience, max_length=50)
    skill = models.CharField(verbose_name='Required Skills', null=True, max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='User', max_length=40)
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='Posted')
    contact = models.IntegerField(null=True, verbose_name='Phone Number')
    email = models.EmailField(max_length=50, null=True, verbose_name='Email id')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recruiter-post-detail', kwargs={'pk': self.pk})

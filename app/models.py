from django.db import models
from django.utils import timezone


# Create your models here.
class PersonalInfo(models.Model):
    full_name = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='profile_pic/')
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    linkedin = models.URLField()
    github = models.URLField()
    youtube = models.URLField(null=True, blank=True)
    medium = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=50)
    about_me = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)

    # Meta tags
    meta_title = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    meta_og_title = models.CharField(max_length=200, blank=True, null=True)
    meta_og_description = models.TextField(blank=True, null=True)
    meta_og_image = models.URLField(blank=True, null=True)
    meta_twitter_title = models.CharField(max_length=200, blank=True, null=True)
    meta_twitter_description = models.TextField(blank=True, null=True)
    meta_twitter_image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['-created']


class WorkExperience(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} at {self.company}"

    class Meta:
        ordering = ['-start_date']


class Education(models.Model):
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.degree} from {self.institution}"

    class Meta:
        ordering = ['-start_date']


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    order = models.IntegerField(default=1)
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']


class Skill(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='skills/', null=True, blank=True)
    order = models.IntegerField(default=1)
    created = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']


class Project(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default="Website")
    order = models.IntegerField(default=1)
    description = models.TextField()
    technologies_used = models.CharField(max_length=255)
    github_link = models.URLField(blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class Volunteering(models.Model):
    title = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} at {self.organization}"

    class Meta:
        ordering = ['-start_date']


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.first_name} {self.last_name} - {self.subject}"

    class Meta:
        ordering = ['-created']

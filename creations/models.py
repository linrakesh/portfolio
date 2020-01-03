from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class creation(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    creation_type = models.CharField(max_length=200)
    description = models.TextField()
    creation_image = models.ImageField(
        "creation image", upload_to='uploads')

    class Meta:
        verbose_name = "creation"
        verbose_name_plural = "creations"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("creation_detail", kwargs={"pk": self.pk})


class option(models.Model):
    sitename = models.CharField(max_length=100)
    punchline = models.CharField(max_length=150)
    site_email = models.EmailField(max_length=254)
    address = models.TextField()
    phoneNo = models.TextField(max_length=15)
    twitter = models.URLField()
    facebook = models.URLField()
    youtube = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()
    github = models.URLField()

    def __str__(self):
        return self.sitename

    def get_absolute_url(self):
        return reverse("option_detail", kwargs={"pk": self.pk})


class slider(models.Model):

    slider_name = models.CharField(max_length=100)
    slider_url = models.URLField()
    slider_image = models.ImageField('slider image', upload_to='sliders')

    def __ster__(self):
        return self.slider_name

    def get_absolute_url(self):
        return reverse("slider_detail", kwargs={"pk": self.pk})


class testimonial(models.Model):
    title = models.CharField(max_length=200)
    text=  models.TextField()
    image= models.ImageField(upload_to='testimonial')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('testimonial_detail', kwargs={"pk":self.pk})


class post(models.Model):

    STATUS_CHOICES = (('draft','Draft'),('published','Published'))

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE)  
    body    = models.TextField()
    publish = models.DateTimeField(default = timezone.now)   
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now= True)
    status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, default='draft')
    featured_image = models.ImageField(upload_to ='blogImages',default="")

    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"pk": self.pk})

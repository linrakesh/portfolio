from django.db import models
from django.urls import reverse

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

    def __str__(self):
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

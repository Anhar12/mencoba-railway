from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Logo(models.Model):
    primary_logo = models.ImageField(upload_to='logos/', blank=True, null=True, help_text="Upload primary logo")
    secondary_logo = models.ImageField(upload_to='logos/', blank=True, null=True, help_text="Upload secondary logo")

    def __str__(self):
        return "Logo Settings"
    
class ImageSlider(models.Model):
    image1 = models.ImageField(upload_to='image_slider/', blank=True, null=True, help_text="Upload slider image 1")
    image2 = models.ImageField(upload_to='image_slider/', blank=True, null=True, help_text="Upload slider image 2")
    image3 = models.ImageField(upload_to='image_slider/', blank=True, null=True, help_text="Upload slider image 3")
    image4 = models.ImageField(upload_to='image_slider/', blank=True, null=True, help_text="Upload slider image 4")
    image5 = models.ImageField(upload_to='image_slider/', blank=True, null=True, help_text="Upload slider image 5")

    def __str__(self):
        return f"Slider Image {self.id}"
    
class HeroSection(models.Model):
    hero_text = models.TextField(help_text="Hero section text", blank=True, null=True)
    hero_image = models.ImageField(upload_to='hero_section/', blank=True, null=True, help_text="Hero section image")

    def __str__(self):
        return "Hero Section Settings"
    
class ServiceSection(models.Model):
    service_title1 = models.CharField(max_length=100, blank=True, null=True, help_text="Service title")
    service_description1 = models.TextField(help_text="Service description", blank=True, null=True)
    service_image1 = models.ImageField(upload_to='services/', blank=True, null=True, help_text="Service image")
    
    service_title2 = models.CharField(max_length=100, blank=True, null=True, help_text="Service title")
    service_description2 = models.TextField(help_text="Service description", blank=True, null=True)
    service_image2 = models.ImageField(upload_to='services/', blank=True, null=True, help_text="Service image")
    
    service_title3 = models.CharField(max_length=100, blank=True, null=True, help_text="Service title")
    service_description3 = models.TextField(help_text="Service description", blank=True, null=True)
    service_image3 = models.ImageField(upload_to='services/', blank=True, null=True, help_text="Service image")

    def __str__(self):
        return f"{self.title1}, {self.title2}, {self.title3}"
    
class PhilosphySection(models.Model):
    philosophy_image = models.ImageField(upload_to='philosophy/', blank=True, null=True, help_text="Philosophy section image")
    philosophy_text = models.TextField(help_text="Philosphy section text", blank=True, null=True)
    
    def __str__(self):
        return "Philosophy Section Settings"
    
class VisionMissionSection(models.Model):
    vision_text = models.TextField(help_text="Vision section text", blank=True, null=True)
    mission_text = models.TextField(help_text="Mision section text", blank=True, null=True)
    
    def __str__(self):
        return "Vision & Mision Section Settings"
    
class BusinessStructure(models.Model):
    name_ceo = models.CharField(max_length=100, help_text="Name CEO", blank=True, null=True)
    image_ceo = models.ImageField(upload_to='business_structure/', blank=True, null=True, help_text="business structure image")
    
    name_coo = models.CharField(max_length=100, help_text="Name COO", blank=True, null=True)
    image_coo = models.ImageField(upload_to='business_structure/', blank=True, null=True, help_text="business structure image")
    
    name_cfo = models.CharField(max_length=100, help_text="Name CFO", blank=True, null=True)
    image_cfo = models.ImageField(upload_to='business_structure/', blank=True, null=True, help_text="business structure image")
    
    name_cto = models.CharField(max_length=100, help_text="Name CTO", blank=True, null=True)
    image_cto = models.ImageField(upload_to='business_structure/', blank=True, null=True, help_text="business structure image")
    
    name_cmo = models.CharField(max_length=100, help_text="Name CMO", blank=True, null=True)
    image_cmo = models.ImageField(upload_to='business_structure/', blank=True, null=True, help_text="business structure image")
    
    
    def __str__(self):
        return f"ceo: {self.name_ceo}, coo: {self.name_coo}, cfo: {self.name_cfo}, cto: {self.name_cto}, cmo: {self.name_cmo}"
    
class SolutionsSection(models.Model):
    solution_title1 = models.CharField(max_length=100, help_text="Solutions Title", blank=True, null=True)
    solution_description1 = models.TextField(help_text="Solutions Description", blank=True, null=True)
    
    solution_title2 = models.CharField(max_length=100, help_text="Solutions Title", blank=True, null=True)
    solution_description2 = models.TextField(help_text="Solutions Description", blank=True, null=True)
    
    solution_title3 = models.CharField(max_length=100, help_text="Solutions Title", blank=True, null=True)
    solution_description3 = models.TextField(help_text="Solutions Description", blank=True, null=True)
    
    def __str__(self):
        return "Solutions Section Settings"

class ContactSection(models.Model):
    phone_number = models.CharField(max_length=50, help_text="Phone Number", blank=True, null=True)
    email = models.EmailField(max_length=100, help_text="Email", blank=True, null=True)
    address = models.TextField(help_text="Address", blank=True, null=True)
    whatsapp = models.CharField(max_length=50, help_text="Whatsapp", blank=True, null=True)
    instagram = models.CharField(max_length=50, help_text="Instagram", blank=True, null=True)
    facebook = models.CharField(max_length=50, help_text="Facebook", blank=True, null=True)
    
    def __str__(self):
        return "Solutions Section Settings"
    
class LocationSection(models.Model):
    longitude = models.CharField(max_length=100, help_text="Longitude", blank=True, null=True)
    latitude = models.CharField(max_length=100, help_text="Latitude", blank=True, null=True)

    def __str__(self):
        return "Location Section Settings"


# ================= Blog Model =======================
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                self).get_queryset()\
                    .filter(status='published')

class Blogs(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    CATEGORIES = (
        ('Technology', 'Technology'),
        ('Sports', 'Sports'),
        ('Health', 'Health'),
        ('Science', 'Science'),
        ('Services', 'Services'),
        ('News', 'News'),
        ('Diseases', 'Diseases'),
        ('Events', 'Events'),
        ('Education', 'Education'),
        ('LifeStyle', 'LifeStyle'),
        ('Medicine', 'Medicine'),
    )
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='blogs/', help_text="Upload image")
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=CATEGORIES, default='health')
    objects = models.Manager()
    published = PublishedManager()
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    
    class Meta:
        ordering = ('-publish',)
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                        args=[self.publish.year,
                            self.publish.strftime('%m'),
                            self.publish.strftime('%d'),
                            self.slug])

class Activities(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='activities_posts', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    published = PublishedManager()
    image = models.ImageField(upload_to='activities/', help_text="Upload image")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    
    class Meta:
        ordering = ('-publish',)
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('activities:post_detail',
                        args=[self.publish.year,
                            self.publish.strftime('%m'),
                            self.publish.strftime('%d'),
                            self.slug])

    
class Comment(models.Model):
    post = models.ForeignKey(Blogs, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
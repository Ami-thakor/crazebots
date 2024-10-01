# Create your models here.
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    bot_url = models.URLField(max_length=255)
    source_url = models.URLField(max_length=255)
    thumb = models.URLField(max_length=600, blank=True, null=True)
    updated_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
    
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify

# Category model (Optional)
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# Tag model (Optional)
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# BlogPost model
class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')  
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    content = RichTextField()  # Blog content
    thumb = models.URLField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='blog_posts')  # Optional category
    tags = models.ManyToManyField(Tag, blank=True, related_name='blog_posts')  # Optional tags
    is_published = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Automatically generate the slug from the title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']  # Newest posts first

    
class TestiMonial(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    thumb = models.URLField(max_length=600, blank=True, null=True)

    def __str__(self):
        return self.title
    
class Servie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    thumb = models.URLField(max_length=600, blank=True, null=True)

    def __str__(self):
        return self.title
    
class Skill(models.Model):
    title = models.CharField(max_length=255)
    thumb = models.URLField(max_length=600, blank=True, null=True)

    def __str__(self):
        return self.title



class Plan(models.Model):
    name = models.CharField(max_length=100)  # Plan name (e.g., Basic, Premium)
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Price for the plan (e.g., 5.49)
    description = models.TextField(blank=True)  
    duration_days = models.IntegerField()  # Duration of the plan in days (e.g., 30 days)

    def __str__(self):
        return self.name

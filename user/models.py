from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    first_name = models.CharField(max_length=100, null = True, blank = True)
    last_name = models.CharField(max_length=150, null = True, blank = True)
    slug = models.SlugField(default='user-slug-field', editable=False)
    email = models.EmailField(editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    social_facebook = models.URLField(null = True, blank = True)
    social_whatsapp = models.URLField(null = True, blank = True)
    social_twitter = models.URLField(null = True, blank = True)
    social_instagram = models.URLField(null = True, blank = True)
    social_youtube = models.URLField(null = True, blank = True)
    social_linkedin = models.URLField(null = True, blank = True)
    social_website = models.URLField(null = True, blank = True)
    bio = models.TextField(null = True, blank = True, max_length=350)
    profile_picture = CloudinaryField('Profile Picture', blank = True, null = True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

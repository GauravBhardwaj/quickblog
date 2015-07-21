from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, default='',editable=False)
    content = models.TextField()
    published = models.BooleanField(default=True,editable=False)
    tags = models.CharField(max_length=200)
    upvotes = models.IntegerField(default=0,editable=False)
    #author = models.ForeignKey(Author, related_name="posts")

    class Meta:
        ordering = ['-upvotes']

    def __str__(self):
        return ' '.join([self.title])

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.id})

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    #website = models.URLField(blank=True)
    #picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return ' '.join([self.user.username])

class Author(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)

    def __str__(self):
        return "%s (%s)" % (self.name, self.email)

class Comment(models.Model):
    text = models.CharField(max_length=100)
    post = models.ForeignKey(Post)


class Admin:
       pass

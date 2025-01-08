from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(unique=True, max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.title}'

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Posts"

    def save(self, *args, **kwargs):
        # Start with the basic slug from the title
        base_slug = slugify(self.title)
        
        # If this is a new post (no ID yet) or the title changed
        if not self.id or not self.slug:
            # Check if the base slug exists
            counter = 1
            new_slug = base_slug
            # Keep checking until we find a unique slug
            while Posts.objects.filter(slug=new_slug).exists():
                new_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = new_slug
        super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.content[:10]}'
    class Meta:
        ordering = ['-created_at']

from django.db import models
from profiles.models import Profile
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images',
                            blank=True, null=True, default=None)

    def __str__(self):
        return str(self.body[:10])

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

    def get_total_likes(self):
        total_likes= self.like_set.all().count()
        return total_likes

    def get_all_likers(self):
        return [like.profile for like in self.like_set.all()]

    def get_all_comments(self):
        all_comments = self.comment_set.all()
        return all_comments
    class Meta:
        ordering = ('-created',)



class Like (models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)



class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.id)




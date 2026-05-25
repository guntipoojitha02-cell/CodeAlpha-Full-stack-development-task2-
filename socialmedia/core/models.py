from django.db import models
from django.contrib.auth.models import User


# User Profile
class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    bio = models.TextField()

    profile_image = models.URLField()

    def __str__(self):

        return self.user.username


# Posts
class Post(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    image = models.URLField()

    caption = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.user.username


# Comments
class Comment(models.Model):

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.user.username


# Likes
class Like(models.Model):

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):

        return self.user.username


# Follow System
class Follow(models.Model):

    follower = models.ForeignKey(
        User,
        related_name='following',
        on_delete=models.CASCADE
    )

    following = models.ForeignKey(
        User,
        related_name='followers',
        on_delete=models.CASCADE
    )

    def __str__(self):

        return self.follower.username
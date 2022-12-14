from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Save for later"), (1, "Published"))


"""Model for Recipe"""


class Recipe(models.Model):
    title = models.CharField(max_length=50, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True, null=False, blank=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipes")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    preparation_time = models.IntegerField(null=False, blank=False)
    cook_time = models.IntegerField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    ingredients = models.TextField(null=False, blank=False)
    image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=1)
    bookmarks = models.ManyToManyField(
        User, related_name='bookmark', default=None, blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    body = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.user}"

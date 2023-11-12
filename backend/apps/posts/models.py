from django.db import models
from core.models import BaseModel, BaseImage

class Post(BaseModel):
    title = models.CharField(max_length=256, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.title

class PostImage(BaseImage):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
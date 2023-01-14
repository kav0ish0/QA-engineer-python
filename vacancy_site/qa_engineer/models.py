from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=140)
    section1 = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title

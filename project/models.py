from django.db import models

# Create your models here.

class projectFormat(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    tech_stack = models.TextField()
    programmer = models.CharField()
    image = models.ImageField(default="default_image.jpg")
    date = models.DateTimeField(auto_now_add=True)
    project_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

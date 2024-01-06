from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
from PIL import Image

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name

class Quote(models.Model):
    quote = RichTextField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    img = models.ImageField(null=True, blank=True, upload_to="images/")
    synopsis = RichTextField(max_length=1000, default="")
    date_created = models.DateField(default=datetime.now)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.img:
            img_path = self.img.path
            desired_width = 300  # Change this to your desired width
            desired_height = 200  # Change this to your desired height

            with Image.open(img_path) as img:
                img.thumbnail((desired_width, desired_height))
                img.save(img_path)

    def __str__(self):
        return self.quote
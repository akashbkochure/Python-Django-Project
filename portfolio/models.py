from django.db import models
import os

# Create your models here.

class Job(models.Model):
    company = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='images/')

    def delete(self, *args, **kwargs):
        # Delete the image file when the job is deleted
        if self.image:
            try:
                # Get the image path
                image_path = os.path.join(settings.MEDIA_ROOT, str(self.image))
                # Delete the image file
                os.remove(image_path)
            except Exception as e:
                # Handle any errors that may occur during image deletion
                print(f"Error deleting image: {e}")

        # Call the superclass delete method to delete the job from the database
        super(Job, self).delete(*args, **kwargs)

from django.db import models

class Job(models.Model):
    company = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='job_images/', blank=True, null=True)

    def delete(self, *args, **kwargs):
        # Delete the image file when the job is deleted
        if self.image:
            self.image.delete()
        super(Job, self).delete(*args, **kwargs)
    

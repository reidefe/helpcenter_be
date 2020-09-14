from django.db import models
from django.conf import settings
from django.db.models.signals import post_save


class Guides(models.Model):    
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    images = models.ImageField(null = True, blank = True, upload_to= '/images')
    content = models.TextField(blank=False, null=False)
    published = models.DateField(auto_now=False, auto_now_add=False)
    likes = models.FloatField()


    class Meta:
        
        ordering = ('published')
        get_latest = 'rating'

    

    def __str__(self):
        return '%d: %s' % (self.published, self.title)

    """def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Guides, self).save(*args, **kwargs) """




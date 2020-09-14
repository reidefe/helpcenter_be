from django.db import models
from django.conf import settings
from django.db.models.signals import post_save



class Ideas(models.Model):    
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    images = models.ImageField(null = True, blank = True, upload_to= '/images')
    content = models.TextField(blank=False, null=False)
    published = models.DateField(auto_now=False, auto_now_add=False)
    rating = models.PositiveIntegerField()


    class Meta:
        
        ordering = ('published')
        get_latest = 'rating'

    
    def __str__(self):
        return '%d: %s' % (self.published, self.title)
    
class Comment(models.Model):
    post = models.ForeignKey(Ideas, related_name='comments', on_delete=models.CASCADE)
    
    body = models.TextField(null=False, blank=False)
    likes = models.PositiveIntegerField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='replies', on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        #sort comments based on reverse chronological order by default
        ordering = ('-timestamp')

    def __str__(self):
        return self.body

    #children
    def children(self):
        return Comment.objects.filter(parent=self)

    



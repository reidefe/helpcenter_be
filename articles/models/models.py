from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

class Visitors(models.Model):
    name = models.CharField()
    email = models.EmailField() 
    password = models.CharField()  

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)




class Article(models.Model):    
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    tag_name = models.SlugField(unique=True)
    image = models.ImageField(null = True, blank = True, upload_to= '/images')
    content = models.TextField(blank=True, null=True)
    published = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    rating = models.PositiveIntegerField()



    class Meta:
         #sort article based on chronological order by default
        ordering = ('created_at')

    def get_absolute_url(self):
        return reversed('Article:details', kwargs={'slug': self.slug})


    def __str__(self):
        return '%d: %s' % (self.published, self.title)
    
class Comment(models.Model):
    post = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    name = models.ForeignKey(Visitors,related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    likes = models.PositiveIntegerField
    parent = models.ForeignKey('self', blank=True, null=True, related_name='replies', on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        #sort comments based on chronological order by default
        ordering = ('-timestamp')

    def __str__(self):
        return self.body

    #children
    def children(self):
        return Comment.objects.filter(parent=self)

    



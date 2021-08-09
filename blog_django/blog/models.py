from django.db import models
from taggit.managers import TaggableManager
from django.contrib.humanize.templatetags.humanize import naturaltime

class TimeStampedModel(models.Model):

    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now= True)

    class Meta:
        abstract = True

class Post(TimeStampedModel):
    image = models.CharField(max_length=200)
    title = models.CharField(max_length=140)
    content = models.TextField()
    tags = TaggableManager()

    @property
    def like_counts(self):
        return self.likes.all().count()

    @property
    def comment_counts(self):
        return self.comments.all().count()
    
    @property
    def natural_time(self):
        return naturaltime(self.created_at)
    
    # class Meta:
    #     ordering = ['-created_at']

class Comment(TimeStampedModel):
   name = models.CharField(max_length=140) 
   message = models.TextField()
   blog = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='comments')




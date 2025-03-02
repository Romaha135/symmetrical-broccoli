from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Title', max_length=50, default='Untitled')
    intro = models.CharField('Introduction', max_length=250, default='No introduction')
    full_text = models.TextField('Article', default='No content')  # Add a default value
    date = models.DateTimeField('Date')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/news/{self.id}'
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles' 


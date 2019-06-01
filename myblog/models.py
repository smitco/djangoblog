from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
        
class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=True, related_name='categories')
    
    class Meta:
        verbose_name_plural = 'Categories' 

    def __str__(self):
        return self.name
          
class HashtagInline(admin.TabularInline):
    model = Category.posts.through
    extra = 1
     
class PostAdmin(admin.ModelAdmin):
    inlines = [
        HashtagInline,
    ] 
    
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


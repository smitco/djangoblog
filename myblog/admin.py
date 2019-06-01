from django.contrib import admin
from myblog.models import Post, PostAdmin
from myblog.models import Category, CategoryAdmin
        
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

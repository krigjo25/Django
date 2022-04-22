from django.contrib import admin

from krigjo25.models import BlogCategory, Post

# Register your models here.
class PostAdmin (admin.ModelAdmin):
    pass

class CategoryAdmin (admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(BlogCategory, CategoryAdmin)
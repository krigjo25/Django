from django.contrib import admin

from krigjo25.models import BlogCategory, BlogPost

# Register your models here.
class PostAdmin (admin.ModelAdmin):
    pass

class CategoryAdmin (admin.ModelAdmin):
    pass

admin.site.register(BlogPost, PostAdmin)
admin.site.register(BlogCategory, CategoryAdmin)
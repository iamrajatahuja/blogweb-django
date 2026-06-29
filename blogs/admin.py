from django.contrib import admin

from .models import Post, Author, Tag

#To tweak and display the admin Posts page and prepopulate the slug field while adding post, use the same variable names-list_display,list_filter
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    list_filter = ('author', 'tags', 'date')
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)

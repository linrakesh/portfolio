from django.contrib import admin
from .models import creation, slider, option, testimonial,post
# Register your models here.

admin.site.register(creation)
admin.site.register(slider)
admin.site.register(option)
admin.site.register(testimonial)
""" admin.site.register(post) """


# change admin view of each models
@admin.register(post)
class postAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'status', 'featured_image')
    list_filter = ('title','author')
    raw_id_fields = ('author',)
    search_fields = ('title','body')
    prepopulated_fields = {'slug':('title',)}
    ordering = ('status','publish')

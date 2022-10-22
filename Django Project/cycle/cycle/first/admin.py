from django.contrib import admin
from .models import cycle_post, Profile


# Register your models here.

@admin.register(cycle_post)
class cycle_postAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'price', 'created_at', 'city')
    fields = ('user', ('title', 'price'), 'discription', 'image', ('city', 'location'))
    list_filter = ('user', 'title', 'price', 'created_at', 'city')
    search_fields = ('user', 'title', 'price', 'created_at', 'city')

    


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'thumbnail', 'bio', 'location', 'birth_date')
    fields = ('user', ('profile_img', 'bio'), ('location', 'birth_date'))





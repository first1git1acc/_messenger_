from django.contrib import admin
from myapp.models import userPage,Post
# Register your models here.
@admin.register(userPage)
class PageAdmin(admin.ModelAdmin):
    list_display = ['user','time','status']
    raw_id_fields = ['user']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user','add_time','slug']
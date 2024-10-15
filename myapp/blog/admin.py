from django.contrib import admin
from .models import Post,Category,AboutUs, ContactForm

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content','category')
    search_fields = ('title','content')
    list_filter = ('category','created_at')
# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(AboutUs)
admin.site.register(ContactForm)
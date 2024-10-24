from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(usermodel)
admin.site.register(Book)
admin.site.register(Employee)
admin.site.register(Product)
class cusadmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','phone_number')
    search_fields=('first_name',)
    list_filter=('email',)
admin.site.register(Customer,cusadmin)
admin.site.site_header='MY_SITE'
admin.site.site_title='Django site'
class blogpost(admin.ModelAdmin):
    list_display=('title','author','created_at','updated_at')
    search_fields=('title',)
    list_filter=('author',)
admin.site.register(Post,blogpost)
admin.site.register(user_product)
admin.site.register(product_for_user)
admin.site.register(Publisher)
class bookk(admin.ModelAdmin):
    list_display=('title','isbn','publisher')
    search_fields=('title',)
    list_filter=('publication_date',)
admin.site.register(Book_publisher,bookk)

admin.site.register(Course)
admin.site.register(Student)

admin.site.register(Organizer)
admin.site.register(Event)
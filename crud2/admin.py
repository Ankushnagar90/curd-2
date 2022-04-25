from django.contrib import admin


from .models import Person

admin.site.register(Person)
class personAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','password')
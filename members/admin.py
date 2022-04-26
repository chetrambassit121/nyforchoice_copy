from django.contrib import admin
from .models import UserProfile, User, State, City
# , College, Branch
# from django.contrib.auth.models import User
# Register your models here.

# admin.site.register(User)
admin.site.register(UserProfile)    
admin.site.register(State)    
admin.site.register(City)    
# admin.site.register(College)    
# admin.site.register(Branch)   


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('username', 'first_name', 'last_name', 'state', 'city')
    list_filter = ('username', 'first_name', 'last_name', 'state', 'city')
    search_fields = ('username', 'first_name', 'last_name', 'state', 'city')
admin.site.register(User, UserAdmin) 




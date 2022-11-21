from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Author, Post

fields = list(UserAdmin.fieldsets)
fields[1] = ('Personal Info', {'fields': ('name', 'account_twitter', 'description', 'street',
                                          'number', 'door', 'postal_code', 'city')})

# fields[1] = ('Personal Info', {'fields': ('age',)})
UserAdmin.fieldsets = tuple(fields)

admin.site.register(Author, UserAdmin)
admin.site.register(Post)

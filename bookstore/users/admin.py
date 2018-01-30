from django.contrib import admin
from users.models import Address

# Register your models here.
# admin.site.register(Address)
@admin.register(Address)
class registerAadmin(admin.ModelAdmin):
	pass
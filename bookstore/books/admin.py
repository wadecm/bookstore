from django.contrib import admin
from books.models import Books

# Register your models here.
# 在admin中添加有关商品的编辑功能。
@admin.register(Books)
class registerAadmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'type_id', 'price')

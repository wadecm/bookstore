from django.db import models
from tinymce.models import HTMLField
from db.base_model import BaseModel
from books.enums import *


# Create your models here.
class BooksManager(models.Manager):
	'''商品模型管理器类'''
	# sort='new' 按照创建时间进行排序
	# sort='hot' 按照商品销量进行排序
	# sort='price' 按照商品的价格进行排序
	# sort= 按照默认顺序排序
	def get_books_by_type(self,type_id, limit=None, sort='default'):
		if sort == 'new':
			order_by = ('-create_time',)
		elif sort == 'hot':
			order_by = ('-sales',)
		elif sort == 'price':
			order_by = ('price',)
		else:
			order_by = ('-pk',)
		#查询数据
		book_li = self.filter(type_id=type_id).order_by(*order_by)

		#查询结果集的限制
		if limit:
			book_li = book_li[:limit]
		return book_li

	def get_books_by_id(self,books_id):
		try:
			books = self.get(id=books_id)
		except Exception as e:
			print('e: ', e)
			books = None
		return books

class Books(BaseModel):
	'''商品模型类'''
	books_type_choices = ((k,v) for k,v in BOOKS_TYPE.items())
	status_choices = ((k,v) for k,v in STATUS_CHOICE.items())
	type_id = models.SmallIntegerField(default='PYTHON', choices=books_type_choices, verbose_name='商品种类')
	name = models.CharField(max_length=30, verbose_name='商品名称')
	desc = models.CharField(max_length=128, verbose_name='商品简介')
	price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')
	unite = models.CharField(max_length=20, verbose_name='商品单位')
	stock = models.IntegerField(default=1, verbose_name='商品库存')
	sales = models.IntegerField(default=0, verbose_name='商品销量')
	details = HTMLField(verbose_name='商品详情')
	image = models.ImageField(upload_to='books', verbose_name='商品图片')
	status = models.SmallIntegerField(default=ONLINE, choices=status_choices, verbose_name='商品状态')

	objects = BooksManager()


	class Meta:
		verbose_name = '商品名称'
		verbose_name_plural = verbose_name
		db_table = 's_books'

	def __str__(self):
		return self.name


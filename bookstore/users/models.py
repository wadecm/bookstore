#coding:utf-8
from django.db import models
from hashlib import sha1
from db.base_model import BaseModel

# Create your models here.

def get_hash(str):
	sh = sha1()
	sh.update(str.encode('utf8'))
	return sh.hexdigest()

class PassportManager(models.Manager):
	def add_one_passport(self,username,password,email):
		'''添加一个账户信息'''
		passport = self.create(username = username, password=get_hash(password), email=email)
		return passport

	def get_one_passport(self,username,password):
		'''根据用户密码查找账户信息'''
		try:
			passport = self.get(username=username,password=get_hash(password))
		except self.model.DoesNotExist:
			passport = None
		return passport

	def check_passport(self,username):
		'''检查是否存在用户名'''
		try:
			passport = self.get(username=username)
		except self.model.DoesNotExist:
			passport = None
		return passport


class Passport(BaseModel):
	username = models.CharField(max_length=20, verbose_name='用户名称')
	password = models.CharField(max_length=40, verbose_name='用户密码')
	email = models.EmailField(verbose_name='用户邮箱')
	is_active = models.BooleanField(default=False, verbose_name='激活状态')

	#用户表的管理器
	objects = PassportManager()

	class Meta:
		verbose_name = '用户'
		verbose_name_plural = verbose_name
		db_table = 's_user_account'

	def __str__(self):
		return self.username



#地址模型管理器
class AddressManager(models.Manager):
	#查询指定用户的默认地址
	def get_default_address(self, passport_id):
		print('passport_id: ', passport_id)
		try:
			addr = self.get(passport_id= passport_id, is_default=True)
		except Exception as e:
			print('e: ', e)
		# except self.model.DoesNotExist:
		# 	addr = None
		return addr


	def get_one_address(self, passport_id, recipient_name, recipient_address, zip_code, recipient_phone ):
		'''判断是否有默认地址'''
		addr = self.get_default_address(passport_id=passport_id)

		if addr:
			is_default = False
		else:
			is_default = True

		addr = self.create(
			passport_id=passport_id,
			recipient_name=recipient_name,
			recipient_address=recipient_address,
			zip_code=zip_code,
			recipient_phone=recipient_phone)
		return  addr

#地址模型类
class Address(BaseModel):
	recipient_name = models.CharField(max_length=20, verbose_name='收件人')
	recipient_addr = models.CharField(max_length=222, verbose_name='收件地址')
	zip_code = models.CharField(max_length=6,verbose_name='邮政编码')
	recipient_phone = models.CharField(max_length=11, verbose_name='练习电话')
	is_default = models.BooleanField(default=False, verbose_name='是否默认')
	passport = models.ForeignKey('Passport', verbose_name='账户')

	objects = AddressManager()

	class Meta:
		verbose_name = '地址'
		verbose_name_plural = verbose_name
		db_table = 's_user_table'

	def __str__(self):
		return self.recipient_name

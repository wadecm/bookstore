from django import http
#中间件示例，打印中间件执行语句
class BookMiddleware(object):
	def process_request(self,request):
		print('Middleware Excuted')

#分别处理收到的请求和发出去的响应，理解中间件的原理
class Another_Middleware(object):
	def process_request(self,request):
		print('Another Middleware Excuted')
	def process_response(self,request,response):
		print('Another Middleware process_response Excuted')
		return response

#记录用户访问的url地址
class UrlPathRecordMiddleware(object):
	EXCLUDE_URL = ['/user/login/','/user/login/','/user/register/']
	# 1./user/ 记录 url_path = /user/
	# 2./user/login/ url_path = /user/
	# 3./user/login_check/  url_path = /user/
	def process_view(self,request,view_func,*view_args,**view_kwargs):
		#当用户的请求地址不在排除的列表中，同时也不是ajax的get请求
		if request.path not in UrlPathRecordMiddleware.EXCLUDE_URL and not request.is_ajax() and request.method == 'GET':
			request.session['url_path'] = request.path

BLOCKED_IPS = []
#拦截在BLOCKED_IPS中的IP
class BlockedIpMiddleware(object):
	def process_request(self,request):
		if request.Meta['REMOTE_ADDR'] in BLOCKED_IPS:
			return http.HttpResponseForbidden('<h1>Forbidden</h1>')



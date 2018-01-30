from haystack import indexes
from books.models import Books

class BookIndex(indexes.SearchIndex,indexes.Indexable):
	# 指定根据表中的哪些字段建立索引:比如:商品名字 商品描述
	text = indexes.CharField(document=True, use_template=True)

	def get_model(self):
		return Books

	def index_queryset(self, using=None):
		return self.get_model().objects.all()


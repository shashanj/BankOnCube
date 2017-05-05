from FrameWork.QueryHelper.DynamicQueries.models import Query


def dynaminImport(clazz):
	components = clazz.split('.')
	mod = __import__(components[0])
	for comp in components[1:]:
		mod = getattr(mod, comp)
	return mod

def execute(query,data):
	qury = Query.objects.get(id = query)
	
	args = qury.args.split(',')
	val  = []
	for arg in args :
		val.append(data.get(str(arg)))

	filters = qury.filters.split(',')
	kwargs = {}

	i = 0 
	for filter in filters:
		kwargs[filter] = val[i]
		i=i+1

	clazz = dynaminImport(qury.modelName)
	return clazz.objects.filter(** kwargs)
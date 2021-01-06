import json

class JSONConnector:
	def __init__(self, filepath):
		self.data = dict()
		with open(filepath, mode='r', encoding='utf-8') as f:
			self.data = json.load(f)
	@property
	def parsed_data(self):
		return self.data

class XMLConnector:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)
    @property
    def parsed_data(self):
        return self.tree

#obj = JSONConnector('D:\\json1.json')
#r = obj.parsed_data
#print(type(JSONConnector))
#print(type(obj))
#print(r)
#fn = 'D:\\json1.json'
#print(fn.endswith('json'))

def connector_factory(filepath):
	if filepath.endswith('json'):
		connector = JSONConnector
	elif filepath.endswith('xml'):
		connector = XMLConnector
	else:
		raise ValueError('Cannot connect to {}'.format(filepath))
	return connector(filepath)

#filepath = 'D:\\json1.json'
#r1 = connector_factory(filepath)
#print(r1.parsed_data)

def connect_to(filepath):
	factory = None
	try:
		factory = connector_factory(filepath)
	except ValueError as ve:
		print(ve)
	return factory


json_data_obj = connect_to('D:\\json1.json')
json_data = json_data_obj.parsed_data
print('found: {} donuts'.format(len(json_data)))
for donut in json_data:
	print('name: {}'.format(donut['name']))
	print('price: ${}'.format(donut['ppu']))
	[print('topping: {} {}'.format(t['id'], t['type'])) for t in donut['topping']]#这是一个奇妙的打印方式

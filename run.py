from DataExplorationEngine import add, eda, vis,Get


DATABASE_NAME =  'IRIS'
collname = 'irisdata'
# load data 
# datatypes = {
# 	'floats' : ['SepalLength','SepalWidth','PetalLength','PetalWidth']
# }
# add.load_csv("iris.csv", "irisdata", datatypes)

key='Species'
key1="SepalLength"
key2="SepalWidth"

# Performing EDA
docs = eda.cursor_to_list(Get().get_documents(collname))
if len(docs) <= 0:
	print collname + ' collection has no documents'
	exit()

 
doc = docs[0]

# Identify variable type
print 'Identifying Variables :'
for key, value in doc.iteritems():
	if key != '_id':
		print key, eda.identify_variable_type(key, collname)

print '\n'

# univariate analysis
print 'Univariate Analysis :'
for key, value in doc.iteritems():
	
	if key != '_id' and eda.identify_variable_type(key, collname) == 'Continuous':
		uni = eda.univariate_analysis(key, collname)[0]
		print 'Continuous Group =', uni['_id']
		print 'Max =', uni['max'], 'Min =', uni['min'], 'Sum =', uni['sum'], 'Mean =', uni['mean']

	elif key != '_id' and eda.identify_variable_type(key, collname) == 'Categorical':
		uni_list = eda.univariate_analysis(key, collname, central_tendencies = False)
		for uni in uni_list:
			print 'Categorical Group =', key
			print 'Sample =', uni['_id'], 'Frequency =', uni['freq']

print '\n'

# Bivariate analysis
print 'Bivariate Analysis :'
bi = eda.bivariate_analysis(key2, key1, collname)


print '\n'

# Detecting Missing values
print 'Deleted missing values :',eda.delete_missing_values(collname)

print '\n'

# Outliers detection
for key, value in doc.iteritems():
	if key != '_id' and eda.identify_variable_type(key, collname) == 'Continuous':
		print 'Outlier exist for', key, '?:', eda.get_outliers(key, collname)

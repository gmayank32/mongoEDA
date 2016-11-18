from DataExplorationEngine import add, eda, vis


# load data 
# datatypes = {
# 	'floats' : ['SepalLength','SepalWidth','PetalLength','PetalWidth']
# }
# add.load_csv("iris.csv", "irisdata", datatypes)

# perform EDA 
key = "Species" #key can be any variable
# print eda.identify_variable_type('SepalLength','irisdata')
# print eda.identify_variable_type('SepalWidth','irisdata')
# print eda.identify_variable_type('PetalLength','irisdata')
# print eda.identify_variable_type('PetalWidth','irisdata')
# print eda.identify_variable_type('Species','irisdata')
# uni = eda.univariate_analysis(key,"irisdata", central_tendencies = False)
# vis.create_univariate_table(uni, key)

collname = "irisdata"
key1 = "SepalLength"
key2 = "SepalWidth"
# bi = eda.bivariate_analysis(key1, key2, collname)
# print 'std_dev',eda.get_std_dev(key1,collname)
# print 'outlier detection',eda.get_outliers(key1,collname)
# vis.createBiTable(bi, key1, key2)
eda.delete_missing_values('irisdata')
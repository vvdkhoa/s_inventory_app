import pandas as pd
import psycopg2
import datetime
import numpy as np

class Inventory():

	def __init__(self):
		self.conn = self.set_conn()
		self.inventory_df = self.get_df(table_name='inventory')

	# Setting database
	def set_conn(self):
		#++++ Google Cloud Setting +++++#
		db_setting = {
			'host': '',
			'port': '',
			'database': 'postgres',
			'user': '',
			'password': '' }
		#++++ Google Cloud Setting +++++#

		conn = None
		conn = psycopg2.connect(
					host=db_setting['host'], 
					port=db_setting['port'], 
					database=db_setting['database'],
					user=db_setting['user'], 
					password=db_setting['password'] )
		conn.get_backend_pid()
		return conn

	# Get Dataframe from database table, # https://chusotsu-program.com/pandas-psycopg2
	def get_df(self, table_name):
		sql = 'SELECT * FROM %s;' % table_name
		return pd.read_sql(sql, self.conn)

	# Run sql command
	def sql_command(self, command):
		run_result = {}
		try:
			cur = self.conn.cursor()
			cur.execute(command)
			cur.close()
			run_result['rowcount'] = cur.rowcount # For check update result, = 0 => error
			self.conn.commit()
		except (Exception, psycopg2.DatabaseError) as error:
			run_result['error'] = error
		return run_result

	# Search all result
	# Input: search_dict = {'asin': 'AA', 'product_name': 'BB'....}
	# Return: Result Dataframe
	def search_inventory_all(self, search_dict):
		res_df = pd.DataFrame()
		for key in search_dict:
			add_df = self.inventory_df.loc[self.inventory_df[key] == search_dict[key]]
			res_df = res_df.append(add_df)
		return res_df

	# 絞り込み検索
	# search_dict = {'asin': 'AA', 'product_name': 'BB'....}
	# product_name or product_name_en => Contains, other key => matching all
	# return result dataframe
	def search_inventory(self, search_dict):
		bool_series = []
		for key in search_dict:
			if search_dict[key] != '':
				if key == 'product_name':
					if search_dict['product_name'] == '*':
						return self.inventory_df
					else:
						bool_product_name = self.inventory_df['product_name'].str.contains(search_dict['product_name']).to_list()
						bool_series.append(bool_product_name)
				elif key == 'product_name_en':
					bool_product_name_en = self.inventory_df['product_name_en'].str.contains(search_dict['product_name_en']).to_list()
					bool_series.append(product_name_en)
				else:
					add_bool = self.inventory_df[key] == search_dict[key]
					bool_series.append(add_bool)
		if bool_series != []:
			bool_ = self.multiplyList(bool_series)
			return self.inventory_df[bool_]
		else:
			return pd.DataFrame() # Return bland Dataframe

	# Multiply all bool series in the list
	def multiplyList(self, myList):
		if len(myList) < 2:
			return myList[0]
		else:
			if len(myList) < 3:
				range_ = range(1,2)
			else:
				range_ = range(1, len(myList))
			result = myList[0]
			for i in range_:
				result = result & myList[i]
			return result

	# Update inventory
	# update_dict = {'asin': 'XXXXXXXXX8', 'product_name': 'Kindle'}
	def update_inventory(self, update_dict, primary_key='asin'):

		# Change dict to update SQL
		key = update_dict.pop(primary_key)
		all_key = ', '.join(update_dict.keys())
		all_values = ''
		for s in update_dict.values():
			if type(s) == str:
				all_values += "'" + s + "', "
			else:
				all_values += str(s) + ", "
		all_values = all_values[:-2] # Remove ", " in the end
		command = """UPDATE inventory SET({}) = ({}) WHERE {}= '{}';
				""".format(all_key, all_values, primary_key, key)
		# Update record
		update_res = self.sql_command(command)
		# Check update result
		if 'error' in update_res:
			print(update_res)
			return 'Update Error'
		else:
			if update_res['rowcount'] < 1:
				print(update_res)
				print(command)
				return 'Update Error'
			else:
				return None

	# Insert new data to inventor table
	def insert_inventory(self, insert_dict):
		# Change dict to update SQL
		all_key = ', '.join(insert_dict.keys())
		for key in insert_dict.keys():
			if type(insert_dict[key]) == str:
				insert_dict[key] = "'" + insert_dict[key] + "'"
			else:
				insert_dict[key] = str(insert_dict[key])

		all_values = ', '.join(insert_dict.values())
		command = "INSERT INTO inventory ({}) VALUES ({});".format(all_key, all_values)

		insert_res = self.sql_command(command)
		# Check insert result
		if 'error' in insert_res:
			print(command)
			print(insert_res)
			return insert_res

	# Import: +, export: -
	def import_export_inventoty(self, jan, import_export_quantity):
		search_dict = {'jan': jan}
		search_res = self.search_inventory(search_dict)
		if search_res.shape[0] == 0:
			return 'No item'
		elif search_res.shape[0] > 1:
			return search_res
		else:
			asin = search_res.reset_index(drop=True).loc[0]['asin']
			quantity = search_res.reset_index(drop=True).loc[0]['quantity']
			new_quantity = quantity + import_export_quantity
			command = """UPDATE inventory SET quantity = {} WHERE asin = '{}';
				""".format(new_quantity, asin)
			update_res = self.sql_command(command)
			# Check update result
			if update_res['rowcount'] < 1 or 'error' in update_res:
				print(update_res)
				return 'Update Error'
			else:
				print('Update success, new quantity = {}'.format(new_quantity))

	# Delete record:
	def delete_inventoty(self, asin):

		command = "DELETE FROM inventory WHERE asin = '{}';".format(asin)
		delete_res = self.sql_command(command)
		# Check result
		if delete_res['rowcount'] < 1 or 'error' in delete_res:
			print(delete_res)
			return {'error': 'Delete Error'}
		else:
			return None
			# print('Delete success, asin = {}'.format(asin))
			
######################################################################################
def print_(str_list):
	print('\n+++++++++++++++++++++++++++++++++++++')
	for s in str_list:
		print(str(s))
	print('+++++++++++++++++++++++++++++++++++++')

######################################################################################
# file_path: ..../*.html
def save_df_to_html(df, file_path):
	df = df.replace(np.nan, '', regex=True)
	with open(file_path, 'w') as f:
		f.write(df.to_html())

######################################################################################
# # file_path: ..../*.html
# def save_df_to_csv(df, file_path):
# 	df = df.replace(np.nan, '', regex=True)
# 	with open(file_path, 'w') as f:
# 		f.write(df.to_csv())


######################################################################################
if __name__ == '__main__':
	print('')

	# Inventory = Inventory()
	# search_dict = {'asin': 'BBBBBBBB4', 'jan': '1234567890', 'mpn': 'MPN100', 'product_name': 'Product 4', 'product_name_en': ''}
	# search_dict = {'product_name': 'Case', 'jan': '1234567890'}
	# search_dict = {'asin': 'BBBBBBBB7'}
	# search_dict = {'mpn': 'MPN100'}

	# search_res = Inventory.search_inventory_use_title(search_dict={'product_name': 'Product', 'product_name_en': ''})
	# search_res = Inventory.search_inventory(search_dict={'product_name': 'Product', 'product_name_en': '', 'asin': 'BBBBBBBB0'})
	# print(search_res.shape[0])
	# print(search_res)

	# for i in range(search_res.shape[0]):
	# 	print(search_res.reset_index(drop=True).loc[i].to_dict())

	# update_dict = {'asin': 'BBBBBBBB7', 'product_name': 'Kindle Paperwhite', 'jan': '12345', 'quantity': 15, 'note': '重い'}
	# Inventory = Inventory()
	# Inventory.update_inventory(update_dict=update_dict)

	# insert_dict = {'asin': 'AAAAAAAAE', 'product_name': 'Sagami 0.02', 'jan': '111111111', 'quantity': 0}
	# Inventory = Inventory()
	# Inventory.insert_inventory(insert_dict=insert_dict)

	# Inventory = Inventory()
	# Inventory.import_export_inventoty('111111111', -2)

	# Inventory = Inventory()
	# Inventory.delete_inventoty('XXXXXXXXX8')

	# print(Inventory.get_df(table_name='inventory'))

	# conn = set_conn()
	# inventory_df = get_df(conn=conn, table_name='inventory')
	# # print(inventory_df)

	# update_dict = {'asin': 'bbbbbb8', 'product_name': 'Case', 'jan': '1234567890', 'quantity': 10}
	# update_inventory(conn, update_dict)


	# conn = set_conn()
	# for i in range(6,8):
	# 	command = "INSERT INTO inventory(asin, product_name, quantity, mpn) VALUES ('{}', '{}', {}, '{}');".format('BBBBBBBB' + str(i), 'Product ' + str(i), i, 'MPN'+ '100')
	# 	# command = "DELETE FROM inventory"
	# 	e = sql_command(conn, command)
	# 	if e:
	# 		print(e)
	# 		conn = set_conn()

	# search_dict = {'asin': 'BBBBBBBB4', 'jan': '123456', 'mpn': 'MPN100', 'product_name': 'Product 4', 'product_name_en': ''}
	# search_dict = {'asin': 'bbbbbb8', 'product_name': 'Case', 'jan': '123456'}
	# search_dict = {'jan': '123456'}
	# res_df = search_inventory(inventory_df=inventory_df, search_dict=search_dict)
	# save_df_to_html(df=res_df, file_path='df.html')
	# print(res_df)

	# command = "INSERT INTO Inventory(asin, product_name, jan) VALUES ('bbbbbb8', 'Case', '123456')"
	# sql_command(conn, command)

# Get all table name
	# sql = '''
	# 		SELECT table_name
	# 		FROM information_schema.tables
	# 		WHERE table_schema='public'
	# 		AND table_type='BASE TABLE';
	# 		'''

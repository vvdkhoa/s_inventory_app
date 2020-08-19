from PySide2 import QtWidgets, QtCore
from PySide2.QtGui import QPixmap, QIcon
from ui import ui_main

from inventory_sql import Inventory
from amazon_scrapt import AmazonScrapt
import re
from bs4 import BeautifulSoup as bs
import webbrowser
import os
import subprocess
import json
import numpy as np
from datetime import datetime

####################  Get Setting ###########################
with open('Setting_InventoryManager.json', 'r', encoding='utf-8') as f:
	Data_dict = json.load(f)[0]
	ProductImages_path = Data_dict['ProductImages_path']
	GoogleChrome_path = Data_dict['GoogleChrome_path']

####################  UI CLASS ############################## 
class MyQtApp(ui_main.Ui_MainWindow, QtWidgets.QMainWindow, Inventory, AmazonScrapt):

	def __init__(self):
		super(MyQtApp, self).__init__()
		self.setupUi(self)
		# self.setIcon(QIcon("/images/stocks.png"))
		self.setWindowIcon(QIcon("ui/images/stocks.png"))
		self.setWindowTitle("Inventory Manager") # Windowns name
		self.searchButton.clicked.connect(self.search)
		self.clearButton.clicked.connect(self.clear)
		self.updateButton.clicked.connect(self.update)
		self.insertButton.clicked.connect(self.insert)
		self.importButton.clicked.connect(self.import_quantity)
		self.exportButton.clicked.connect(self.export_quantity)
		self.deleteButton.clicked.connect(self.delete)
		self.downloadImageButton.clicked.connect(self.download_image)
		self.deleteImageButton.clicked.connect(self.delete_image)
		self.Inventory = Inventory()

	# Get all UI data to dict
	def get_ui_data(self):
	    ui_dict = {}
	    for widget in qApp.allWidgets():
	        if isinstance(widget, QtWidgets.QLineEdit) and widget.text() != '':
	                ui_dict[widget.objectName()] = widget.text()
	    return ui_dict

	# Show dict to UI
	def set_ui_data(self, set_dict):
	    for widget in qApp.allWidgets():
	        if isinstance(widget, QtWidgets.QLineEdit) and set_dict[widget.objectName()] != None:
	            widget.setText(str(set_dict[widget.objectName()]))
	    self.set_ui_picture(set_dict['asin'])

	def set_ui_picture(self, asin):
		image_path = ProductImages_path + '/' + asin + '.jpg'
		widget = self.image

		if os.path.exists(image_path):
			pixmap = QPixmap(image_path)
			try:
				pixmap_height = widget.height()
				pixmap_width = pixmap.width() * widget.height()/pixmap.height()
				pixmap = pixmap.scaled(pixmap_height, pixmap_width, QtCore.Qt.KeepAspectRatio) # ReSize
				widget.setPixmap(pixmap)
				widget.setAlignment(QtCore.Qt.AlignCenter)
			except:
				pass
		else:
			pixmap = QPixmap('')
			widget.setPixmap(pixmap)

	# Save html and open chrome
	def save_html(self, dataframe):
	    # path = os.path.join(os.getcwd(), "search_result.html")
	    path = 'export/search_result.html'
	    with open(path, 'w') as f:
	        html = dataframe.to_html()
	        soup = bs(html, features="lxml")
	        target = soup.find_all(text=re.compile(r'None'))
	        for v in target:
	            v.replace_with(v.replace('None',''))
	        f.write(str(soup))
	    webbrowser.get(GoogleChrome_path + ' %s').open(path)

	def save_csv(self, dataframe):
		path = 'export/' + 'search_result_' + datetime.now().strftime("%Y.%m.%d_%H.%M.%S") + '.csv'
		df = dataframe.replace(np.nan, '', regex=True)
		with open(path, 'w') as f:
			f.write(df.to_csv())

	def search(self):
		search_dict = self.get_ui_data()
		self.Inventory = Inventory()
		search_res_df = self.Inventory.search_inventory(search_dict)

		# Check and show search result to UI
		if search_res_df.shape[0] == 0:
		    QtWidgets.QMessageBox.about(self, 'Search Result ', 'No Result')
		    return 'No result'
		elif search_res_df.shape[0] == 1:
		    search_res_dict = search_res_df.reset_index(drop=True).loc[0].to_dict() #Change dataframe to dict
		    for key in ['unit_price', 'quantity']:
		        try:
		        	search_res_dict[key] = int(search_res_dict[key])
		        except:
		        	pass
		    self.set_ui_data(search_res_dict)
		else:
		    self.save_html(search_res_df)
		    self.save_csv(search_res_df)


	def clear(self):
		for widget in qApp.allWidgets():
			if isinstance(widget, QtWidgets.QLineEdit):
				widget.setText('')
			elif isinstance(widget, QtWidgets.QLabel):
				if widget.objectName() == 'image':
					widget.setPixmap(QPixmap(''))

	def update(self):
	    update_dict = self.get_ui_data()
	    self.Inventory = Inventory()
	    update_result = self.Inventory.update_inventory(update_dict, primary_key='asin')
	    if update_result:
	    	QtWidgets.QMessageBox.about(self, 'Update Error', 'Update Error')
	    else:
	    	QtWidgets.QMessageBox.about(self, 'Update Successful', 'Update successful')


	def insert(self):
		insert_dict = self.get_ui_data() # Get search dict from UI[]

		# Check data before update
		note = []
		must_enter = ['asin', 'product_name']
		must_enter_number = ['unit_price']

		for key in must_enter:
			if key not in insert_dict:
				note.append('Please enter %s' % key)
			elif insert_dict[key] == '':
				note.append('Please enter %s' % key)
		for key in must_enter_number:
			try:
				insert_dict[key] = float(insert_dict[key])
			except:
				note.append('%s must be a digit' % key)

		if note != []:
			note_text = '\n-------\n'.join(note)
			QtWidgets.QMessageBox.about(self, 'Update Error', note_text)
		else:
			insert_res = self.Inventory.insert_inventory(insert_dict)
			if insert_res:
				QtWidgets.QMessageBox.about(self, 'Insert Error', 'Insert Error')
			else:
				QtWidgets.QMessageBox.about(self, 'Insert Successful', 'Insert Successful')


	def import_export(self, im_or_ex):
		ui_dict = self.get_ui_data()
		search_res = None
		if ui_dict == {}:
			input_jan = QtWidgets.QInputDialog.getText(self, "Enter JAN", "Please enter JAN")
			self.jan.setText(input_jan[0])
			search_res = self.search()

		if search_res:
			pass
		else:	
			ui_dict = self.get_ui_data()
			old_quantity = int(ui_dict['quantity'])

			if im_or_ex == 'import':
				update_quantity = QtWidgets.QInputDialog.getText(self, "Import", "Please enter Import quantity:")[0]
			elif im_or_ex == 'export':
				update_quantity = QtWidgets.QInputDialog.getText(self, "Export", "Please enter Export quantity:")[0]

			if update_quantity == '':
				QtWidgets.QMessageBox.about(self, 'Note', 'Nothing Updated')
			else:
				try:
					update_quantity = int(update_quantity) # Check number available or not 
					if im_or_ex == 'import':
						new_quantity = old_quantity + update_quantity
					elif im_or_ex == 'export':
						new_quantity = old_quantity - update_quantity
					self.quantity.setText(str(new_quantity)) # Caculate and set to ui
					self.update() # Update from ui
				except:
					QtWidgets.QMessageBox.about(self, 'Input Error', 'Quantity must be an Integer')

	def import_quantity(self):
		self.import_export(im_or_ex='import')
	def export_quantity(self):
		self.import_export(im_or_ex='export')

	def delete(self):
		ui_dict = self.get_ui_data()
		if 'asin' in ui_dict:
			res = QtWidgets.QMessageBox.information(self, 'DELETE Record', "Delete record?", 
					QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
			if res == QtWidgets.QMessageBox.Yes:
				delete_res = self.Inventory.delete_inventoty(ui_dict['asin'])
				if delete_res:
					QtWidgets.QMessageBox.about(self, 'Delete Error', 'Delete Error')
				else:
					QtWidgets.QMessageBox.about(self, 'Delete Successful', 'Delete Successful')
		else:
			QtWidgets.QMessageBox.about(self, 'Input Error', 'Please enter ASIN')

	def download_image(self):
		ui_dict = self.get_ui_data()
		if 'asin' in ui_dict:
			asin = ui_dict['asin']
			Amazon_scrapt = AmazonScrapt(asin)
			res = Amazon_scrapt.dowload_fist_image()
			if res:
				QtWidgets.QMessageBox.about(self, 'Download Picture Error', 'Can not dowload picture')
			else:
				self.set_ui_picture(asin)
		else:
			QtWidgets.QMessageBox.about(self, 'Input Error', 'Please enter ASIN')

	def delete_image(self):
		ui_dict = self.get_ui_data()
		if 'asin' in ui_dict:
			asin = ui_dict['asin']
			path = ProductImages_path + '/' + asin + '.jpg'
			os.remove(path)
			self.set_ui_picture(asin)
		else:
			QtWidgets.QMessageBox.about(self, 'Input Error', 'Please enter ASIN')

#################################################################
if __name__ == '__main__':

    # Create Table #
    # create_table_dimentions()
    # create_table_settings()

    # Run UI #
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()




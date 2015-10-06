import io
import sys
import csv
from configReader import ConfigReader

class FileReader:

	def __init__(self):
		self.configReader = ConfigReader()
		self.config = self.configReader.readConfig()

		
	def readHeader(self):

		file = self.config.get('Csv', 'csv.file')
		topOffset = self.config.get('Csv','csv.topOffset')
		
		with open(file, "rb") as csvfile:
			file = csv.reader(csvfile, delimiter=',', quotechar='"')
			data = []
			for lines in file:
				data.append(lines)
			columns = data[int(topOffset)]		
		
		return columns
	
	def readRows(self) :
		
		file = self.config.get('Csv', 'csv.file')
		topOffset = self.config.get('Csv','csv.topOffset')
		
		with open(file, "rb") as csvfile:
			file = csv.reader(csvfile, delimiter=',', quotechar='"')
			data = []
			for lines in file:
				data.append(lines)
				#print data
			startRow = int(topOffset)+ 1
			endRow = len(data)		
			rows = data[startRow:endRow]

		return rows
	
		
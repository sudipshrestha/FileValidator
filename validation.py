from datetime import datetime

class Validation :

	def validateHeaders(self,dbColumns,fileColumns):
		self.dbColumns = dbColumns
		self.fileColumns = fileColumns
		
		for i in range (len(self.dbColumns)):
			if self.fileColumns[i] <> self.dbColumns[i]:
				return False
	
		return True

	
	def validateRow(self,dataType,eachRow):
		self.dataType = dataType
		self.eachRow = eachRow	
		
		for i in range (len(self.dataType)):
			
			value = self.eachRow[i]
			
			if self.dataType[i] == "int":
				print self.dataType[i]
				if self.isValueInt(value) is False:
					return False
			
			elif self.dataType[i] == "datetime":
				print self.dataType[i]
				if self.isValueDatetime(value) is False:
					return False
			
			else :
				print self.dataType[i]
				if self.isValueVarchar(value) is False:
					return False
	
	
	def isValueInt(self,value):
		try:		
			int(value)
			return True
		except :
			return False	
				
	def isValueDatetime(self,value):
		try:		
			datetime.strptime(value, "%d/%m/%Y %H:%M")
			return True
		except :
			return False

	def isValueVarchar(self,value):
		try:		
			str(value)
			return True
		except :
			return False
		
		
		

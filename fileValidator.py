from fileReader import FileReader
from tableMetadata import TableMetadata
from validation import Validation

class FileValidator:
	rowNum = 0

	def __init__(self):	
		fileReader = FileReader()
		tableMetadata = TableMetadata()
		validation = Validation()
		error = None
		
		fileColumns = fileReader.readHeader()
		dbColumns = tableMetadata.readTableHeader()
		
		if validation.validateHeaders(dbColumns,fileColumns):
			dataType = tableMetadata.readMetadata()
			fileRows = fileReader.readRows()
			
			for eachRow in fileRows :	
				self.rowNum = self.rowNum + 1
				if validation.validateRow(dataType,eachRow,self.rowNum) is False:
					error = "Error in dataType"
					break	
		else:
			error =  "Error in header"
		
		if error:
			print error
		else:	
			print"File sucessfully validated"
		
		
		
if  __name__ =='__main__':
	fileValidator = FileValidator()
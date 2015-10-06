from fileReader import FileReader
from tableMetadata import TableMetadata
from validation import Validation

class FileValidator:

	def __init__(self):	
		fileReader = FileReader()
		tableMetadata = TableMetadata()
		validation = Validation()
		
		fileColumns = fileReader.readHeader()
		dbColumns = tableMetadata.readTableHeader()
		
		if validation.validateHeaders(dbColumns,fileColumns):
			dataType = tableMetadata.readMetadata()
			fileRows = fileReader.readRows()
			
			for eachRow in fileRows :	
	
				if validation.validateRow(dataType,eachRow) is False:
					print "Error in dataType"
					break	
				else:
					print "success"
		
		else:
			print "Error in header"
			
		
if  __name__ =='__main__':
	fileValidator = FileValidator()
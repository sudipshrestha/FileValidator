import sys
from fileReader import FileReader
from tableMetadata import TableMetadata
from validation import Validation
from sortfiletype import SortFileType

class FileValidator:
	rowNum = 0

	def __init__(self):
		#importing the client name and raw table name passed as parameters
		clientName = sys.argv[1]
		fileName = sys.argv[2]
		
		sortFileType = SortFileType()
		fileType,rawTableName = sortFileType.getFileType(clientName,fileName)
		#print fileType
		#print rawTableName
		
		fileReader = FileReader(fileName)
		tableMetadata = TableMetadata()
		validation = Validation()
		error = None
		
		fileColumns = fileReader.readHeader()
		dbColumns = tableMetadata.readTableHeader(clientName,rawTableName)
		
		if validation.validateHeaders(dbColumns,fileColumns):
			dataType = tableMetadata.readMetadata(clientName,rawTableName)
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
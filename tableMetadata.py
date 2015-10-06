import MySQLdb
from dbConnection import DbConnection

class TableMetadata:
	
	
	def __init__(self):
		self.dbConnection = DbConnection()
		self.conn = self.dbConnection.dbConnect()
	

	def readTableHeader (self):

		cursor = self.conn.cursor()
		cursor.execute("select raw_column_field from test_db.data_validation where client_name = 'Teletech';")
		dbColumns = cursor.fetchall()

		rawColumns =[]
		for eachColumn in dbColumns:
			eachColumn  = [x.strip(',') for x in eachColumn]
			rawColumns.append(eachColumn)	
		#self.conn.close()
		
		columns = []
		for i in range (len(rawColumns)):
			 columns.append(rawColumns[i][0])
	
		return columns
	
	def readMetadata (self) :
		
		cursor = self.conn.cursor()
		cursor.execute("select data_types from test_db.data_validation where client_name = 'Teletech';")
		columns = cursor.fetchall()
		
		rawColumns =[]
		for eachColumn in columns:
			eachColumn  = [x.strip(',') for x in eachColumn]
			rawColumns.append(eachColumn)	
		self.conn.close()
		
		dataType = []
		for i in range (len(rawColumns)):
			 dataType.append(rawColumns[i][0])
	
		return dataType
	


	
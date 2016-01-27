import sys
import re

class SortFileType:

	def getFileType(self,clientName,fileName):
		
		if clientName == "Correctcare":
			if re.search('^jobs\.[0-9.]+\.csv',fileName):
				fileType = 'req'
				rawTableName = 'zzz_cc_req_raw'
				return fileType,rawTableName
			elif (re.search('^candidates\.[0-9.]+\.csv',fileName)):
				fileType = 'candidate'
				rawTableName = 'zzz_cc_candidate_raw'
				return fileType,rawTableName
			else:
				sys.exit("Unknown file")
				
		elif clientName == "Pepsico":
			if re.search('^NEW\sBB\sCandidate\s',fileName):
				fileType = 'candidate'
				rawTableName = 'zzz_pepsico_candidate_raw'
				return fileType,rawTableName
			elif (re.search('^NEW\sBB\sReq\s',fileName)):
				fileType = 'req'
				rawTableName = 'zzz_pepsico_req_raw'
				return fileType,rawTableName
			else:
				sys.exit("Unknown file")
			
		else:
			sys.exit("Unknown client")
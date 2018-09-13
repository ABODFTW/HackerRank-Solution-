
import os
import sys
import time
#
# Complete the timeConversion function below.
#
def timeConversion(s):
	new_format = time.strptime(s , "%I:%M:%S%p")
	print(('{0:0=2d}'.format(new_format.tm_hour) + ":" +  
		'{0:0=2d}'.format(new_format.tm_min)) + ":" +
		'{0:0=2d}'.format(new_format.tm_sec))
	# print(f"{'{0:0=2d}'.format(new_format.tm_hour)}:"+ 
	# 	f"{'{0:0=2d}'.format(new_format.tm_min)}:" + 
	# 	f"{'{0:0=2d}'.format(new_format.tm_sec)}")



if __name__ == '__main__':

	f = open(os.environ['OUTPUT_PATH'], 'w')

	s = input()
	# s = "07:50:05PM"

	result = timeConversion(s)

	f.write(result + '\n')

	f.close()

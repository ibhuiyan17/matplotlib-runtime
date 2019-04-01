#csvTest.py

import csv
import time


path = raw_input("enter path of csv file: ")


startTime = time.time()
with open(path, 'rb') as csvfile:
	contents = []
	file_reader = csv.reader(csvfile, delimiter = ',')

	'''
	row_num = 1
	for row in file_reader:
		print 'Row #%d:' % row_num,       #Prints Contents in easy to read way
		print row
		row_num += 1
	
	for row in file_reader:
		print row[6]                      #accessing column index 1 of each row
	'''

	for row in file_reader:
		contents.append(row)              #makes list of list (2d array) copy of csv file

	print contents, '\n\n'
	print contents[9][0]     #accessing arr[row][col]
	print 'num rows:', len(contents)
	print 'num cols:', len(contents[0])

	for row in contents:
		for val in row:
			print val + ',',
		print ''



endTime = time.time()
print 'time elapsed: %f seconds' % (endTime - startTime) 

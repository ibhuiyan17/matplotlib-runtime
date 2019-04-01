#runtimes.py


'''
Creates an output file of time it takes for python to perform a series of 
operations. The file will later be plotted using matplotlib to see if 
efficiency of python decreases over time

#/Users/ibtida.bhuiyan/Desktop/Dev/Python/Plotting/Runtime Test Output/untitled folder
'''

import csv
import time

arrFile = []
inFile = raw_input("pathname of file to run test on: ")
outFileName = raw_input("name for output file: ")
outpath = '/Users/ibtida.bhuiyan/Desktop/Dev/Python/Plotting/Runtime Test Output/' + outFileName

numIterations = int(raw_input("enter iterations to check (keep below 1000): "))
while numIterations > 1000:
	numIterations = int(raw_input("enter iterations to check (keep below 1000): "))

descChoice = int(raw_input("Would you like to add a description to the output? 1 = yes, 2 = no: "))
if descChoice == 1:
	description = raw_input("Type Description: ")
	description = '#' + description + '#\n\nRuntimes per iteration:\n'

#opening file to be written to
programStart = time.time()
sum = 0
with open(outpath, 'w') as times:
	times.write(description)
	#runs test user inputed number of times
	for i in range(numIterations):
		#runs operations wit csv file
		startTime = time.time()
		with open(inFile, 'rb') as csvfile:
			file_reader = csv.reader(csvfile, delimiter = ',')

			#makes copy of csv as list of list
			for row in file_reader:
				arrFile.append(row)

			#prints csvfile to console
			for row in arrFile:
				for val in row:
					print val + ',',
				print ''

		endTime = time.time()
		times.write(str(endTime - startTime))
		times.write('\n')
		sum = sum + (endTime - startTime)
	times.write('\n\nFull Program runtime: %s seconds' % (str(sum)))
	print sum



			





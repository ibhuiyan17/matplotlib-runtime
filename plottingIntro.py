#plottingIntro.py

import matplotlib.pyplot as plt

inputFiles = []

print 'enter "q" when all desired input files are loaded'



while True:
	dataIn = raw_input("pathname of input file: ")
	if dataIn == 'q':
		break
	else:
		inputFiles.append(dataIn)	


'''
with open(dataIn) as data:
	
	times = data.readLines()    #this includes description so fix

	for i in range(3):
		del times[i]
		del times[len(times) - 1 - i]

	print times
'''
for i in range(len(inputFiles)):
	with open(inputFiles[i]) as data:
		times = data.readlines()
		dataPoints = []

		for i in range(3):
			del times[0]
			del times[len(times) - 1]

		for t in times:
			dataPoints.append(float(t))

		numIteration = range (1, len(dataPoints) + 1)  #list of iterations

		plt.plot(numIteration, dataPoints)


plt.show()




'''
	data = open(inputFiles[i])
	times = data.readlines()
	dataPoints1 = []

	for i in range(3):
		del times[0]



	for t in times:
		dataPoints1.append(float(t))



	nums1 = range(1,1001)

	plt.plot(nums, dataPoints)

	plt.show()
'''


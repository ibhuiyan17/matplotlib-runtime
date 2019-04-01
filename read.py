#read.pyLd
import time

email = open('message.txt')
#contents = email.read()        reads whole file
sentences = email.readlines()	#makes list of sentences
email.close()

#print contents + '\n'
#print sentences

file = open('writeTest.txt', 'w')            #arguments: r-read, w-write, a-append

starTime = time.time()

print 'writing to file'
for i in range(9999999):
	file.write('ilham')
file.write('\n')
file.close()
print 'finished'

endTime = time.time()
print 'elapsed time', (endTime - starTime)


'''
Things to learn:

-os and sys modules
-binary data
-csv module and files


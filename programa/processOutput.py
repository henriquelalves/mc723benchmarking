#!/usr/bin/python
#import pdb
import math

'''
def desvioPadrao(numbers_list):
	n = len(numbers_list)
	media = sum(numbers_list) / n
	sigma = 0
	
	for x in numbers_list:
		sigma += (x - media) * (x - media)
	
	sigma = sigma / (n - 1)
	sigma = math.sqrt(sigma)
	
	return sigma
'''

def harmonicMean(numbers):
	n = len(numbers)
	s = 0
	
	for x in numbers:
		s += 1.0 / float(x)
	
	return n / s	

def propagateUncert(a, b, sigma_a, sigma_b):
	#return math.sqrt((sigma_a / b)**2 + ((sigma_a / b**2)**2) * sigma_b**2)
	return (a / b) * math.sqrt((sigma_a / a)**2 + ((sigma_b / b)**2))
		
#captura dados do output
input = open('output/perf.out')
text = input.readlines()[3:]
dict = {}
for item in text:
	rawList = item.split()
	proclist = [x for x in rawList if x != '']
	if len(proclist) > 1 and "not" not in proclist[0]:
		#pdb.set_trace()
		if(proclist[2] == "time"):
			x = float(proclist[0].replace(',','.'))
			dict[proclist[2]] = (x, (float(proclist[len(proclist) - 2].replace('%', '').replace(',', '.')) / 100.0) * x)
		else:
			x =  float(proclist[0].replace(',','').replace('.', ''))
			dict[proclist[1].replace(":u", "")] = (x, (float(proclist[len(proclist) - 3].replace('%', '').replace(',', '.')) / 100.0) * x)

#pdb.set_trace()

cyclePerInstruc = dict['cycles'][0]/dict['instructions'][0]
l1MissRatio = dict['L1-dcache-load-misses'][0]/dict['L1-dcache-loads'][0]
l1MissRatePTI = dict['L1-dcache-load-misses'][0]/(dict['instructions'][0]/1000)
dataTLBMissRatio = dict['dTLB-load-misses'][0]/dict['cache-references'][0]
dataTLBMissRatePTI = dict['dTLB-load-misses'][0]/(dict['instructions'][0]/1000)
branchMispredictRatio = dict['branch-misses'][0]/dict['branch-instructions'][0]
branchMispredictRatePTI = dict['branch-misses'][0]/(dict['instructions'][0]/1000)
time = dict['time'][0]

cyclePerInstruc_sigma = propagateUncert(dict['cycles'][0], dict['instructions'][0], dict['cycles'][1], dict['instructions'][1]) 
l1MissRatio_sigma = propagateUncert(dict['L1-dcache-load-misses'][0], dict['L1-dcache-loads'][0], dict['L1-dcache-load-misses'][1], dict['L1-dcache-loads'][1])
l1MissRatePTI_sigma = propagateUncert(dict['L1-dcache-load-misses'][0], (dict['instructions'][0]/1000), dict['L1-dcache-load-misses'][1], (propagateUncert(dict['instructions'][0], 1000, dict['instructions'][1], 0)))
dataTLBMissRatio_sigma = propagateUncert(dict['dTLB-load-misses'][0], dict['cache-references'][0], dict['dTLB-load-misses'][1], dict['cache-references'][1])
dataTLBMissRatePTI_sigma = propagateUncert(dict['dTLB-load-misses'][0], (dict['instructions'][0]/1000), dict['dTLB-load-misses'][1], (propagateUncert(dict['instructions'][0], 1000, dict['instructions'][1], 0)))
branchMispredictRatio_sigma = propagateUncert(dict['branch-misses'][0], dict['branch-instructions'][0], dict['branch-misses'][1], dict['branch-instructions'][1])
branchMispredictRatePTI_sigma = propagateUncert(dict['branch-misses'][0], (dict['instructions'][0]/1000), dict['branch-misses'][1], (propagateUncert(dict['instructions'][0], 1000, dict['instructions'][1], 0)))
time_sigma = dict['time'][1]
	

#imprime media
print "Cycles per Instructions: " +  str(cyclePerInstruc) + " +- " +  str((cyclePerInstruc_sigma / cyclePerInstruc) * 100) + "%"
print "L1 cache miss ratio: " +  str(l1MissRatio) + " +- " +  str((l1MissRatio_sigma / l1MissRatio) * 100) + "%"
print "L1 cache miss rate PTI: " +  str(l1MissRatePTI) + " +- " +  str((l1MissRatePTI_sigma / l1MissRatePTI) * 100) + "%"
print "Data TLB miss ratio: " +  str(dataTLBMissRatio) + " +- " +  str((dataTLBMissRatio_sigma / dataTLBMissRatio) * 100) + "%"
print "Tempo: " +  str(time) + " +- " +  str((time_sigma / time) * 100)  + "%"

#get time used for reading pdb from gprof output
#captura dados do output
input = open('gprof.txt')
text = input.readlines()[5:]
disk_time = 0

#pdb.set_trace()
for item in text:
	rawList = item.split()
	#pdb.set_trace()
	if(rawList[len(rawList) - 1] == "readpdb"):
		disk_time  = rawList[0]
		break

print "Disk Time Usage: " + str(disk_time) + "%"
		

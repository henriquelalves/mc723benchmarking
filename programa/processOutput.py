#!/usr/bin/python
#import pdb

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
			dict[proclist[2]] = (float(proclist[0].replace(',','.')), float(proclist[len(proclist) - 2].replace('%', '').replace(',', '.')))
		else: 
			dict[proclist[1].replace(":u", "")] = (float(proclist[0].replace(',','').replace('.', '')), float(proclist[len(proclist) - 3].replace('%', '').replace(',', '.')))

#pdb.set_trace()

cyclePerInstruc = dict['cycles'][0]/dict['instructions'][0]
l1MissRatio = dict['L1-dcache-load-misses'][0]/dict['L1-dcache-loads'][0]
#l1MissRatePTI = dict['L1-dcache-load-misses'][0]/(dict['instructions'][0]/1000)
dataTLBMissRatio = dict['dTLB-load-misses'][0]/dict['cache-references'][0]
dataTLBMissRatePTI = dict['dTLB-load-misses'][0]/(dict['instructions'][0]/1000)
branchMispredictRatio = dict['branch-misses'][0]/dict['branch-instructions'][0]
branchMispredictRatePTI = dict['branch-misses'][0]/(dict['instructions'][0]/1000)
time = dict['time'][0]

cyclePerInstruc_sigma = dict['instructions'][1]
l1MissRatio_sigma = dict['L1-dcache-load-misses'][1]
#l1MissRatePTI_sigma = dict['L1-dcache-load-misses'][1]
dataTLBMissRatio_sigma = dict['dTLB-load-misses'][1]
dataTLBMissRatePTI_sigma = dict['dTLB-load-misses'][1]
branchMispredictRatio_sigma = dict['branch-misses'][1]
branchMispredictRatePTI_sigma = dict['branch-misses'][1]
time_sigma = dict['time'][1]
	

#imprime media
print "Cycles per Instructions: " +  str(cyclePerInstruc) + " +- " +  str(cyclePerInstruc_sigma)
print "L1 cache miss ratio: " +  str(l1MissRatio) + " +- " +  str(l1MissRatio_sigma)
#print "L1 cache miss rate PTI: " +  str(l1MissRatePTI) + " +- " +  str(l1MissRatePTI_sigma)
print "Data TLB miss ratio: " +  str(dataTLBMissRatio) + " +- " +  str(dataTLBMissRatio_sigma)
print "Tempo: " +  str(time) + " +- " +  str(time_sigma)

#!/usr/bin/python

input = open('perfOutput1.out')
text = input.readlines()[3:]
dict = {}
for item in text:
    rawList = item.split(" ")
    proclist = [x for x in rawList if x != '']
    if len(proclist) > 1 and "not" not in proclist[0]:
        dict[proclist[1]] = float(proclist[0].replace(',',''))

instrucPerCycle = dict['instructions']/dict['cycles']
l1MissRatio = dict['L1-dcache-load-misses']/dict['L1-dcache-loads']
l1MissRatePTI = dict['L1-dcache-load-misses']/(dict['instructions']/1000)
dataTLBMissRatio = dict['dTLB-load-misses']/dict['cache-references']
dataTLBMissRatePTI = dict['dTLB-load-misses']/(dict['instructions']/1000)
branchMispredictRatio = dict['branch-misses']/dict['branch-instructions']
branchMispredictRatePTI = dict['branch-misses']/(dict['instructions']/1000)

print "Instructions per cycle: "
print instrucPerCycle
print "L1 cache miss ratio:"
print l1MissRatio
print "L1 cache miss rate PTI:"
print l1MissRatePTI
print "Data TLB miss ratio:"
print dataTLBMissRatio

list = [1/instrucPerCycle,l1MissRatio,l1MissRatePTI,dataTLBMissRatio,dataTLBMissRatePTI,branchMispredictRatio,branchMispredictRatePTI]
print "Media:"
print sum(list)/len(list)

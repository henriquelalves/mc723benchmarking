#só roda o programa uma vez, pra gerar o gmon.out
./solver

#gprof interpreta gmon.out
gprof solver gmon.out > gprof.txt

#cria graficos do gprof(nao eh necessario)
#gprof solver | python gprof2dot.py -n0 -e0 | dot -Tpng -o output.png

#roda o perf no programa, altere o numero dps de "-r" para mudar o numero de runs
perf stat -d -r 5 -e instructions,cycles,L1-dcache-loads,L1-dcache-load-misses,dTLB-load-misses,cache-references,branch-misses,branch-instructions ./solver > output/perf.out 2>&1

#script para interpretar os dados
python processOutput.py

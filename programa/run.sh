#só roda o programa
# ./solver

#gera graficos do gprof
# gprof solver | python gprof2dot.py -n0 -e0 | dot -Tpng -o output.png

# 3 iteracoes do perf para calcularmos a media dos valoresp posteriormente
echo 'Primeira iteração do perf'
perf stat -d -e instructions,cycles,L1-dcache-loads,L1-dcache-load-misses,dTLB-load-misses,cache-references,branch-misses,branch-instructions ./solver > perfOutput1.out 2>&1
echo 'Segunda iteração do perf'
perf stat -d -e instructions,cycles,L1-dcache-loads,L1-dcache-load-misses,dTLB-load-misses,cache-references,branch-misses,branch-instructions ./solver > perfOutput2.out 2>&1
echo 'Terceira iteração do perf'
perf stat -d -e instructions,cycles,L1-dcache-loads,L1-dcache-load-misses,dTLB-load-misses,cache-references,branch-misses,branch-instructions ./solver > perfOutput3.out 2>&1


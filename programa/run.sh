#só roda o programa
# ./solver

#gera graficos do gprof
# gprof solver | python gprof2dot.py | dot -Tpng -o output.png

#cache misses
# perf stat -B -e cache-references,cache-misses,cycles,instructions,branches,faults,migrations ./solver < tests/test0

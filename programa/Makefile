#OPT = -O1
#-pg -fopenmp
# ----------------------------------

solver: solver.c solver_functions.c heap.c
	gcc -pg -o solver solver.c solver_functions.c heap.c -lm

clean :
	$(RM) solver


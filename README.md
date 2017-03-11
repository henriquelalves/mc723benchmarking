# Programa 0 - 15-puzzle solver

## O que faz? Para que serve?
O programa escolhido é um solver ótimo para o 15-puzzle. Isto é, dado qualquer estado possível do 15-puzzle, o programa computa a solução que move o menor número de peças.
 
## Por que é bom para medir desempenho?
O 15-puzzle é um problema combinatório difícil devido ao alto número de permutações possíveis. Assim sendo, a busca da solução ótima com o algoritmo A* 
necessita de uma quantidade de tempo razoável e pode ser utilizada para medir o desempenho da CPU da máquina.

Também destacamos que a heurística utilizada pelo A*, chamada Pattern Databases, pré-computa as soluções para problemas menores, chamados patterns, e salva em um arquivo separado, que será posteriormente utilizado pelo solver.
Portanto, antes do solver iniciar a árvore de busca, ele carrega do disco para a RAM um arquivo que representa as soluções para os patterns. Esse arquivo possui cerca de 11.7MB e ele pode oferecer uma medida
sobre a velocidade de leitura ao disco da máquina a ser analizada.

## O que baixar
O programa poder ser encontrado na pasta "final" do seguinte repositório: https://github.com/matheusota/Sliding-Puzzle-Solver

## Como compilar/instalar
O programa deverá ser instalado no computador, compilado localmente. Não deixar o binário disponível. Não deve ser necessário instalar como administrador do computador (root)

## Como executar
Instruções para execução. Se seu programa precisa de entradas, você deve fornece-las para que todos executem corretamente.
## Como medir o desempenho
Como que o desempenho é medido através deste programa? Se for através de tempo, você deve especificar claramente qual tempo deverá ser utilizado e indicar o motivo aqui. Quantas vezes a medida deverá ser feita? O que fazer com ela (média, etc) ? Não especificar o tempo será considerado falha grave.
## Como apresentar o desempenho
Como o desempenho deverá ser mostrado. Margem de erro, etc. 
## Medições base (uma máquina)
Inclua a especificação dos componentes relevantes e os resultados de desempenho.

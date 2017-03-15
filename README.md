# Programa: 15-puzzle solver

## O que faz? Para que serve?
O programa escolhido é um solver ótimo para o 15-puzzle. Isto é, dado qualquer estado possível do 15-puzzle, o programa computa a solução que move o menor número de peças.
 
## Por que é bom para medir desempenho?
O 15-puzzle é um problema combinatório razovelmente difícil devido ao alto número de permutações possíveis. Assim sendo, a busca da solução ótima com o algoritmo A* 
explora uma árvore de busca de grande tamanho e pode ser utilizado como uma medida do desempenho do processador. Destaca-se que o programa utilizado não utiliza processamento paralelo, e portanto
o desempenho avaliado corresponde a um único core.

Também destacamos que a heurística utilizada pelo A*, chamada Pattern Databases, pré-computa as soluções para problemas menores, chamados patterns, e salva em um arquivo separado. 
Portanto, antes do solver iniciar a árvore de busca, ele carrega do disco para a RAM um arquivo que representa as soluções para os patterns. Na RAM esses patterns são salvos em uma tabela hash.
Esse arquivo possui cerca de 11.7MB, a inserção na tabela hash consome grande parte do tempo. e ele pode oferecer uma medida sobre a velocidade de leitura ao disco da máquina a ser analizada.

## O que baixar
O programa pode ser encontrado na pasta "programa" do seguinte repositório: https://github.com/henriquelalves/mc723benchmarking.git

## Como compilar/instalar
Um Makefile está disponível na pasta do programa, portanto, para compilar, basta que o usuário digite "make" no terminal.

## Como executar
Um script para rodar o programa também está disponível. Uma vez que o programa esteja compilado, para rodá-lo basta que o usuário digite "./run.sh" no terminal.

## Como medir o desempenho

Como que o desempenho é medido através deste programa? 
Se for através de tempo, você deve especificar claramente qual tempo deverá ser utilizado e indicar o motivo aqui. 
Quantas vezes a medida deverá ser feita? O que fazer com ela (média, etc) ? Não especificar o tempo será considerado falha grave.

As seguintes medidas serão consideradas: 
* tempo de execução
* instruções por ciclo
* taxa de miss da cache L1 (cache-loads/cache-loads-misses)
* misses da L1 por mil instruções
* taxa de miss da TLB (TLB load misses / cache-references)
* misses da TLB por mil instruções
* taxa de erros na predição de branch (branch-misses/branch-instructions)
* erros na predição de branch por mil instruções

## Como apresentar o desempenho
Pensei em utilizar o tempo total, tempo de leitura de disco e o output do que o Borges passou. Podemos colocar tambem um desvio padrao para a media dos tempos.
Aí coloca numa tabela e gg.
 
## Medições base (uma máquina)
(coloquei as specs do meu computador)

Processador | Cores | Cache | Disk Model
--- | --- | --- | ---
Intel(R) Core(TM) i7-4720HQ CPU @ 2.60GHz | 4 | L1: 32K, L2: 256K, L3: 6144K | HGST HTS721010A9E630


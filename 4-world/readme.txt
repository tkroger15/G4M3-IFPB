4-1
Entrada
A entrada contém um único inteiro N, entre 1 e 2×10^9, inclusive.

Saída
A saída deve conter um único inteiro, representando a quantidade de números na sequência gerada a partir de N.


4-2
Entrada
A primeira linha da entrada contém um número NNN, indicando o tamanho da matriz.

As próximas NNN linhas contém NNN inteiros cada, separados por espaço. Cada inteiro representa sua estimativa da quantidade de goblins presentes naquela célula (desconsiderando K-Ôru).

Considere 1≤N≤501 \le N \le 501≤N≤50.

Considere que todos os números da matriz são maiores que 111 e menores que 300300300.

Saída
Você deve imprimir a versão simplificada da matriz de entrada.

Para cada célula, deve ser impresso um dentre três caracteres: +, quando sempre for possível entrar na célula; -, quando nunca for possível entrar na célula; o, quando for possível entrar na célula apenas quando K-Ôru não estiver presente. Os caracteres na mesma linha não devem ser separados. Observe o exemplo.

Após imprimir a matriz, deve-se imprimir uma linha em branco.

Em seguida, deve-se imprimir a contagem de +, o e - na matriz simplificada, seguindo o padrão: S: X, onde S representa o símbolo e X a quantidade. Observe com cuidado o exemplo.


4-3
Entrada
A entrada é composta por um único inteiro NNN.

Considere 1≤N≤1001 \le N \le 1001≤N≤100.

Considere que o ar no pulmão de Glooid nunca será capaz de soprar mais que 10000 melões.

Saída
A saída deve ser composta pela sequência gerada a partir de NNN, começando em NNN e terminando em 111. Deve-se imprimir um valor por linha.


4-4
Entrada
A entrada representa o mapa da parte central da cidade com as posições dos depósitos marcadas.

A primeira linha traz dois inteiros LLL e CCC, separados por um espaço, representando o número de linhas e de colunas do mapa, respectivamente.

Seguem LLL linhas, cada uma com CCC números separados por espaço. Um número 111 indica que há um depósito naquela posição, um número 000 indica o contrário.

Considere 2≤L,C≤1002 \le L, C \le 1002≤L,C≤100.

Saída
A primeira linha da saída deve trazer um inteiro XXX, indicando a quantidade de frascos de essência de melão que será necessário.

Em sequência, para cada linha do mapa, seu programa deve imprimi-la novamente, seguido da informação se será necessário ou não colocar essência nessa linha. Um caractere M indica que sim, enquanto um caractere - indica que não.

Por fim, o programa deve imprimir mais uma linha, com um caractere para cada coluna, separando-os com um espaço, informando se será necessário ou não colocar essência nessa coluna. Um caractere M indica que sim, enquanto um caractere - indica que não.


4-5
Entrada
A entrada traz o mapa da cidade com as posições dos barris de melança. A primeira linha da entrada contém um número NNN, indicando o número de linhas e colunas do mapa.

As próximas NNN linhas contêm NNN caracteres cada. Um caractere * indica a presença de um barril naquela posição, enquanto que um caractere - indica a ausência. Não há espaços em branco.

Considere 1≤N≤501 \le N \le 501≤N≤50

Saída
Dado o mapa com a localização dos barris, a saída deve ser um mapa com a quantidade de bombas que cada posição possui ao redor, considerando também as diagonais.

Para cada posição do mapa da entrada o seu programa deve imprimir:

999, caso exista uma bomba naquela posição, ou

O número de posições vizinhas que possuem bomba.

Não devem ser impressos espaços entre os números.


4-6
Entrada
A entrada possui apenas uma linha.

Esta linha traz NNN números inteiros separados por espaços, representando os tamanhos iniciais dos slimes após a sórdida magia final.

Considere 1≤N≤10001 \le N \le 10001≤N≤1000.

Considere que cada slime tem tamanho inicial no intervalo [2,99][2,99][2,99], inclusive;

Saída
A quantidade de turnos que vocês precisam aguentar fugindo até que restem apenas sementes.
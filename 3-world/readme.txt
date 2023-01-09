3-1
Entrada
A primeira linha da entrada contém um inteiro NNN, que indica a quantidade de pessoas que querem ajuda com algum problema.

Cada uma das próximas NNN linhas contém um inteiro XXX indicando a prioridade do problema de uma das pessoas da população.

Considere que 1≤N≤1001 \le N \le 1001≤N≤100 e 0≤X≤1000 \le X \le 1000≤X≤100.

Saída
A saída deve ser composta pelas mesmas prioridades da entrada, uma por linha, ordenadas de forma crescente. As pessoas serão atendidas começando pela última linha.


3-2
Entrada
A primeira linha da entrada contém um inteiro ímpar NNN indicando a quantidade de casas do tabuleiro.

A segunda linha da entrada contém NNN inteiros separados por espaço, indicando a quantidade de moedas em cada casa. A quantidade de moedas é sempre maior que 0, com exceção do buraco na casa central (que será sempre igual a 0).

Considere que 1≤N≤1001 \le N \le 1001≤N≤100.

Considere que a quantidade inicial de moedas em cada casa do tabuleiro nunca é maior que 29.

Saída
A saída deve conter um único inteiro, a quantidade mínima de turnos necessários para mover todas as moedas para o buraco.


3-3
Entrada
A entrada é formada por múltiplas linhas. Cada linha contém uma única palavra (formada unicamente por caracteres maiúsculos, minúsculos ou números), indicando um tipo de semente de melão.

A entrada termina com a palavra FIM, que não deve ser processada.

Considere que o número de linhas sempre é maior que 111 e menor que 100110011001 .

Considere que o nome de cada melão nunca tem mais que 100100100 caracteres.

Saída
Para cada linha da entrada, deve ser impresso o tipo de semente e quantas sementes daquele tipo já foram entregues, separados por um espaço.


3-4
Entrada
A entrada é formada por várias linhas. Cada linha contém uma única palavra, que pode ser o nome de uma pessoa que acabou de chegar ou a palavra PROXIMO, indicando que há um entregador livre para atender a próxima pessoa da fila.

A entrada termina com a palavra FIM, que não deve ser processada.

Considere que o número de linhas sempre é maior que 2 e menor que 200$.

Considere que o nome de cada pessoa nunca tem mais que 100 caracteres.

Considere que a entrada está correta. Nunca o próximo é chamado sem ninguém na fila. Todos da fila sao chamados.

Saída
Quando chegar uma nova pessoa, ela deve ser adicionada ao final da fila. Então, deve-se imprimir FILA: X, onde X representa todos os nomes da fila, separados por espaço (observe o exemplo).

Quando a entrada for a palavra PROXIMO, será impressa uma linha com o próximo da fila, seguindo o formato PROXIMO: X. Nesse caso, não é necessário imprimir a fila.


3-5
Entrada
A entrada possui várias linhas. A primeira linha traz o inteiro NNN, a quantidade de sementes que cabem no GFM.

Cada uma das linhas que segue traz um número inteiro aaa.

Se aaa for zero, isto significa que o ancião acha-ninjeiro achou um ninja, então você deve remover do GFM a semente com o maior valor.

Quando aaa for diferente de zero, então você deve adicionar uma semente com valor igual a aaa ao GFM.

O programa acaba quando o GFM possuir exatamente NNN sementes.

Considere que 1≤N≤1001 \le N \le 1001≤N≤100.

Considere que 0≤a≤1000 \le a \le 1000≤a≤100.

Considere que a entrada está correta. Nunca vem um ninja quando o galpão está vazio. A entrada acaba quando o GFM completar NNN sementes.

Considere que o número de linhas da entrada nunca é maior que 1000.

Saída
Toda vez que aaa for zero o seu programa deve imprimir o valor da semente retirada do GFM.
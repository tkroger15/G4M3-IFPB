1-1
Entrada
A entrada do problema possui três linhas, cada uma com um número inteiro entre 111 e 400400400.

A primeira linha traz o número pés de melão que o camponês possui.

A segunda linha traz o número melões que o camponês colheu.

A terceira linha traz o número de melões que cada pé de melão deveria produzir.

Saída
Caso o total de melões esteja abaixo do esperado pelo camponês, seu programa deve imprimir SIM.

Caso o total de melões seja igual ou esteja acima do esperado, seu programa deve imprimir NAO.

Note que todas as letras são maiúsculas, não tem acento, nem pontuação e nem deve imprimir as aspas.


1-2
Entrada
A entrada do problema possui várias linhas.

A primeira linha traz dois inteiros NNN e EEE, separados por um espaço. NNN representa o número de produtores e EEE representa o valor total esperado, segundo o ancião colheiteiro.

Seguem exatamente NNN linhas, cada uma com um número inteiro representando a quantidade de melões colhida por cada um dos produtores.

Considere que 1≤N≤1001 \le N \le 1001≤N≤100 e que cada produtor colheu pelo menos 111 e não mais que 999 melões.

Saída
Caso o total de melões colhido seja maior ou igual ao total esperado, seu programa deve imprimir a frase: NADA PREOCUPANTE.

Caso o total de melões colhido seja maior ou igual ao total esperado menos 555, seu programa deve imprimir a frase: POUCO PREOCUPANTE.

Caso o total de melões colhido seja estritamente menor que o total esperado menos 555, seu programa deve imprimir a frase: MUITO PREOCUPANTE.

Note que todas as letras são maiúsculas, não tem acento, nem pontuação e nem deve imprimir as aspas.


1-3
Entrada
A entrada do problema possui duas linhas.

A primeira linha traz dois inteiros, NNN e RRR, separados por um espaço. NNN representa o número de sensores e RRR representa o valor de referência do sensor caso nenhum objeto tenha feito sombra sobre este.

A segunda linha traz uma lista com NNN inteiros separados por um espaço em branco. Cada um desses números representa o valor de um dos sensores colocados por Ham-Ham Sino.

Considere 1≤N≤1001 \le N \le 1001≤N≤100.

Considere que tanto RRR quanto os valores dos sensores estão no intervalo [1,9][1,9][1,9].

Saída
Para cada sensor posicionado por Ham-Ham Bell, você deve imprimir:

111, caso o valor do sensor seja menor ou igual ao valor de referência RRR, indicando que a plantação foi invadida, ou

000, caso o valor do sensor seja estritamente maior que o valor de referência RRR, indicando que a plantação não foi invadida.

Estes valores devem ser impressos na mesma ordem que os sensores são listados na entrada do problema.


1-4
Entrada
A entrada possui várias linhas. A primeira linha traz um inteiro NNN, representando o número de sensores instalados.

Cada uma das NNN linhas que seguem traz um inteiro por linha, em ordem, representando a sequência dos valores de ativação dos sensores instalados.

Um valor 111 significa que o sensor foi ativado, enquanto um valor 000 significa que o sensor não foi ativado.

Considere 1≤N≤1001 \le N \le 1001≤N≤100.

Saída
Você deve imprimir apenas um número inteiro: a quantidade mínima de armadilhas que deve ser instalada para que cada conjunto contíguo de sensores ativados possua pelo menos uma armadilha.


1-5
Entrada
A entrada possui várias linhas. A primeira linha da entrada contém um inteiro PPP, indicando o tamanho da população da cidade que está de prontidão para defender os melões.

Na sequência, seguem os ataques dos goblins. Cada ataque é apresentado em uma linha contendo três inteiros: FFF, indicando a força da horda (quantos humanos são necessários para impedí-la); MMM, a quantidade de melões que a horda consegue roubar se não for impedida; e GGG, a quantidade de goblins que serão resgatados, caso a horda não seja bloqueada.

A entrada acaba com o ataque 0 0 0, que não deve ser processado.

Considere 1≤P≤1001 \le P \le 1001≤P≤100.

Considere 1≤F,M,G≤2001 \le F, M, G \le 2001≤F,M,G≤200, para todas as linhas.

Saída
Para cada ataque, seu programa deve imprimir uma linha com a informação de quantos melões (XXX) foram roubados e quantos goblins (YYY) resgatados ATÉ O MOMENTO, seguindo o formato:

Meloes roubados: X
Goblins resgatados: Y
---
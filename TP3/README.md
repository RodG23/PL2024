# PL2024

## Titulo
Somador on/off

## Autor

- **Nome:** Rodrigo Ferreira Gomes
- **ID:** A100555
  
## Funcionalidades:

Simula um AFD que percorre as palavras de um ficheiro texto.

- O estado inicial é 'on'. 
    Neste estado, sempre que é encontrado um inteiro, este é somado a um acumulador.
    Se for encontrado 'off', transita-se para o estado off, deixando-se de somar os inteiros encontrados (e vice-versa).

- Estar nos estados 'on' e 'off' e encontrar o estado atual provoca uma transição para o mesmo estado.

- Encontrar '=' não provoca nenhuma transição, mas é escrito no stdout o valor do acumulador.

- Chegando ap fim do ficheiro, transita-se para o estado 'fim', único estado final.

(PS): 'on' e 'off' podem aparecer em qualquer combinação de maiúsculas e minúsculas.
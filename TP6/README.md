# TPC6: Gramática Independente de Contexto LL(1)

## 2024-03-19

## Autor

- A100555
- Rodrigo Ferreira Gomes

## Resumo

Encontra-se implementada uma gramática independente de contexto LL(1) para o seguinte código: 

```bash
?a
b = a * 2/ (27-3)
!a+b
c = a*b / (a/b)
```

- É também garantida a prioridade dos operadres e calculado o LA (look ahead para todas as produções)
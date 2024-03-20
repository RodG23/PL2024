# GIC LL(1)

## Símbolos não terminais

- **Start**: `S`
- **Declaração**: `D`
- **Expressão**: `E`
- **Expressão'**: `E'`
- **Termo**: `T`
- **Termo'**: `T'`
- **Fator**: `F`

## Terminais

- **Input e Output**: `? | !`
- **Atribuição**: `:`
- **Igualdade**: `=`
- **Operadores**: `+ | - | * | /`
- **Parênteses**: `( | )`
- **Num**: `\d+`
- **Id**: `[a-zA-Z_]`

## Regras de Produção e LA

- ` S  -> D S       {?, !, :}`
- `     | ε         {$}`
- ` D  -> ? id      {?}`
- `     | ! E       {!}`
- `     | : id = E  {:}`
- ` E  -> T E'      {(, Id, Num, ), $}`
- ` E' -> + T E'    {+}`
- `     | - T E'    {-}`
- `     | ε         {), $}`
- ` T  -> F T'      {(, Id, Num, +, -, ), $}`
- ` T' -> * F T'    {*}`
- `     | / F T'    {/}`
- `     | ε         {+, -, ), $}`
- ` F  -> ( E )     {(}`
- `     | Id        {Id}`
- `     | Num       {Num}`

NOTA: Foi adicionado o símbolo terminal `:` para conseguir tornar a gramática LL(1).

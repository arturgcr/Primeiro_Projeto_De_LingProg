# Primeiro_Projeto_De_LingProg

---

## Descrição do Projeto

## Padrão de Commit
Utilizamos tipos de commit para padronizar as mensagens de commit neste projeto. A seguir, estão os tipos de commit a serem utilizados, juntamente com exemplos de sumários correspondentes:

### ADD
Use o tipo "ADD" quando estiver adicionando um novo recurso ou funcionalidade ao código.

Exemplo:
```
"Adiciona funcionalidade de autenticação de usuário"
```

### DROP
O tipo "DROP" é usado para indicar a remoção de um recurso ou funcionalidade do código.

Exemplo:
```
"Remove o módulo de gráficos legados"
```

### FIX
Utilize "FIX" ao realizar correções de bugs e resolver problemas.

Exemplo:
```
"Corrige o erro de formatação na página de perfil do usuário"
```

### BUILD
O tipo "BUILD" é usado quando você atualiza dependências ou realiza alterações nas características de compilação do projeto.

Exemplos:
```
"Atualiza as dependências do servidor de produção"
"Altera as configurações de compilação para suportar a nova biblioteca"
```

### REFACTOR
Use "REFACTOR" quando estiver realizando refatorações no código, melhorando sua estrutura ou desempenho sem alterar sua funcionalidade.

Exemplo:
```
"Refatora a classe de manipulação de dados para melhorar a legibilidade"
```

### DOCS
O tipo "DOCS" é aplicado a alterações relacionadas à documentação, como adição ou atualização de comentários no código ou no README.

Exemplo:
```
"Adiciona documentação de código para o método de autenticação"
```

### STYLE
Utilize o tipo "STYLE" para alterações que afetam apenas o estilo visual do código, como formatação ou estilos de código.

Exemplo:
```
"Melhora a formatação do código de acordo com as diretrizes de estilo"
```

## Modelo de Branchs Neste Projeto
Neste projeto, estamos adotando o GitFlow como nosso modelo de fluxo de trabalho para gerenciar o desenvolvimento e a entrega de software de forma eficiente e organizada.

### Ramificações Principais
- **Master**: A ramificação "master" é a principal linha de desenvolvimento. Ela contém apenas versões estáveis e testadas do software.

- **Develop**: A ramificação "develop" é onde o desenvolvimento ativo ocorre. Todas as novas funcionalidades e correções de bugs são implementadas aqui.

### Ramificações de Recursos
- **Feature**: Ramificações "feature" são criadas a partir de "develop" e são usadas para desenvolver novas funcionalidades ou melhorias. Quando a funcionalidade estiver pronta, ela é mesclada de volta para "develop".

# Lista de Tarefas CLI

Este é um simples gerenciador de lista de tarefas feito em Python, com interface de linha de comando (CLI). Ele permite que os usuários adicionem, visualizem, atualizem, completem e excluam tarefas de uma lista.

## Funcionalidades

- Adicionar uma nova tarefa
- Visualizar a lista de tarefas
- Atualizar o nome de uma tarefa existente
- Marcar uma tarefa como concluída
- Excluir todas as tarefas concluídas

## Como Usar

1. **Clonar o Repositório:**

   ```bash
   git clone https://github.com/taciodev/gerenciador-lista-de-tarefas.git
   ```
   
2. **Criar e Ativar um Ambiente Virtual (opcional):**

   ```bash
   python -m venv venv
   source venv/bin/activate # No Windows: venv\Scripts\activate
   ```

3. **Executar o Programa:**

   ```bash
   python main.py
   ```
   
4. **Interagir com a Aplicação:** Siga as instruções na interface de linha de comando para realizar as operações desejadas na lista de tarefas.

## Exemplos de Uso

- Adicionar uma nova tarefa:

  ```python
  Qual a sua escolha: 1
  Digite o nome da tarefa que deseja adicionar: Comprar leite
  ```

  - Atualizar o nome de uma tarefa existente:

  ```python
  Qual a sua escolha: 3
  1 - [ ] Comprar leite
  Digite o número da tarefa que deseja atualizar: 1
  Digite o novo nome da tarefa: Comprar pão
  ```

- Marcar uma tarefa como concluída:

  ```python
  Qual a sua escolha: 4
  1 - [ ] Comprar pão
  Digite o número da tarefa que deseja completar: 1
  ```

## Contribuindo

Contribuições são bem-vindas! Se você tiver sugestões de melhorias, abra uma issue para discutir suas ideias ou envie um pull request com suas alterações.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT). Sinta-se à vontade para usar, modificar e distribuir o código conforme necessário.

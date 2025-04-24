# 📘 Diário de Bordo – MsiczzBOT

> Última atualização: 22/04/2025
> Autor: Jonathas Uallace Macedo Santos
> Status: 🌀 Em andamento

---

## 📅 Dia 1

### ✅ Feito hoje:
- Projeto criado
- Adicionadas dependências ([python-telegram-bot](https://docs.python-telegram-bot.org/en/stable/), [pytubefix](https://pytubefix.readthedocs.io/en/latest/), [pytest](https://docs.pytest.org/en/stable/))
- Adicionado arquivos `src/bot.py` e `src/config.py`, para configuração de váriaveis de ambiente + inicialização do bot

### 🧭 Próximos passos:
- Criar os primeiros comandos básicos do bot (start e help)

---

## 📅 Dia 2

### ✅ Feito hoje:
- Adicionado arquivo `pytest.ini` para definir o caminho dos arquivos que serão testados.
- Criada a função de registro de comandos `utils/register.py`, que retorna nome (identificador), função e descrição do mesmo.
- Criado os comandos de start e help.
- Criados testes para a função de registro de comandos `utils/register.py::register_command()`.

### 🎯 Aprendizados e desafios

#### 📦 Geral
- Mesmo que o Python não seja uma linguagem tipada, "tipar" variáveis, parâmetros e retornos pode facilitar a manutenção do código pelo fato de aumentar a compreensão.

#### 🧪 Pytest
- Para rodar testes importando funções de outras pastas/diretórios com o `pytest`, é necessário definir um pythonpath para que o programa saiba onde buscar os recursos. Por isso, é bom adicionar um arquivo de configuração na raiz do projeto, `pytest.ini`, e definir as variáveis de configuração lá.
- Para ver saídas como `print()` a partir de testes, é necessário usar a flag `-s`.
- Para rodar teste específico dentro de um arquivo de testes devemos usar a sintaxe: `pytest nome_do_arquivo.py::nome_da_funcao`.

### 🧭 Próximos passos:
- Definir categorias para os comandos.
- Automatizar adição de handlers de comando com base em suas respectivas categorias.
- Automatizar conteúdo do comando de help.

---

## 📅 Dia 3

### ✅ Feito hoje:
- Adicionadas categorias ao agrupamento de comandos.
- Automatizado a adição do handler dos comandos com base em suas respectivas categorias.
- Automatizado conteúdo do comando `help`.

### 🎯 Aprendizados e desafios

#### 📦 Geral
- É possível retornar o valor de uma chave, dentro de um dicionário que esteja dentro de um array utilizando a seguinte sintaxe: `[item['chave'] for item in array]`, o que é bastante intuitivo, na verdade. Percebi que para entender e conseguir construir essa estrutura, devo dividir em duas partes: `[retorno iteracao_default_array]`

#### 📥 Importação Dinâmica
- Para trabalhar com importações dinâmicas devo utilizar `pkgutil: iter_modules`, `importlib: import_module` e `path: Path`
  - Para **encontrar** os módulos/arquivos desejados, devo utilizar a iteração do `pkgutil`
    ```js
    path = Path(__file__).parent
    for _, name, _ in iter_modules([str(path)]):
      print(name)
    ```
    A exemplo da pasta `commands/`, o print retornará cada módulo/arquivos presente na pasta em questão.<br>**OBS:** O `iter_modules` **não faz iteração recursiva**, ou seja, não acessa o conteúdo das pastas. Retorna apenas o "visível".

  - Para **importar** os módulos, utilizamos o `importlib`.
    ```js
    import_module('parent.child_module.file')
    ```
    Para importar é necessário seguir o padrão `parent.child_module.file`. A exemplo do `simple_command.py` teriamos algo como: `commands.simple.simple_command`

#### 📤 PPrint
- Módulo do Python que formata estruturas de dados mais **complexas**, de dificil visualização, como listas aninhadas, dicionários e objetos num geral.
  Exemplo:
  ```bash
    Saída com print():
    {'nome': 'John', 'idade': 19, 'interesses': ['Música', 'Programação', 'Games'], 'enderecos': [{'tipo': 'residencial', 'rua': 'Rua A', 'numero': 123}, {'tipo': 'comercial', 'rua': 'Avenida B', 'numero': 465}]}

    Saída com pprint():
    {'enderecos': [{'numero': 123, 'rua': 'Rua A', 'tipo': 'residencial'},
                   {'numero': 456, 'rua': 'Avenida B', 'tipo': 'comercial'}]},
    'idade': 19,
    'interesses': ['Música', 'Programação', 'Games'],
    'nome': 'John'}
  ```

### 🧭 Próximos passos:
- Adicionar comando para baixar música.
  - As músicas após baixadas devem ser armazenadas em uma pasta chamada `downloads/`
  - As músicas baixadas por usuário devem ficar salvas em uma pasta nomeada com o ID do usuário `downloads/{user_id}`
  - Após o download e envio da música(s) a pasta com o ID do usuário deve ser deletada.

---

## 📅 Dia 4

### ✅ Feito hoje:

### 🎯 Aprendizados e desafios

#### Geral

#### 🗃️ Biblioteca os
- Biblioteca para manipulação de diretórios, arquivos e OS.
- Comandos comuns:
  - **Diretórios e arquivos**
    - `os.curdir`: retorna o diretório atual `.`
      - usado geralmente com o `os.path.join()`
    - `os.getcwd()`: retorna o caminho absoluto do diretório atual
    - `os.mkdir()`: cria uma pasta
      - `os.makedirs()`: cria pastas recursivamente
    - `os.rmdir()`: deleta uma pasta
    - `os.remove()`: deleta um arquivo
  - **Caminhos**
    - `os.path.join()`: retorna um caminho juntando os parâmetros passados
    - `os.path.isdir()`: verifica se o caminho passado é um diretório existe (**apenas diretórios**)
    - `os.path.exists()`: verifica se o caminho/arquivo existe

#### ✂️ Biblioteca re

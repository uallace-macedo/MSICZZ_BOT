# 📘 Diário de Bordo – MsiczzBOT

> Última atualização: 30/04/2025
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
- Adicionado comando para baixar música.
  - As músicas são armazenadas em uma pasta `downloads/`
  - As músicas baixadas ficam salvas em uma pasta nomeada com o ID do usuário
  - Após o download e envio da música, a pasta com o ID é deletada

- Adicionados comandos para criação e exclusão de pastas com `os`
- Adicionados comandos com `regex` e `unidecode` para formatação de textos (titulos e extração de URL)


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

- **Adicional** `shutil`
  - Biblioteca utilizada para apagar pastas e conteúdos internos sem necessidade de esvaziar a pasta primeiro
    ```js
    if os.path.exists(folder_path):
    shutil.rmtree(folder_path)
    ```

#### ✂️ Biblioteca re
- Expressões regulares (regex) são padrões que descrevem **conjuntos de strings**
- Utilizamos `re` para procurar, validar, substituir ou extrair partes de texto que seguem um determinado padrão

- **Raw string**: r'\t'

**Caracteres especiais**:
  - *Correspondências*:
    - `.`: qualquer caracter com exceção de nova linha
    - `\d`: digitos (0-9)
    - `\D`: não é um digito que se encaixe no `\d`
    - `\w`: caracteres (a-z, A-Z, 0-9, _)
    - `\W`: não é um caracter que se encaixe no `\w`
    - `\s`: espaço em branco (espaço, tab, nova linha)
    - `\S`: não é espaço em branco (espaço, tab, nova linha)

  - *Âncoras*:
    - `\b`: limite da palavra (espaço em branco ou caractere não-alfanumérico) [o "word boundary", precisa estar antes]
    - `\B`: não tem um limitador ("word boundary") antes dele
    - `^`: Inicio de uma string
    - `$`: Fim de uma string

  - *Agrupadores*:
    - `[]`: caracteres específicos. [apenas um digito é levado em consideração]
    - `-`: define um range
    - `[^]`: nega o que estiver dentro dos colchetes
    - `|`: ou
    - `()`: grupo

  - *Quantificadores:*
    - `*`: 0+
    - `+`: 1+
    - `?`: 0 ou 1
    - `{3}`: número exato
    - `{3,4}`: range (minimo, máximo)

- **Adicional** `unicode`: transforma caracteres com acento para sem acento

### 🧭 Próximos passos:
- Adicionar feedback (mensagem) ao download de música
- Adicionar tratamento de erros ao comando de baixar músicas
- Adicionar comando para download de playlist

---

## 📅 Dia 5

### ✅ Feito hoje:
- Adicionado feedback ao download da música
- Adicionados tratamento de erros ao comando de baixar músicas
- Adicionado `download_music` ao `utils`, para evitar repetição e aumentar reusabilidade de código
- Adicionado comando `download_playlist`
- Adicionada pasta `downloads/zips` para centralizar arquivos zip (playlists)
- Adicionado `zip_file` ao `utils` para zipar playlists baixadas, evitando spam ao enviar a playlist para o usuário
- Removida função para limpar títulos, pois o Telegram tem bom suporte a uma vasta gama de caracteres.

### 🎯 Aprendizados e desafios

#### Geral

#### 📁 Zipfile

- Parâmetros comuns:
  - `zf.write(filename, arcname)`
    - `filename`: caminho para o arquivo
    - `arcname`: nome do arquivo quando zipado

- Para zipar um arquivo
  ```js
  import os
  from zipfile import ZipFile, ZIP_DEFLATED

  pasta_destino: str = os.path.join(os.curdir, 'pasta_destino', 'nome_zip.zip')
  referencia_zip: ZipFile = ZipFile(pasta_destino, 'w', compression=ZIP_DEFLATED)
  path_arquivo_toZIP: str = os.path.join(os.curdir, 'arquivo.py')

  referencia_zip.write(path_arquivo_toZIP, 'nome-zip')
  referencia_zip.close()
  ```

- Para zipar vários arquivos
  ```js
  import os
  from zipfile import ZipFile, ZIP_DEFLATED

  def compactar_tudo(diretorio):
    arquivos = os.listdir(diretorio)

    for arquivo in arquivos:
      archive_name: str = arquivo[0:arquivo.rfind('.')]
      destiny: str = os.path.join(os.curdir, 'musics', f'{archive_name}.zip')
      zip_reference: ZipFile = ZipFile(destiny, 'w', compression=ZIP_DEFLATED)
      zip_reference.write(os.path.join(diretorio, arquivo), arquivo)
      zip_reference.close()

    return len(arquivos)

  if __name__ == '__main__':
    pasta = input('Digite o endereço da pasta a ser compactada (com "/" para subdiretorios): ')
    pasta = pasta.strip().split('/')

    final_path: str = os.path.join(*pasta)
    amount = compactar_tudo(final_path)
    print(f'Arquivos compactados: {amount}.')
  ```

- Para zipar pasta + subpastas
  ```js
  import os
  from zipfile import ZipFile, ZIP_DEFLATED

  def zip_folder(directory, zip_name):
    with ZipFile(zip_name, 'w', compression=ZIP_DEFLATED) as zf:
      for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
          full_path: str = os.path.join(dirpath, filename)
          relative_path: str = os.path.relpath(full_path, directory)

          zf.write(full_path, relative_path)

  if __name__ == '__main__':
    folder: str = str(input('Digite o path (com "/" para subdiretorios): '))
    name: str = str(input('Digite o nome do zip: '))

    if not name.endswith('.zip'):
      name = name + '.zip'

    zip_folder(folder, name)
  ```

#### 🗺️ os.walk

Função do módulo `os` que varre (recursivamente) todos os diretórios e arquivos a partir de uma pasta inicial

Gera uma tupla com: `dirpath`, `dirnames` e `filenames`

```js
for dirpath, dirnames, filenames in os.walk('caminho_inicial'):
```

- `dirpath`: o caminho atual (string) da pasta que está sendo visitada.
- `dirnames`: lista com os nomes das subpastas dentro de `dirpath`
- `filenames`: lista com os nomes dos arquivos dentro de `dirpath`
- `os.path.relpath()`: retorna a "diferença" entre os parâmetros

### 🧭 Próximos passos:
- Adicionar explicação detalhada de comando `/help command`
- Adicionar possibilidade de adicionar várias músicas fora de uma playlist

---

# 📘 Diário de Bordo – MsiczzBOT

> Última atualização: 14/04/2025
> Autor: Jonathas Uallace Macedo Santos
> Status: 🌀 Em andamento

---

## 📅 13/04/2025

### ✅ Feito hoje:
- Projeto criado
- Adicionadas dependências ([python-telegram-bot](https://docs.python-telegram-bot.org/en/stable/), [pytubefix](https://pytubefix.readthedocs.io/en/latest/), [pytest](https://docs.pytest.org/en/stable/))
- Adicionado arquivos `src/bot.py` e `src/config.py`, para configuração de váriaveis de ambiente + inicialização do bot

### 🧭 Próximos passos:
- Criar os primeiros comandos básicos do bot (start e help)

---

## 📅 14/04/2025

### ✅ Feito hoje:
- Adicionado arquivo `pytest.ini` para definir o caminho dos arquivos que serão testados
- Criada a função de registro de comandos `utils/register.py`, que retorna nome (identificador), função e descrição do mesmo.
- Criado os comandos de start e help.
- Criados testes para a função de registro de comandos `utils/register.py::register_command()`

### 🎯 Aprendizados e desafios

#### 📦 Geral
- Mesmo que o Python não seja uma linguagem tipada, "tipar" variáveis, parâmetros e retornos pode facilitar a manutenção do código pelo fato de aumentar a compreensão.

#### 🧪 Pytest
- Para rodar testes importando funções de outras pastas/diretórios com o `pytest`, é necessário definir um pythonpath para que o programa saiba onde buscar os recursos. Por isso, é bom adicionar um arquivo de configuração na raiz do projeto, `pytest.ini`, e definir as variáveis de configuração lá.
- Para ver saídas como `print()` a partir de testes, é necessário usar a flag `-s`.
- Para rodar teste específico dentro de um arquivo de testes devemos usar a sintaxe: `pytest nome_do_arquivo.py::nome_da_funcao`

### 🧭 Próximos passos:
- Definir categorias para os comandos
- Automatizar adição de handlers de comando com base em suas respectivas categorias
- Automatizar conteúdo do comando de help

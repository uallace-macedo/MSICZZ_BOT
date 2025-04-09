from .markdown import escape_markdown

def generate_help_text(commands_by_category: dict[str, list[dict[str, str]]]) -> str:
    """
    Gera mensagem de ajuda formatada para Telegram com MarkdownV2.

    Args:
      commands_by_category (dict):
        - Chaves no formato ":emoji: Categoria"
        - Valores são listas de dicionários no formato {"/comando": "descrição"}

      Exemplo:
      {
          "📌 Geral": [
            {"/start": "Inicia o bot"},
            {"/help": "Mostra esta mensagem de ajuda"}
          ],
          "🎵 Música": [
            {"/download": "Baixa uma música"},
            {"/playlist": "Baixa uma playlist"}
          ]
      }

    Returns:
      str: Texto formatado em MarkdownV2 pronto para envio.
    """
    lines = []

    for category, commands in commands_by_category.items():
      if not commands:
        continue

      lines.append(f"*{escape_markdown(category)}*")

      for cmd in commands:
        for name, desc in cmd.items():
          escaped_name = escape_markdown(name)
          escaped_desc = escape_markdown(desc)
          lines.append(f"`{escaped_name}` \\- {escaped_desc}")

      lines.append('')

    return '\n'.join(lines).strip()

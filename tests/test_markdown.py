from src.utils.markdown import escape_markdown

def test_escape_markdown_basic():
  text = "comando - descrição"
  escaped = escape_markdown(text)
  assert escaped == "comando \\- descrição"

def test_escape_markdown_full():
  text = "comando_1 *bold* [link](url) ~strike~"
  escaped = escape_markdown(text)
  assert escaped == (
    "comando\\_1 \\*bold\\* \\[link\\]\\(url\\) \\~strike\\~"
  )

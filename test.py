from ruamel.yaml import YAML
from io import StringIO

document = """
ingress:
  tls:
    # comment
    []

persistence:
  enabled: true
"""

yaml = YAML()
content = yaml.load(document)
output = StringIO()
yaml.dump(content, output)

formatted = output.getvalue()
print(formatted)

second = yaml.load(formatted)

assert content == second

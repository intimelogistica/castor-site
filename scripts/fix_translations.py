import re
from pathlib import Path
from bs4 import BeautifulSoup

base = Path(r"C:\Users\João Batista\castor-site\frontend\prototypes")
files = [
    "v2-versao-a-premium.html",
    "v2-versao-b-catalogo.html",
    "v2-versao-c-conversao.html",
]

# Correcoes globais em todo o HTML (texto + atributos)
def fix_html(html, target):
    # 1. Reverter marca Castor (em EN foi traduzido para Beaver)
    html = re.sub(r'\bBeaver\b', 'Castor', html)

    # 2. Corrigir espacos perdidos entre palavras comuns
    html = re.sub(r'(?i)(Castor)([A-Z])', r'\1 \2', html)
    html = re.sub(r'(?i)(madeira|madera|wood)(em|en|de|do|da|dos|das|para|por|com|sem)\b', r'\1 \2', html)
    html = re.sub(r'(?i)(em|en|de|do|da|dos|das|para|por|com|sem)(Minas|Belo|Lagoa|Matozinhos|Brasil|MG|BH)', r'\1 \2', html)
    html = re.sub(r'(\d+(?:,\d+)?\s*m\²?)([a-zA-Z])', r'\1 \2', html)
    html = re.sub(r'(?i)(total|de area|de \u00e1rea|total area|\u00e1rea total)([a-zA-Z])', r'\1 \2', html)
    html = re.sub(r'(?i)(em|en)(Minas|MG|BH|Belo|Lagoa|Matozinhos)', r'\1 \2', html)

    # 3. Correcoes especificas de idioma
    if target == 'en':
        html = html.replace('Castor Wooden Houses', 'Castor Wood Houses')
        html = html.replace('Wooden houses in Minas Gerais', 'Wood houses in Minas Gerais')
        html = html.replace('wooden house builder', 'wood house builder')
        html = html.replace('Wooden Houses', 'Wood Houses')
        html = html.replace('Wooden houses', 'Wood houses')
        html = html.replace('wooden house', 'wood house')
    elif target == 'es':
        html = html.replace('CastorCasas de madera', 'Castor Casas de madera')
        html = html.replace('casas de madera enMinas', 'casas de madera en Minas')
        html = html.replace('constructora de casas de madera enMG', 'constructora de casas de madera en MG')

    return html

for target in ["en", "es"]:
    target_dir = base / target
    for filename in files:
        p = target_dir / filename
        html = p.read_text(encoding="utf-8")
        html = fix_html(html, target)
        p.write_text(html, encoding="utf-8")
        print(f"Corrigido: {p}")

print("Correcoes concluidas.")

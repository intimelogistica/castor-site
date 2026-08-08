import re
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag

base = Path(r"C:\Users\João Batista\castor-site\frontend\prototypes")
files = [
    "v2-versao-a-premium.html",
    "v2-versao-b-catalogo.html",
    "v2-versao-c-conversao.html",
]

def fix_spacing(soup):
    """Garante espaco entre nos de texto adjacentes sem espaco."""
    for tag in soup.find_all(True):
        children = list(tag.contents)
        for i in range(len(children) - 1):
            a, b = children[i], children[i+1]
            if isinstance(a, NavigableString) and isinstance(b, NavigableString):
                a_text = str(a)
                b_text = str(b)
                if a_text and b_text and not a_text[-1].isspace() and not b_text[0].isspace():
                    # Inserir espaco entre eles
                    a.replace_with(a_text + " ")

def fix_terms(html, target):
    # Correcoes especificas
    if target == "en":
        html = re.sub(r'CastorWood Houses', 'Castor Wood Houses', html)
        html = re.sub(r'Wood House Industry', 'Wood House Industry', html)
        html = re.sub(r'Wood houses inMinas', 'Wood houses in Minas', html)
        html = re.sub(r'Castor Indústria de Wood Houses Ltda', 'Castor Indústria de Casas de Madeira Ltda', html)
        html = re.sub(r'builder of wood houses', 'builder of wood houses', html)
        html = re.sub(r'Castor wood house', 'Castor wood house', html)
    elif target == "es":
        html = re.sub(r'CastorHogars de Madera', 'Castor Casas de Madera', html)
        html = re.sub(r'Hogars de madera', 'Casas de madera', html)
        html = re.sub(r'Hogars de Madera', 'Casas de Madera', html)
        html = re.sub(r'Industria de Hogars de Madera', 'Industria de Casas de Madera', html)
        html = re.sub(r'Hogars de madera enMinas', 'Casas de madera en Minas', html)
        html = re.sub(r'Castor Indústria de Casas de Madera Ltda', 'Castor Indústria de Casas de Madeira Ltda', html)

    # Correcoes genericas de espaco
    html = re.sub(r'(?<=[a-zA-Zà-ü])(?=[A-ZÀ-Ü][a-z])', ' ', html)
    html = re.sub(r'inMinas', 'in Minas', html)
    html = re.sub(r'enMinas', 'en Minas', html)
    html = re.sub(r'deMinas', 'de Minas', html)

    return html

for target in ["en", "es"]:
    target_dir = base / target
    for filename in files:
        p = target_dir / filename
        html = p.read_text(encoding="utf-8")
        soup = BeautifulSoup(html, "html.parser")
        fix_spacing(soup)
        html = str(soup)
        html = fix_terms(html, target)
        p.write_text(html, encoding="utf-8")
        print(f"Processado: {p}")

print("Concluido.")

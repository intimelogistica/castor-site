import re
from pathlib import Path

base = Path(r"C:\Users\João Batista\castor-site\frontend\prototypes")
files = [
    ("en", "v2-versao-a-premium.html"),
    ("en", "v2-versao-b-catalogo.html"),
    ("en", "v2-versao-c-conversao.html"),
    ("es", "v2-versao-a-premium.html"),
    ("es", "v2-versao-b-catalogo.html"),
    ("es", "v2-versao-c-conversao.html"),
]

for target, filename in files:
    p = base / target / filename
    html = p.read_text(encoding="utf-8")

    # Adicionar margem entre brand-name e brand-badge
    html = re.sub(
        r'(\.brand-badge\s*\{[^}]*margin-top:\s*3px;?)',
        r'\1\n    .brand-name + .brand-badge { margin-left: 6px; }',
        html,
        count=1
    )

    # Correcoes de espaco colado
    html = re.sub(r'inMinas', 'in Minas', html)
    html = re.sub(r'enMinas', 'en Minas', html)
    html = re.sub(r'deMinas', 'de Minas', html)
    html = re.sub(r'emMinas', 'em Minas', html)

    # Correcoes especificas de marca
    if target == "en":
        html = re.sub(r'CastorWood Houses', 'Castor Wood Houses', html)
        html = re.sub(r'Castor Wood Houses\|', 'Castor Wood Houses |', html)
    elif target == "es":
        html = re.sub(r'CastorCasas de Madera', 'Castor Casas de Madera', html)
        html = re.sub(r'CastorCasas de Madeira', 'Castor Casas de Madeira', html)
        html = re.sub(r'Hogars de Madera', 'Casas de Madera', html)
        html = re.sub(r'Hogars de madera', 'Casas de madera', html)

    p.write_text(html, encoding="utf-8")
    print(f"Ajustado: {p}")

print("Concluido.")

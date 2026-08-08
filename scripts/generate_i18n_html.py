import json
import html as html_module
import re
from pathlib import Path

base = Path(r"C:\Users\João Batista\castor-site\frontend\prototypes")
cache_file = base / ".translation_cache.json"

files = [
    "v2-versao-a-premium.html",
    "v2-versao-b-catalogo.html",
    "v2-versao-c-conversao.html",
]

cache = json.loads(cache_file.read_text(encoding="utf-8"))

def escape_for_regex(s):
    return re.escape(s)

def translate_html(html, target):
    # Ajustar lang
    html = re.sub(r'<html[^>]*>', f'<html lang="{target}">', html, count=1)

    # Preparar substituicoes ordenadas do maior para o menor texto
    items = sorted(cache[target].items(), key=lambda x: len(x[0]), reverse=True)

    # Substituir textos fora de tags <style> e <script>
    # Abordagem: processar o HTML em partes
    parts = []
    last = 0
    for m in re.finditer(r'<(style|script)[^>]*>.*?</\1>', html, flags=re.DOTALL | re.IGNORECASE):
        parts.append(("text", html[last:m.start()]))
        parts.append(("skip", m.group()))
        last = m.end()
    parts.append(("text", html[last:]))

    result = []
    for kind, segment in parts:
        if kind == "skip":
            result.append(segment)
            continue
        for src, dst in items:
            # Evitar substituir dentro de tags (aproximacao: so fora de < >)
            # Fazer substituicao global no segmento
            segment = segment.replace(src, dst)
        result.append(segment)

    return "".join(result)

def add_language_bar(html, target, filename):
    if target == "pt":
        pt_link, en_link, es_link = filename, f"en/{filename}", f"es/{filename}"
    elif target == "en":
        pt_link, en_link, es_link = f"../{filename}", filename, f"../es/{filename}"
    else:
        pt_link, en_link, es_link = f"../{filename}", f"../en/{filename}", filename

    bar = f'''<div id="lang-bar" style="position:fixed;top:0;left:0;right:0;z-index:9999;background:#29241c;color:#faf6ef;font-family:system-ui,sans-serif;font-size:13px;padding:8px 16px;display:flex;justify-content:center;gap:16px;align-items:center;">
  <span style="opacity:.8;">Idioma / Language / Idioma:</span>
  <a href="{pt_link}" style="color:{'#b8ac97' if target=='pt' else '#faf6ef'};text-decoration:none;font-weight:600;">PT-BR</a>
  <a href="{en_link}" style="color:{'#b8ac97' if target=='en' else '#faf6ef'};text-decoration:none;font-weight:600;">EN</a>
  <a href="{es_link}" style="color:{'#b8ac97' if target=='es' else '#faf6ef'};text-decoration:none;font-weight:600;">ES</a>
</div>
<div style="height:36px;"></div>
'''
    # Inserir logo apos <body...>
    html = re.sub(r'(<body[^>]*>)', r'\1\n' + bar, html, count=1)
    # Adicionar estilo hover
    style = '<style>#lang-bar a:hover{text-decoration:underline;}</style>'
    html = re.sub(r'(</head>)', style + r'\1', html, count=1)
    return html

for target in ["en", "es"]:
    target_dir = base / target
    target_dir.mkdir(exist_ok=True)
    for filename in files:
        html = (base / filename).read_text(encoding="utf-8")
        html = translate_html(html, target)
        html = add_language_bar(html, target, filename)
        out_path = target_dir / filename
        out_path.write_text(html, encoding="utf-8")
        print(f"Gerado: {out_path}")

print("Concluido.")

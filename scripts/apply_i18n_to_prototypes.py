import json
import re
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag

base = Path(r"C:\Users\João Batista\castor-site\frontend\prototypes")
cache_file = base / ".translation_cache.json"

files = [
    "v2-versao-a-premium.html",
    "v2-versao-b-catalogo.html",
    "v2-versao-c-conversao.html",
]

if not cache_file.exists():
    raise FileNotFoundError("Cache de traducao nao encontrado. Rode translate_prototypes.py primeiro.")

cache = json.loads(cache_file.read_text(encoding="utf-8"))

def translate(key, target):
    key = key.strip()
    if key in cache[target]:
        return cache[target][key]
    return key

# Atributos que devem ser traduzidos
TRANS_ATTRS = {"content", "alt", "placeholder", "title", "aria-label"}

for target in ["en", "es"]:
    target_dir = base / target
    target_dir.mkdir(exist_ok=True)
    for filename in files:
        html = (base / filename).read_text(encoding="utf-8")
        soup = BeautifulSoup(html, "html.parser")

        # Ajustar lang
        if soup.html:
            soup.html["lang"] = target

        # Traduzir textos nos nos
        for node in soup.find_all(string=True):
            if isinstance(node, NavigableString):
                original = str(node)
                stripped = original.strip()
                if stripped in cache[target]:
                    new_text = original.replace(stripped, cache[target][stripped])
                    node.replace_with(new_text)

        # Traduzir atributos
        for tag in soup.find_all(True):
            for attr in TRANS_ATTRS:
                if attr in tag.attrs and isinstance(tag.attrs[attr], str):
                    val = tag.attrs[attr]
                    stripped = val.strip()
                    if stripped in cache[target]:
                        tag.attrs[attr] = cache[target][stripped]

        # Seletor de idioma
        if target == "pt":
            pt_link = filename
            en_link = f"en/{filename}"
            es_link = f"es/{filename}"
        elif target == "en":
            pt_link = f"../{filename}"
            en_link = filename
            es_link = f"../es/{filename}"
        else:  # es
            pt_link = f"../{filename}"
            en_link = f"../en/{filename}"
            es_link = filename

        lang_bar_html = f'''
        <div id="lang-bar" style="position:fixed;top:0;left:0;right:0;z-index:9999;background:#29241c;color:#faf6ef;font-family:system-ui,sans-serif;font-size:13px;padding:8px 16px;display:flex;justify-content:center;gap:16px;align-items:center;">
          <span style="opacity:.8;">Idioma / Language / Idioma:</span>
          <a href="{pt_link}" style="color:{'#b8ac97' if target=='pt' else '#faf6ef'};text-decoration:none;font-weight:600;">PT-BR</a>
          <a href="{en_link}" style="color:{'#b8ac97' if target=='en' else '#faf6ef'};text-decoration:none;font-weight:600;">EN</a>
          <a href="{es_link}" style="color:{'#b8ac97' if target=='es' else '#faf6ef'};text-decoration:none;font-weight:600;">ES</a>
        </div>
        <div style="height:36px;"></div>
        '''
        lang_bar = BeautifulSoup(lang_bar_html, "html.parser")

        # Inserir logo no inicio do body
        body = soup.find("body")
        if body:
            body.insert(0, lang_bar)
            style = soup.new_tag("style")
            style.string = "#lang-bar a:hover{text-decoration:underline;}"
            head = soup.find("head")
            if head:
                head.append(style)
        else:
            # Fallback: inserir antes do conteudo
            print(f"AVISO: body nao encontrado em {filename}")

        out_path = target_dir / filename
        out_path.write_text(str(soup), encoding="utf-8")
        print(f"Gerado: {out_path}")

print("Concluido.")

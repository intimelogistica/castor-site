import json
import time
import re
import sys
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString
from deep_translator import GoogleTranslator

base = Path(r"C:\Users\João Batista\castor-site\frontend\prototypes")
cache_file = base / ".translation_cache.json"

files = {
    "v2-versao-a-premium.html": "versao-a-premium",
    "v2-versao-b-catalogo.html": "versao-b-catalogo",
    "v2-versao-c-conversao.html": "versao-c-conversao",
}

if cache_file.exists():
    cache = json.loads(cache_file.read_text(encoding="utf-8"))
else:
    cache = {"en": {}, "es": {}}

def save_cache():
    cache_file.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")

def translate_text(text, target):
    key = text.strip()
    if key in cache[target]:
        return cache[target][key]
    try:
        translator = GoogleTranslator(source="pt", target=target)
        translated = translator.translate(key)
        cache[target][key] = translated
        return translated
    except Exception as e:
        print(f"ERRO {target}: {repr(key[:60])}: {e}", file=sys.stderr)
        return key

# Extrair textos
all_texts = set()
for filename in files:
    html = (base / filename).read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")
    for text in soup.stripped_strings:
        t = text.strip()
        if len(t) > 1 and not t.startswith("http") and not t.isdigit() and not re.match(r"^#[0-9a-fA-F]{6}$", t):
            all_texts.add(t)

print(f"Total textos unicos: {len(all_texts)}")

BATCH = 30
for target in ["en", "es"]:
    missing = [t for t in all_texts if t not in cache[target]]
    print(f"[{target}] pendentes: {len(missing)}")
    for i in range(0, len(missing), BATCH):
        batch = missing[i:i+BATCH]
        for text in batch:
            translate_text(text, target)
            time.sleep(0.3)
        save_cache()
        print(f"[{target}] {min(i+BATCH, len(missing))}/{len(missing)}")
        time.sleep(1)

print("Traducao concluida. Gerando HTMLs...")

# Funcao para substituir textos mantendo estrutura
for target in ["en", "es"]:
    target_dir = base / target
    target_dir.mkdir(exist_ok=True)
    for filename, slug in files.items():
        html = (base / filename).read_text(encoding="utf-8")
        soup = BeautifulSoup(html, "html.parser")

        # Substituir textos em nos de texto
        for node in soup.find_all(string=True):
            if isinstance(node, NavigableString):
                original = str(node).strip()
                if original in cache[target]:
                    new_text = cache[target][original]
                    node.replace_with(new_text)

        # Ajustar lang e title base
        if soup.html:
            soup.html["lang"] = target

        # Adicionar seletor de idioma no topo do body
        target_label = {"en": "EN", "es": "ES", "pt": "PT-BR"}[target]
        pt_link = f"../{filename}"
        en_link = f"en/{filename}" if target != "en" else filename
        es_link = f"es/{filename}" if target != "es" else filename
        if target == "en":
            pt_link = f"../{filename}"
            en_link = filename
            es_link = f"../es/{filename}"
        elif target == "es":
            pt_link = f"../{filename}"
            en_link = f"../en/{filename}"
            es_link = filename
        else:
            pt_link = filename
            en_link = f"en/{filename}"
            es_link = f"es/{filename}"

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
        if soup.body:
            soup.body.insert(0, lang_bar)
            style = soup.new_tag("style")
            style.string = "#lang-bar a:hover{text-decoration:underline;}"
            if soup.head:
                soup.head.append(style)

        out_path = target_dir / filename
        out_path.write_text(str(soup), encoding="utf-8")
        print(f"Gerado: {out_path}")

print("Concluido.")

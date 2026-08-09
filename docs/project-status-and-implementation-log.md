# Registro de Implementação — Castor Casas de Madeira

> Documento de continuidade técnica. Resume tudo o que foi produzido desde o SPEC até o estado atual do projeto.
> 
> Última atualização: 2026-08-08
> Projeto: `intime-castor` / `castor-site`
> Repositório: https://github.com/intimelogistica/castor-site
> Site publicado (protótipos): https://intimelogistica.github.io/castor-site/frontend/prototypes/

---

## 1. Visão geral do projeto

**Objetivo:** substituir o site atual da Castor (`casademadeira.com.br`), atualmente em WordPress comprometido (backdoor, Elementor desatualizado, SEO inexistente), por uma stack moderna baseada no site da InTime.

**Stack definida:**
- Frontend: Next.js 16 + App Router + React 19 + TypeScript + Tailwind CSS v4
- UI: shadcn/ui + componentes customizados
- CMS: Strapi 5.50 com plugin i18n
- Banco: PostgreSQL (produção) / SQLite (dev)
- Mídia: Cloudinary
- Email: Resend
- Anti-spam: Cloudflare Turnstile
- Analytics: GA4 + GTM + Consent Mode v2 + Vercel Analytics
- CRM de leads: Notion (via Server Action)
- Deploy: Vercel
- Domínio: `casademadeira.com.br`

**Idiomas de lançamento:** Português (pt-BR), Inglês (en), Espanhol (es).

---

## 2. Documentação estratégica criada

| Arquivo | Descrição | Status |
|---|---|---|
| `docs/castor-site-plano-fases.md` | Plano estratégico com 7 fases (FASE 0 a FASE 7), stack, diagnóstico do site atual, análise competitiva e próximos passos | Atualizado com i18n |
| `planning/information-architecture.md` | Mapa de páginas, taxonomia de modelos, keyword map e componentes principais | Base |
| `planning/model-fields-mapping.md` | Mapeamento completo de campos do Strapi para `house-model` e content-types auxiliares (`category`, `wood-type`, `roof-type`, `window-type`, `faq`) | Base |
| `planning/internationalization-strategy.md` | Estratégia de i18n: subdiretórios (`/pt/`, `/en/`, `/es/`), middleware Next.js, Strapi i18n, hreflang, sitemaps, tradução de conteúdo | Criado |
| `planning/i18n-glossary.md` | Glossário técnico pt/en/es para termos do nicho, navegação, CTAs e slugs | Criado |
| `planning/github-references.md` | Repositórios de referência visual/UX organizados por direção (Premium, Catálogo, Conversão) | Base |
| `planning/skills-ux-ui-analysis.md` | Análise de skills e padrões de UX/UI | Base |
| `docs/project-status-and-implementation-log.md` | Este documento | Criado |

---

## 3. Pesquisa e dados coletados

Pasta `research/`:
- `relatorio_concorrentes_casas_madeira_mg.md` — análise de 10 concorrentes do nicho casas de madeira/MG
- `competitor-model-urls.json` — URLs dos modelos dos concorrentes
- Arquivos HTML salvos de concorrentes (Madecasa, Chalé de Madeira, etc.)
- `castor-models-fields.json` — extração dos campos dos 47 modelos do site atual Castor
- `castor-models.tar.gz` — backup comprimido do conteúdo original
- `modelo-castor-brasil.html` — exemplo de página de modelo
- Pastas `casa-de-madeira-modelo-*/` — páginas individuais de modelos
- `chale-products-list.json`, `chale_lista_de_produtos.html` — dados do concorrente Chalé

**Conteúdo original do site Castor:**
- ~55 modelos de casa extraídos do WordPress antigo
- Faixa de área total: 103,13 m² a 306,55 m²
- Estrutura padrão: área coberta, área da varanda, área total, quartos, suítes, banheiros, lavanderia, cozinha americana, varanda, galeria de imagens

---

## 4. Protótipos de layout

Pasta `frontend/prototypes/`.

### 4.1 Versões da 1ª rodada
- `versao-a-premium.html`
- `versao-b-catalogo.html`
- `versao-c-conversao.html`

### 4.2 Versões da 2ª rodada (atuais)
- `v2-versao-a-premium.html` — Premium/Institucional (Fraunces + Karla)
- `v2-versao-b-catalogo.html` — Catálogo/Visual (Fraunces + Archivo, filtros funcionais)
- `v2-versao-c-conversao.html` — Conversão/Agressiva (Fraunces + Work Sans, formulário + WhatsApp)
- `index.html` — hub com links para as 3 versões

### 4.3 Internacionalização dos protótipos
Cada protótipo v2 possui versões em pt, en e es:
- `frontend/prototypes/index.html` (pt)
- `frontend/prototypes/en/index.html` + `en/v2-versao-*.html`
- `frontend/prototypes/es/index.html` + `es/v2-versao-*.html`

Todos incluem uma barra fixa de seleção de idioma com links PT-BR | EN | ES.

### 4.4 Características técnicas dos protótipos
- HTML5 standalone, sem build/instalação
- Mobile-first, CSS custom properties (design tokens)
- Google Fonts carregadas via CDN
- Imagens dos modelos carregadas do site atual (`casademadeira.com.br`)
- Links relativos entre páginas (`href="v2-versao-a-premium.html"`)
- Meta tags SEO básicas (title, description, og:*)
- Filtros funcionais na versão B (JavaScript puro)
- Formulário com envio para WhatsApp na versão C

---

## 5. Internacionalização (i18n) — implementação técnica

### 5.1 Estratégia de URL
- Subdiretórios por idioma: `/pt/`, `/en/`, `/es/`
- Raiz `/` redireciona conforme `accept-language` ou serve como `x-default`
- Sitemaps separados por idioma
- hreflang cruzado em todas as páginas

### 5.2 Arquivos de dicionário UI
Pasta `frontend/i18n/`:
- `pt.json` — UI em português
- `en.json` — UI em inglês
- `es.json` — UI em espanhol
- `getDictionary.ts` — loader com `server-only`, tipagem e validação de locale

Dicionários cobrem: meta, nav, localeSwitcher, home, model, contact, cookieConsent, footer.

### 5.3 Tradução dos protótipos
Foi feita via Google Translate (biblioteca `deep-translator`) com pós-processamento manual para:
- Manter "Castor" como nome próprio da marca
- Corrigir termos técnicos ("wood house", "casa de madera")
- Ajustar espaçamento entre elementos inline
- Adicionar seletor de idioma

Cache de tradução: `frontend/prototypes/.translation_cache.json` (360 entradas EN, 353 ES).

### 5.4 Scripts de tradução
Pasta `scripts/`:
- `translate_prototypes.py` — extrai textos, traduz via Google Translate e salva cache
- `apply_i18n_to_prototypes.py` — aplica cache com BeautifulSoup (não usado na versão final)
- `generate_i18n_html.py` — gera HTMLs en/es usando string replacement e adiciona lang bar
- `post_process_i18n.py` — ajusta espaçamento entre nós de texto
- `fix_translations.py` — correções de termos e espaços
- `final_i18n_adjustments.py` — ajustes finais de CSS e marca

---

## 6. Estrutura do repositório

```
castor-site/
├── brand/
│   └── README.md              # checklist de identidade visual (pendente)
├── cms/                       # (vazio — Strapi a ser configurado)
├── docs/
│   ├── castor-site-plano-fases.md
│   └── project-status-and-implementation-log.md  (este arquivo)
├── frontend/
│   ├── i18n/                  # dicionários pt/en/es + loader
│   │   ├── pt.json
│   │   ├── en.json
│   │   ├── es.json
│   │   └── getDictionary.ts
│   └── prototypes/            # protótipos HTML
│       ├── index.html         # hub pt
│       ├── v2-versao-a-premium.html
│       ├── v2-versao-b-catalogo.html
│       ├── v2-versao-c-conversao.html
│       ├── en/                # versões em inglês
│       │   ├── index.html
│       │   ├── v2-versao-a-premium.html
│       │   ├── v2-versao-b-catalogo.html
│       │   └── v2-versao-c-conversao.html
│       ├── es/                # versões em espanhol
│       │   ├── index.html
│       │   ├── v2-versao-a-premium.html
│       │   ├── v2-versao-b-catalogo.html
│       │   └── v2-versao-c-conversao.html
│       └── .translation_cache.json
├── planning/
│   ├── information-architecture.md
│   ├── model-fields-mapping.md
│   ├── internationalization-strategy.md
│   ├── i18n-glossary.md
│   ├── github-references.md
│   └── skills-ux-ui-analysis.md
├── research/                  # pesquisas, concorrentes, conteúdo original
├── scripts/                   # automações de tradução e geração
├── index.html                 # redirect local para /frontend/prototypes/
├── README.md
└── Stackinfraestrutura Proposta Castor.txt
```

---

## 7. Publicação web

### 7.1 GitHub Pages
- Repositório: `intimelogistica/castor-site` (público)
- Branch: `main`
- Source: raiz (`/`)
- Workaround para subpasta: `.nojekyll` + `index.html` na raiz com meta-refresh para `/frontend/prototypes/`

### 7.2 URLs publicadas
- Hub: https://intimelogistica.github.io/castor-site/frontend/prototypes/
- PT:
  - https://intimelogistica.github.io/castor-site/frontend/prototypes/v2-versao-a-premium.html
  - https://intimelogistica.github.io/castor-site/frontend/prototypes/v2-versao-b-catalogo.html
  - https://intimelogistica.github.io/castor-site/frontend/prototypes/v2-versao-c-conversao.html
- EN:
  - https://intimelogistica.github.io/castor-site/frontend/prototypes/en/v2-versao-a-premium.html
  - https://intimelogistica.github.io/castor-site/frontend/prototypes/en/v2-versao-b-catalogo.html
  - https://intimelogistica.github.io/castor-site/frontend/prototypes/en/v2-versao-c-conversao.html
- ES:
  - https://intimelogistica.github.io/castor-site/frontend/prototypes/es/v2-versao-a-premium.html
  - https://intimelogistica.github.io/castor-site/frontend/prototypes/es/v2-versao-b-catalogo.html
  - https://intimelogistica.github.io/castor-site/frontend/prototypes/es/v2-versao-c-conversao.html

---

## 8. Decisões arquiteturais registradas

1. **Subdiretórios para i18n** (`/pt/`, `/en/`, `/es/`) em vez de subdomínios/TLDs — menor custo operacional e consolida autoridade de domínio.
2. **Strapi com plugin i18n** — campos localizados para nome, slug, descrição, SEO; campos numéricos/imagens compartilhados.
3. **Fallback pt-BR** — se tradução não existir, exibe versão em português com aviso sutil.
4. **Imagens compartilhadas entre idiomas** — mesma galeria, alt text localizado.
5. **Moeda BRL para todos os idiomas** — operação é no Brasil.
6. **SEO internacional** — hreflang + x-default + sitemaps separados.
7. **GitHub Pages para protótipos** — URL pública gratuita para compartilhamento; deploy via `git push`.

---

## 9. Pendências e próximos passos

### 9.1 Decisões pendentes
- [ ] Aprovação/combinação dos 3 layouts (A/B/C ou híbrido)
- [ ] Identidade visual da Castor (logo, cores oficiais, fontes) — pasta `brand/` vazia
- [ ] Glossário técnico final pt/en/es
- [ ] Quem fornece as traduções? (automático + revisão humana vs. tradutor profissional)
- [ ] Criar novo repo ou adaptar/forkar `intime-site`?
- [ ] Acesso às contas: Vercel, Cloudinary, Resend, Strapi, GA4/GTM/GSC do domínio

### 9.2 FASE 1 — Arquitetura e SEO
- [ ] Mapa de URLs multilíngues com slugs por idioma
- [ ] Keyword map por idioma
- [ ] Configurar Strapi 5 com content-types Castor e plugin i18n
- [ ] Especificar eventos de conversão com parâmetro `locale`

### 9.3 FASE 2 — Design
- [ ] Aplicar identidade visual nos protótipos
- [ ] Refinar seletor de idioma no header/footer (no momento é uma barra fixa provisória)
- [ ] Prever expansão de texto EN/ES (10–30% maior que PT)

### 9.4 FASE 3 — Desenvolvimento
- [ ] Setup Next.js com `[locale]`, middleware, `generateStaticParams`
- [ ] Integrar dicionários JSON e fetch localizado do Strapi
- [ ] Adaptar componentes do InTime (Header/Footer, ContactForm, WhatsApp, CookieConsent, JsonLd)
- [ ] Criar componentes Castor (HouseModelCard, Filter, Detail, etc.)

### 9.5 FASE 4 — Conteúdo
- [ ] Migrar 55 modelos para Strapi com traduções
- [ ] Criar páginas institucionais em 3 idiomas
- [ ] Produzir/otimizar imagens (WebP/AVIF, alt text)

### 9.6 FASE 5 — SEO técnico
- [ ] hreflang + x-default
- [ ] Sitemaps por idioma
- [ ] Schema JSON-LD completo por idioma
- [ ] Core Web Vitals

### 9.7 FASE 6 — Deploy
- [ ] Limpar WordPress antigo ou desativar
- [ ] DNS para Vercel
- [ ] HTTPS + HSTS + CSP
- [ ] GSC properties por locale

---

## 10. Notas técnicas importantes

### 10.1 Tradução automática
A tradução dos protótipos foi feita com `deep_translator.GoogleTranslator` (Google Translate free). Algumas traduções precisam de revisão humana antes do lançamento, especialmente:
- Termos técnicos do nicho
- Nome da marca "Castor" (em alguns casos foi traduzido indevidamente e corrigido via pós-processamento)
- Expressões coloquiais e CTAs
- Textos longos de descrição dos modelos

### 10.2 Limitações dos protótipos
- Imagens carregadas do site atual — se o WordPress antigo for desativado, as imagens quebrarão.
- Testemunhos e algumas obras são placeholders.
- Formulários enviam para WhatsApp, não para backend/CRM.
- Filtros da versão B funcionam com dados estáticos embutidos.

### 10.3 Manutenção dos dicionários
Os arquivos `frontend/i18n/*.json` são a fonte da verdade para a UI do Next.js. Ao adicionar novos textos de interface, atualizar os 3 idiomas.

### 10.4 Re-gerar traduções dos protótipos
Se houver mudanças nos protótipos PT:
1. Edite os arquivos em `frontend/prototypes/v2-*.html`
2. Execute `scripts/translate_prototypes.py` para atualizar o cache
3. Execute `scripts/generate_i18n_html.py` para gerar en/es
4. Execute `scripts/final_i18n_adjustments.py` para ajustes visuais
5. Commit e push

---

## 11. Links e referências

- Repositório GitHub: https://github.com/intimelogistica/castor-site
- Protótipos publicados: https://intimelogistica.github.io/castor-site/frontend/prototypes/
- Site atual (WordPress): https://casademadeira.com.br
- Site de referência InTime: https://intimelogistica.com.br
- Documentação Hermes: https://hermes-agent.nousresearch.com/docs

---

## 12. Glossário do projeto

| Termo | Significado |
|---|---|
| AEO | Answer Engine Optimization — otimização para motores de resposta/snippets |
| LLM | Large Language Model — modelo de linguagem grande (ChatGPT, Claude, etc.) |
| CMS | Content Management System — Strapi |
| SSG | Static Site Generation — geração estática de páginas |
| ISR | Incremental Static Regeneration — regeneração estática incremental |
| CSP | Content Security Policy |
| HSTS | HTTP Strict Transport Security |
| GSC | Google Search Console |
| GTM | Google Tag Manager |
| GA4 | Google Analytics 4 |

---

*Documento mantido pela equipe de desenvolvimento. Atualizar a cada marco alcançado.*

# Análise de Skills de UX/UI Disponíveis + Referências GitHub

> Skills encontradas na pasta local do Hermes e repositórios bem avaliados no GitHub para elevar o nível dos layouts do novo site Castor.

---

## 1. Skills de UX/UI disponíveis localmente

### 1.1 `claude-design` — Nota 9/10 ⭐
- **Descrição**: Design de artefatos HTML one-off (landing pages, protótipos, decks).
- **Pontos fortes**:
  - Processo completo: briefing → contexto → superfície → sistema visual → variações → verificação.
  - Regra **Surface-First**: evita o clássico "hero + 3 cards" genérico.
  - **Anti-Slop Diagnostic**: 10 sinais de design ruim de IA com instruções de correção.
  - Cobre tipografia, cor, composição, motion, acessibilidade, responsivo.
  - Ensina a fazer variações: conservadora, strong-fit e divergente.
- **Por que não usei antes**: deveria ter sido carregada antes de criar os protótipos.
- **Aplicabilidade para Castor**: **alta** — usar como processo principal para refazer os 3 layouts.

### 1.2 `popular-web-designs` — Nota 9/10 ⭐
- **Descrição**: 54 sistemas de design reais (Stripe, Linear, Vercel, Notion, Apple, Airbnb, Framer, etc.) com tokens CSS exatos.
- **Pontos fortes**:
  - Paletas, tipografia, componentes, espaçamento e sombras de marcas modernas já mapeadas.
  - Templates como Stripe, Framer, Apple, SpaceX, Linear são excelentes para posicionar um produto premium.
  - Inclui substituição de fontes proprietárias por Google Fonts equivalentes.
- **Aplicabilidade para Castor**: **muito alta** — escolher 2-3 referências (ex: Apple + Stripe + Framer) e aplicar na construção civil de madeira.

### 1.3 `sketch` — Nota 8/10
- **Descrição**: Mockups descartáveis em HTML para comparar 2-3 variantes.
- **Pontos fortes**:
  - Foco em iteração rápida e comparação lado a lado.
  - Ensina a criar variantes com posturas diferentes (density, emphasis, aesthetic, layout).
  - Inclui README por variante explicando trade-offs.
- **Limitação**: mais voltado para exploração inicial do que para entregas finais polidas.
- **Aplicabilidade para Castor**: **alta** para fazer novas rodadas de exploração.

### 1.4 `website-redesign-strategy` — Nota 8/10
- **Descrição**: Planejar redesigns via auditoria de stack e concorrentes.
- **Pontos fortes**:
  - Fases claras (diagnóstico → arquitetura → design → desenvolvimento → conteúdo → SEO → deploy).
  - Já foi usada como base do planejamento do Castor.
- **Limitação**: é estratégica, não ensina design visual especificamente.
- **Aplicabilidade para Castor**: **média** — boa para manter o projeto organizado, mas não resolve o visual.

### 1.5 `landing-page-audit-nextjs` — Nota 7/10
- **Descrição**: Auditoria e especificação de landing pages comerciais em Next.js.
- **Pontos fortes**:
  - Checklist completo de SEO/CRO para LPs.
  - Estrutura de seções recomendadas (hero, dores, solução, etapas, cases, form, FAQ, CTA final).
  - Alerta sobre CTAs env-gated e schema cross-linkage.
- **Limitação**: focada em auditoria/validação, não em criação visual.
- **Aplicabilidade para Castor**: **média-alta** — útil para validar as LPs depois de prontas.

### 1.6 `seo-cro-landing-page-audit` — Nota 7/10
- **Descrição**: Auditoria abrangente de SEO/CRO com análise competitiva em lote.
- **Pontos fortes**:
  - Muito detalhada sobre schemas JSON-LD, CTAs, interlinks, llms.txt.
  - Scripts para descobrir e auditar concorrentes.
- **Limitação**: é uma skill de análise, não de design visual.
- **Aplicabilidade para Castor**: **média** — usar depois que os layouts estiverem prontos.

### 1.7 `design-md` — Nota 7/10
- **Descrição**: Author/validate/export do formato DESIGN.md do Google (tokens de design).
- **Pontos fortes**:
  - Especificação formal de tokens (cores, tipografia, espaçamento).
  - Exporta para Tailwind/DTCG.
- **Limitação**: é para documentar sistema de design, não para gerar layouts visuais.
- **Aplicabilidade para Castor**: **média** — útil para documentar o design system depois de definido.

### 1.8 `excalidraw` — Nota 5/10
- **Descrição**: Diagramas estilo hand-drawn.
- **Aplicabilidade para Castor**: **baixa** — útil para wireframes rápidos, não para protótipos finais.

### 1.9 `architecture-diagram` — Nota 4/10
- **Descrição**: Diagramas de arquitetura/infra em SVG dark-themed.
- **Aplicabilidade para Castor**: **muito baixa** — não é para UI de site.

### 1.10 `p5js` — Nota 3/10
- **Descrição**: Sketches artísticos interativos.
- **Aplicabilidade para Castor**: **muito baixa** — poderia ser usado para um efeito artístico específico, mas não é prioridade.

---

## 2. Resumo das notas

| Skill | Nota | Uso recomendado agora |
|-------|:----:|-----------------------|
| `claude-design` | 9/10 | Processo principal de redesign |
| `popular-web-designs` | 9/10 | Vocabulary visual (Stripe, Apple, Framer) |
| `sketch` | 8/10 | Nova rodada de variações |
| `website-redesign-strategy` | 8/10 | Manter fases organizadas |
| `landing-page-audit-nextjs` | 7/10 | Validar LPs depois |
| `seo-cro-landing-page-audit` | 7/10 | Validar SEO/CRO depois |
| `design-md` | 7/10 | Documentar tokens depois |
| `excalidraw` | 5/10 | Wireframes rápidos |
| `architecture-diagram` | 4/10 | Não aplicável |
| `p5js` | 3/10 | Efeitos artísticos opcionais |

---

## 3. Referências no GitHub — melhores e mais bem avaliados

### 3.1 Landing pages gerais (alta qualidade)

| Repositório | Estrelas (aprox.) | Por que usar |
|-------------|-------------------|--------------|
| [cruip/open-react-template](https://github.com/cruip/open-react-template) | muito alta | React/Next.js, profissional, animado |
| [cruip/tailwind-landing-page-template](https://github.com/cruip/tailwind-landing-page-template) | muito alta | Tailwind puro, limpo, conversão |
| [ixartz/Next-JS-Landing-Page-Starter-Template](https://github.com/ixartz/Next-JS-Landing-Page-Starter-Template) | alta | Next.js 14 + Tailwind + TypeScript |
| [leoMirandaa/shadcn-landing-page](https://github.com/leoMirandaa/shadcn-landing-page) | alta | Shadcn/UI, moderno, acessível |
| [Blazity/next-saas-starter](https://github.com/Blazity/next-saas-starter) | alta | SaaS completo, boa arquitetura |
| [nordicgiant2/awesome-landing-page](https://github.com/nordicgiant2/awesome-landing-page) | alta | Coleção de templates |

### 3.2 Nicho imobiliário / casas (mais próximo da Castor)

| Repositório | Estrelas (aprox.) | Por que usar |
|-------------|-------------------|--------------|
| [Sara12-2/luxury-real-estate-landing-page](https://github.com/Sara12-2/luxury-real-estate-landing-page) | média | Imobiliário de luxo, filtros, calculadora, glassmorphism |
| [eslamalawy/Nexter](https://github.com/eslamalawy/Nexter) | média | Real estate moderno, grid de propriedades |
| [nahor-dev/wealthome-landing](https://github.com/nahor-dev/wealthome-landing) | média | Real estate HTML/CSS/JS puro |
| [ionandrei44/real-estate-landing-page](https://github.com/ionandrei44/real-estate-landing-page) | média | React + MUI, moderno |
| [MALEK-developer/Residem---Single-Property-Website-Template](https://github.com/MALEK-developer/Residem---Single-Property-Website-Template) | baixa | Foco em uma propriedade/single property |

### 3.3 Portfólios de arquitetura / design premium

| Repositório | Estrelas (aprox.) | Por que usar |
|-------------|-------------------|--------------|
| [mariovida/zona](https://github.com/mariovida/zona) | baixa | Arquitetura premium, projetos, galeria |
| [NexoStudio](https://github.com/yecos/NexoStudio) | baixa | Next.js, arquitetura, Vercel |
| [vladimirbalaur18/xLineDesignWeb](https://github.com/vladimirbalaur18/xLineDesignWeb) | baixa | Next.js, arquitetura moderna |
| [BR-Architect](https://github.com/Shubham-cyber-prog/BR-Architect) | baixa | HTML/CSS/JS, arquitetura limpa |

### 3.4 Layouts modernos / Bento / Agency

| Repositório | Estrelas (aprox.) | Por que usar |
|-------------|-------------------|--------------|
| [saipranay47/bento-grid-portfolio](https://github.com/saipranay47/bento-grid-portfolio) | média | Bento grid, moderno, Tailwind |
| [nurd0tid/eleveta](https://github.com/nurd0tid/eleveta) | baixa | Next.js 15 + Tailwind 4, agency moderno |
| [Lumacodes/devfolio-template](https://github.com/Lumacodes/devfolio-template) | média | Bento + 3D + dark/light mode |

### 3.5 Recursos e listas

| Repositório | Estrelas (aprox.) | Por que usar |
|-------------|-------------------|--------------|
| [nicolesaidy/awesome-web-design](https://github.com/nicolesaidy/awesome-web-design) | muito alta | Lista curada de recursos para designers |
| [birobirobiro/awesome-shadcn-ui](https://github.com/birobirobiro/awesome-shadcn-ui) | alta | Componentes e recursos Shadcn/UI |
| [nextjs/saas-starter](https://github.com/nextjs/saas-starter) | alta | Starter oficial Next.js + Postgres + Stripe + shadcn |

---

## 4. Recomendação para os novos layouts Castor

Combinação sugerida para elevar o nível:

1. **Use `claude-design` + `popular-web-designs`** como base do processo.
2. **Referências visuais**:
   - **Apple / SpaceX**: fotografia em full-bleed, tipografia grande, espaçamento generoso → para a versão Premium.
   - **Stripe**: gradientes sutis, cards com profundidade, CTAs elegantes → para a versão Conversão.
   - **Framer / Linear**: dark mode opcional, precisão, componentes refinados → para a versão Catálogo.
3. **Inspiração de nicho**: layouts de real estate de luxo (Sara12-2/luxury-real-estate) e portfólios de arquitetura (Zona, NexoStudio).
4. **Técnicas a adicionar**:
   - Hero em full-bleed com imagens reais de obras.
   - Cards de modelo com hover state, badges e specs visuais.
   - Grid assimétrico / bento para a galeria de modelos.
   - Micro-interações (hover, scroll reveal).
   - Tipografia com contraste de peso (serif para títulos, sans para corpo).
   - Paleta sofisticada (terroso + verde musgo + branco/cinza claro).

---

## 5. Próximo passo

Com sua autorização, refaço os 3 protótipos aplicando:
- Processo `claude-design` (Surface-First + Anti-Slop Diagnostic).
- Visual vocabulary de `popular-web-designs` (Apple/Stripe/Framer/Linear).
- Inspiração dos repositórios de real estate e arquitetura listados.
- Fotos reais de obras/modelos da Castor.
- Tipografia, micro-interações e hierarquia visual mais refinadas.

Aguardo seu “ok” para seguir.

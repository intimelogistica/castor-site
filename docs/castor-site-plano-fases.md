# Plano Estratégico — Novo Site Castor Casas de Madeira

> Baseado na infraestrutura do InTime (`intime-site`), análise do site publicado `intimelogistica.com.br`, auditoria do site atual `casademadeira.com.br` e amostra competitiva do nicho casas de madeira/MG.
> Última atualização: 2026-08-05

---

## 1. Resumo executivo

A Castor deve abandonar o WordPress atual (comprometido, Elementor desatualizado, sem SEO/AEO) e migrar para a **mesma stack moderna do InTime**: Next.js 16 + App Router, Tailwind v4, Strapi 5 CMS, Vercel, Resend, Cloudflare Turnstile, GTM/GA4/Consent Mode v2 e Cloudinary.

O projeto será executado em **7 fases**. Antes de escrever qualquer linha de código, definiremos arquitetura de informação, design system e estratégia de conteúdo AEO/LLM. Serão construídas **3 versões de layout** para aprovação visual.

---

## 2. O que reaproveitamos do InTime

### 2.1 Stack e infraestrutura

| Componente | Versão / detalhe | Reaproveitar? |
|---|---|---|
| Next.js | 16.2.4 + App Router | Sim — base do frontend |
| React | 19 | Sim |
| Tailwind CSS | v4 | Sim |
| TypeScript | 5.8 | Sim |
| Strapi | 5.50 | Sim — CMS para artigos, páginas, FAQ e novos content-types |
| Banco Strapi | Postgres / SQLite (dev) | Sim |
| Email | Resend | Sim |
| Anti-spam | Cloudflare Turnstile | Sim |
| Upload de mídia | Cloudinary | Sim |
| Analytics | Vercel Analytics + Speed Insights | Sim |
| GTM/GA4/Ads | Consent Mode v2 | Sim |
| Deploy | Vercel Pro | Sim |
| Cookie consent | Implementação própria (`intime_consent_v1`) | Sim |

### 2.2 Padrões e componentes prontos

- **SEO técnico**: `sitemap.ts`, `robots.ts`, `manifest.ts`, `opengraph-image.tsx`, metadata API, canonical, hreflang.
- **Schemas JSON-LD**: `LocalBusiness` + `ProfessionalService`, `WebSite`, `WebPage`, `FAQPage`, `Article`, `BreadcrumbList`, `HowTo`.
- **Conversão**: `ContactForm` (Server Action), `WhatsAppFloat`, `WhatsAppLeadGate`, `CookieConsent`, eventos `dataLayer`.
- **Conteúdo**: `ArticleCard`, sistema de LPs configuráveis (`lib/landing-pages`), feed RSS/Atom, `llms.txt`.
- **Integrações**: Notion CRM (`createLeadInNotion`), Resend, rate-limit, honeypot.

### 2.3 Lições do InTime para replicar/evitar

- **Replicar**: arquitetura de schema rica, `llms.txt`, FAQPage por página, Consent Mode v2, Server Actions, sitemap dinâmico.
- **Melhorar**: meta descriptions atualmente genéricas/longo demais em algumas LPs; o Castor terá metadados únicos e otimizados por modelo de casa.
- **Replicar**: PageSpeed médio 96 — manter o padrão.

### 2.4 Ajustes refinados a partir da análise técnica publicada

Análise adicional do site publicado `intimelogistica.com.br` apontou oportunidades que devem ser incorporadas ao Castor:

- **TTFB alto (~1,9s / total ~3,7s)**: o InTime faz chamadas ao Strapi durante o request. O Castor deve priorizar **SSG/ISR + edge cache**, gerando páginas estáticas no build e invalidando sob demanda. Meta: TTFB < 1s.
- **Cache HTML**: `max-age=0, must-revalidate` força revalidação a cada visita. Configurar cache adequado para conteúdo estático e usar ISR com `fallback` controlado.
- **OG images pesadas**: imagem PNG de 282 KB. Usar WebP/JPG otimizado e dimensões corretas (1200x630).
- **robots.txt com lixo legado**: ainda contém regras de WordPress (`/wp-admin/`, `/wp-login.php`). O Castor terá `robots.ts` limpo e gerado via código.
- **Hreflang incompleto**: páginas de categoria sem hreflang. Aplicar hreflang + x-default em **todas** as páginas públicas.
- **HSTS preload**: o InTime envia `preload`, mas o domínio não está na lista de pré-carregamento. Só ativar `preload` após submeter e validar em `hstspreload.org`.

---

## 3. Diagnóstico do site atual Castor (`casademadeira.com.br`)

- **Plataforma**: WordPress 7.0.2 + Elementor 3.14.1 (desatualizado).
- **Segurança**: backdoor ativo na página 404 injetando links de cassino/apostas.
- **SEO**: 0 H1, meta description ausente, sem schema estruturado, LCP mobile ~5,6s.
- **Conteúdo**: ~55 modelos de casa extraídos e salvos em `/root/castor-site/conteudo-original/casademadeira.com.br/`.
- **Domínio**: manter `casademadeira.com.br` com redirects 301 corretos.

---

## 4. Análise competitiva

Pesquisa automatizada identificou e analisou tecnicamente **10 fabricantes/construtoras reais** do nicho casas de madeira/MG. O mercado é **digitalmente imaturo**: a maioria usa WordPress + Elementor, tem sites visualmente aceitáveis, mas falhas graves de SEO/AEO.

| # | Empresa | URL | Stack | H1 semântico | Schema | FAQ | AEO Score* |
|---|---------|-----|-------|:------------:|:------:|:---:|:----------:|
| 1 | Doce Lar de Madeira | docelardemadeira.com.br | Wix | Não | Nenhum | Sim | 2/4 |
| 2 | Madecasa | madecasa.com.br | WP + Elementor | Não** | Nenhum | Sim | 3/4 |
| 3 | Chalé de Madeira | chaledemadeira.com | WordPress | Não | Nenhum | Sim | 2/4 |
| 4 | **Castor Casas (atual)** | casademadeira.com.br | WP + Elementor | Não | Nenhum | Sim | 1/4 |
| 5 | Casa de Madeira HM | casademadeirahm.com.br | WP + Elementor | Não | Nenhum | Sim | 2/4 |
| 6 | Aliança Casas | aliancacasasdemadeira.com.br | WP + Elementor | Não | Nenhum | Sim | 1/4 |
| 7 | Casa & Campo | casaecampo.com.br | SPA/HTML leve | Não | Nenhum | Não | 1/4 |
| 8 | Diamond House | casaprefabricada.com.br | WP + WooCommerce | Sim | FAQPage | Sim | **4/4** |
| 9 | Casas Paraná | casasparana.com.br | WP + Elementor | Não | Nenhum | Sim | 2/4 |
| 10 | Real Casas | realcasas.com.br | SPA/HTML leve | Não | Nenhum | Não | 1/4 |

\* AEO Score baseado em H1 semântico, meta description, schema e FAQ estruturado.  
\*\* Madecasa usa H1s como "01.", "02.", "03." — sem valor semântico.

### Principais falhas do nicho

- **Schema.org ausente**: apenas Diamond House usa `FAQPage`. Nenhum usa `LocalBusiness`, `Organization`, `BreadcrumbList` ou `Product`.
- **`llms.txt` inexistente**: 0 dos 10 sites possuem.
- **H1 semântico**: 9 de 10 falham. A maioria nem tem H1 na home.
- **Meta description**: Castor (atual) e Aliança não possuem.
- **Alt text**: HM e Casas Paraná têm ~0% de imagens com alt.
- **Velocidade**: 1,1s a 3,8s no HTML bruto; sites Elementor tendem a ser pesados.

### Oportunidades de diferenciação para o novo site Castor

1. **SEO técnico impecável** desde o lançamento: H1 único, meta descriptions, alt text 100%, sitemap, canonical.
2. **Schema completo**: `LocalBusiness`, `Organization`, `BreadcrumbList`, `FAQPage`, `Product` (por modelo), `Article`, `HowTo`.
3. **AEO/LLM**: criar `/llms.txt`, FAQ estruturado em todas as páginas, conteúdo em formato de respostas diretas.
4. **Estratégia local**: LPs por cidade (Lagoa Santa, Matozinhos, BH, Pedro Leopoldo, Sete Lagoas, Nova Lima, Contagem).
5. **Conteúdo comparativo**: preço/m², madeira vs alvenaria, prazos, manutenção, financiamento.
6. **Conversão**: catálogo interativo com filtros, calculadora/cotador online, WhatsApp integrado, cases de obras com depoimentos.
7. **Performance**: Next.js estático pode facilmente superar todos os concorrentes em Core Web Vitals.

### Concorrente de referência

- **Diamond House (`casaprefabricada.com.br`)**: único com AEO 4/4 por ter H1, FAQ, schema FAQPage, meta e OG. Ponto fraco: poderia ter `LocalBusiness`/`Product` e `llms.txt`.

### Arquivos da pesquisa

- Relatório completo: `C:\Users\João Batista\relatorio_concorrentes_casas_madeira_mg.md`
- Dados brutos: `competitors_analysis.json`, `competitors_deep_analysis.json`
- Scripts: `research_competitors.py`, `analyze_competitors.py`, `analyze_competitors_deep.py`

---

## 5. Plano por fases

### FASE 0 — Fundação e decisões (1 semana)

- [ ] Confirmar domínio: manter `casademadeira.com.br`.
- [ ] Criar repositório Git (`castor-site`) ou forkar/adaptar `intime-site`.
- [ ] Definir identidade visual provisória: paleta (madeira/terrosos/verde), tipografia, tom de voz.
- [ ] Listar todas as integrações obrigatórias: WhatsApp, telefone, email, formulário, eventos GA4/Ads.
- [ ] Mapear conteúdo existente: 55 modelos + páginas institucionais do spec.
- [ ] Criar conta Vercel/Cloudinary/Resend/Strapi Cloud se necessário (ou reutilizar as do InTime).

**Entregável**: documento de arquitetura + repositório inicial.

---

### FASE 1 — Arquitetura, SEO e AEO (1–2 semanas)

- [ ] **Mapa de páginas**:
  - Institucionais: Home, Sobre, Como Funciona, Obras Realizadas, Depoimentos, Contato.
  - Comerciais: modelos de casa, categorias (chalés, casas de campo, residenciais, comerciais).
  - LPs de captura: "casa de madeira BH", "casa de madeira Lagoa Santa", etc.
  - Blog/Base de conhecimento: AEO (respostas diretas, HowTo, FAQ).
- [ ] **Keyword mapping**: intenção por página (navigational, transactional, informational).
- [ ] **Arquitetura Strapi**:
  - Reutilizar `article`, `page`, `faq`, `category`, `tag`, `author`.
  - Criar `house-model` (nome, slug, categoria, metragem, quartos, banheiros, preço, descrição, galeria, planta, destaque, SEO).
  - Criar `testimonial` (nome, cidade, foto, depoimento, obra).
  - Criar `obra-realizada` (título, local, descrição, galeria, modelo relacionado).
- [ ] **Especificar eventos de conversão** para GTM/GA4/Ads.
- [ ] **Estratégia de AEO/LLM**:
  - `direct_answer` em artigos (igual ao InTime).
  - FAQPage vinculado a cada página e modelo.
  - `llms.txt` com resumo do negócio, URLs principais e diretrizes de conteúdo.
  - Schema `Product` para modelos de casa (nome, descrição, imagem, oferta, marca).

**Entregável**: documento de arquitetura + schemas do Strapi + keyword map.

---

### FASE 2 — Design: 3 versões de layout (2 semanas)

Construir 3 propostas visuais modernas (wireframes/protótipos em HTML estático ou Figma). Todas devem manter:

- Mobile-first.
- CTAs de WhatsApp e formulário sempre visíveis.
- Filtro de modelos por metragem/quartos/preço.
- Galeria de imagens lazy-loaded.
- Tipografia legível e espaçamento generoso.

**Versão A — Premium/Institucional**
- Estética clean, cores sóbrias (branco, cinza, madeira natural, verde musgo).
- Foco em credibilidade: "+X anos", "Y obras entregues", selos de qualidade.
- Hero com foto de obra realizada + headline direta.
- Ideal para posicionar a Castor como construtora séria e diferenciada.

**Versão B — Catálogo/Visual**
- Grid grande de modelos na home.
- Filtros de busca em destaque.
- Foco nas imagens e especificações rápidas.
- Ideal para quem já sabe o que quer e quer comparar modelos.

**Versão C — Conversão/Agressiva**
- Hero com formulário ou CTA de orçamento no primeiro viewport.
- Prova social forte (depoimentos, obras, garantia).
- Sticky WhatsApp + múltiplos gatilhos de conversão.
- LPs enxutas por cidade/bairro.
- Ideal para campanhas pagas e captura imediata de leads.

**Entregável**: 3 protótipos aprovados (ou combinados em híbrido).

---

### FASE 3 — Desenvolvimento frontend/backend base (3–4 semanas)

- [ ] Setup do projeto Next.js com Tailwind v4, shadcn/ui, tipografia e design tokens.
- [ ] Configurar Strapi 5 com content-types Castor.
- [ ] Adaptar componentes do InTime:
  - Header/Footer (novo design).
  - ContactForm + Server Action + Turnstile.
  - WhatsAppFloat + WhatsAppLeadGate.
  - CookieConsent + Consent Mode v2.
  - JsonLd, FAQ schema, BreadcrumbList.
- [ ] Criar componentes novos:
  - `HouseModelCard`, `HouseModelGrid`, `HouseModelFilter`.
  - `HouseModelDetail` (galeria, planta, especificações, CTA).
  - `ObraRealizadaCard`, `TestimonialCard`.
  - `Hero`, `FeatureSection`, `CTABanner`.
- [ ] Implementar sistema de LPs configuráveis (reaproveitar `lib/landing-pages`).
- [ ] Configurar Resend, Notion CRM, eventos `dataLayer`.
- [ ] Setup Vercel: deploy, previews, variáveis de ambiente.

**Entregável**: site funcional em ambiente de preview com páginas principais.

---

### FASE 4 — Conteúdo e migração (2–3 semanas)

- [ ] Migrar os 55 modelos de casa do `conteudo-original` para o Strapi.
- [ ] Padronizar títulos, descrições e URLs (`/modelos/[slug]`).
- [ ] Reescrever conteúdos com AEO:
  - Resposta direta no início.
  - Especificações estruturadas.
  - FAQ por modelo.
- [ ] Criar páginas institucionais (Sobre, Como Funciona, Obras, Depoimentos).
- [ ] Produzir/otimizar imagens: compressão WebP/AVIF, alt text descritivo.
- [ ] Criar artigos iniciais do blog (topo de funil):
  - "Quanto custa uma casa de madeira em BH?"
  - "Casa de madeira vs alvenaria: prós e contras"
  - "Como funciona a construção de uma casa pré-fabricada de madeira"
- [ ] Gerar `llms.txt`, `robots.txt`, `sitemap.xml`, `manifest.webmanifest`, feeds RSS.

**Entregável**: conteúdo completo populado no CMS + site com todos os modelos.

---

### FASE 5 — SEO técnico, AEO e performance (1–2 semanas)

- [ ] Metadata única por página/modelo/artigo (title ≤ 60, description ≤ 160).
- [ ] Schema JSON-LD completo:
  - `Organization`/`LocalBusiness` (com geo, telefone, WhatsApp, horário).
  - `WebSite` + `WebPage` + `BreadcrumbList` em todas as páginas.
  - `Product` em cada modelo de casa.
  - `FAQPage` vinculado a páginas e modelos.
  - `Article` + `HowTo` no blog.
- [ ] URLs amigáveis e canonicals.
- [ ] Redirecionamentos 301 do site antigo (WordPress → novo Next.js).
- [ ] Otimização Core Web Vitals:
  - Imagens otimizadas (`next/image`, WebP/AVIF).
  - Fontes otimizadas.
  - Code splitting / lazy loading.
  - TTFB < 1s (meta).
- [ ] `llms.txt` atualizado com todas as URLs e diretrizes.
- [ ] Testes de acessibilidade (WCAG 2.1 AA) e mobile usability.

**Entregável**: site otimizado, aprovado nos testes de SEO e performance.

---

### FASE 6 — Segurança, testes e deploy (1 semana)

- [ ] Limpar/resetar instância WordPress antiga (remover backdoor) ou desativar.
- [ ] Configurar DNS para Vercel.
- [ ] HTTPS + HSTS + CSP ajustado.
- [ ] Testes de segurança básicos (headers, formulários, spam).
- [ ] Testes de usabilidade em formulários, WhatsApp, filtros, galeria.
- [ ] Deploy em produção (`casademadeira.com.br`).
- [ ] Configurar GSC, GA4, GTM (ou reaproveitar contas existentes).
- [ ] Sitemap enviado ao Google.

**Entregável**: site no ar, indexável, monitorado.

---

### FASE 7 — Pós-lançamento e evolução (contínuo)

- [ ] Monitorar Core Web Vitals no GSC.
- [ ] Acompanhar rankings e snippets (AEO).
- [ ] Criar novas LPs por cidade/cenário.
- [ ] Expandir blog com conteúdo AEO.
- [ ] Otimizar taxa de conversão (CTA, formulários, WhatsApp).
- [ ] Campanhas pagas (Google Ads/Meta) quando apropriado.
- [ ] Backlinks locais (diretórios de BH/MG).

---

## 6. Stack final recomendada

| Camada | Tecnologia |
|---|---|
| Frontend | Next.js 16 (App Router) + React 19 + TypeScript |
| Estilo | Tailwind CSS v4 + design tokens próprios |
| UI | shadcn/ui + componentes customizados |
| CMS | Strapi 5.50 (content-types Castor) |
| Banco | PostgreSQL (produção) / SQLite (dev) |
| Mídia | Cloudinary |
| Email | Resend |
| Anti-spam | Cloudflare Turnstile |
| Analytics | GA4 + GTM + Consent Mode v2 + Vercel Analytics |
| CRM leads | Notion (via Server Action) |
| Deploy | Vercel |
| Domínio | `casademadeira.com.br` |

---

## 7. Próximos passos imediatos

1. **Você aprova a stack e as 3 direções de layout?** Se sim, seguimos para FASE 0/FASE 1.
2. **Escolha da identidade visual**: a Castor já tem marca (cores, logo, fonte) ou precisamos criar?
3. **Decisão de repositório**: criar novo repo ou adaptar `intime-site`?
4. **Acesso às contas**: Vercel, Cloudinary, Resend, Strapi, GA4/GTM/GSC do domínio `casademadeira.com.br`.
5. **Definição de modelo de casa**: quais campos são obrigatórios por modelo? (ex: metragem, quartos, banheiros, preço, materiais, planta, galeria)

Assim que você validar esse plano, iniciamos a **FASE 1 (arquitetura + keyword map)** e em seguida a **FASE 2 (3 versões de design)**.

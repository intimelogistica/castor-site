# Estratégia de Internacionalização — Castor Casas de Madeira

> Idiomas de lançamento: **Português (pt-BR)**, **Inglês (en-US)**, **Espanhol (es-ES)**.
> Objetivo: atender exportação / compradores estrangeiros no Brasil e mercados hispânicos sem perder SEO local nem aumentar a complexidade de manutenção.
> Última atualização: 2026-08-07

---

## 1. Decisões arquiteturais

### 1.1 Estrutura de URL: subdiretórios

Usaremos **subdiretórios por idioma** (`/pt/`, `/en/`, `/es/`). A raiz (`/`) redireciona para `/pt/` ou serve o conteúdo em português como `x-default`.

| Página | Português | Inglês | Espanhol |
|---|---|---|---|
| Home | `/pt/` | `/en/` | `/es/` |
| Modelos | `/pt/modelos` | `/en/models` | `/es/modelos` |
| Modelo Brasil | `/pt/modelos/casa-de-madeira-modelo-brasil` | `/en/models/brazil-wood-house-model` | `/es/modelos/casa-de-madera-modelo-brasil` |
| Contato | `/pt/contato` | `/en/contact` | `/es/contacto` |
| LP BH | `/pt/casa-de-madeira-bh` | `/en/wood-house-belo-horizonte` | `/es/casa-de-madera-belo-horizonte` |

**Por que subdiretórios e não subdomínios/TLDs?**
- Menor custo operacional (um domínio, um certificado, uma instância Vercel).
- Consolida autoridade de domínio (`casademadeira.com.br`) para todos os idiomas.
- Fácil de implementar no Next.js App Router com `[locale]` dynamic segment.
- Permite hreflang cruzado sem complexidade de CORS/infra.

### 1.2 Idioma padrão e comportamento da raiz

- `/` → detecta idioma do navegador (`accept-language`). Se `pt` → 308 para `/pt/`; se `es` → `/es/`; caso contrário `/en/`.
- `/` também serve como **x-default** nos hreflangs (aponta para a versão de escolha automática).
- Sitemaps separados por idioma: `/pt/sitemap.xml`, `/en/sitemap.xml`, `/es/sitemap.xml`, mais índice `/sitemap.xml`.

### 1.3 Escopo de idiomas

| Código | Idioma | Público-alvo principal |
|---|---|---|
| `pt-BR` | Português do Brasil | Clientes brasileiros (prioridade) |
| `en-US` | Inglês americano | Estrangeiros no Brasil, investidores, expats, futura exportação |
| `es-ES` | Espanhol europeu/ LATAM neutral | Compradores hispanos, paraguaios, argentinos, chilenos no Brasil |

> Nota: es-ES pode evoluir para es-MX ou es-AR no futuro se houver demanda. Inicialmente usamos um espanhol neutro com locale `es`.

---

## 2. Next.js App Router — implementação

### 2.1 Estrutura de rotas

```
app/
├── [locale]/
│   ├── layout.tsx          # carrega dicionário + metadata base + JsonLd
│   ├── page.tsx            # home
│   ├── modelos/
│   │   ├── page.tsx        # listagem
│   │   └── [slug]/page.tsx # detalhe do modelo
│   ├── contato/
│   │   └── page.tsx
│   ├── casa-de-madeira-bh/
│   │   └── page.tsx
│   └── ...
├── api/
│   └── revalidate/route.ts # invalidação por locale
├── sitemap.ts              # índice de sitemaps
└── robots.ts
```

### 2.2 Middleware de locale

```ts
// middleware.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

const locales = ['pt', 'en', 'es'];
const defaultLocale = 'pt';

export function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;
  const pathnameHasLocale = locales.some(
    (locale) => pathname.startsWith(`/${locale}/`) || pathname === `/${locale}`
  );
  if (pathnameHasLocale) return NextResponse.next();

  // Ignora arquivos estáticos e API
  if (pathname.startsWith('/_next') || pathname.startsWith('/api')) return;

  const acceptLang = request.headers.get('accept-language') || '';
  const preferred = acceptLang.split(',')[0]?.split('-')[0];
  const locale = locales.includes(preferred) ? preferred : defaultLocale;

  request.nextUrl.pathname = `/${locale}${pathname}`;
  return NextResponse.redirect(request.nextUrl, 308);
}

export const config = {
  matcher: ['/((?!_next|api|favicon.ico|robots.txt|sitemap.xml).*)'],
};
```

### 2.3 Dicionários de UI

Criar arquivos JSON por locale em `frontend/i18n/`:

```
i18n/
├── pt.json        # UI, CTAs, labels, mensagens
├── en.json
├── es.json
└── getDictionary.ts
```

Exemplo:

```json
{
  "nav": {
    "models": "Modelos",
    "about": "Sobre",
    "contact": "Contato",
    "budget": "Solicitar orçamento"
  },
  "model": {
    "area": "Área total",
    "bedrooms": "Quartos",
    "bathrooms": "Banheiros",
    "getQuote": "Quero um orçamento para este modelo"
  }
}
```

Carregamento com `getDictionary(locale)` dentro dos Server Components. Cache via `React.cache` ou `unstable_cache`.

### 2.4 Geração estática de locales

```ts
// app/[locale]/layout.tsx
export async function generateStaticParams() {
  return [{ locale: 'pt' }, { locale: 'en' }, { locale: 'es' }];
}
```

Todas as páginas dinâmicas (`[slug]`) devem exportar `generateStaticParams` que inclua cada locale + slug.

---

## 3. Strapi: conteúdo multilíngue

### 3.1 Estratégia: campos localizados (Internationalization plugin)

Ativar o plugin oficial `i18n` do Strapi 5. Configurar locales:
- Portuguese (Brazil) (`pt-BR`)
- English (`en`)
- Spanish (`es`)

### 3.2 Content-types com localização

Habilitar localização nos campos editáveis:

| Content-type | Campos localizados | Campos não localizados |
|---|---|---|
| `house-model` | `name`, `slug`, `description`, `short_description`, `seo_title`, `seo_description`, `includes` | `area_total_m2`, `bedrooms`, `bathrooms`, `floors`, `gallery`, `featured_image`, `is_published` |
| `category` | `name`, `slug`, `description` | `type`, `display_order` |
| `page` | `title`, `slug`, `content`, `seo_title`, `seo_description` | `is_published` |
| `article` | `title`, `slug`, `content`, `direct_answer`, `seo_title`, `seo_description` | `author`, `publishedAt`, `cover_image` |
| `faq` | `question`, `answer` | `pages` (relação) |
| `testimonial` | `quote` | `name`, `city`, `photo`, `obra` |
| `obra-realizada` | `title`, `description` | `local`, `gallery`, `modelo` |

### 3.3 Slugs por idioma

Cada tradução pode ter slug diferente. Exemplo:
- pt: `casa-de-madeira-modelo-brasil`
- en: `brazil-wood-house-model`
- es: `casa-de-madera-modelo-brasil`

**Regra técnica**: o frontend faz fetch por `locale` + `slug`. A API do Strapi retorna a entrada localizada. O fallback é `pt-BR` caso a tradução não exista.

### 3.4 Fallback de conteúdo

```ts
// utils/getLocalizedEntry.ts
export async function getLocalizedEntry({ contentType, slug, locale }: Params) {
  const strapiLocale = mapLocale(locale); // pt -> pt-BR
  const data = await fetchStrapi({ contentType, slug, locale: strapiLocale });
  if (data) return data;
  // Fallback para português
  return fetchStrapi({ contentType, slug, locale: 'pt-BR' });
}
```

Exibir um banner sutil "Conteúdo disponível apenas em português" quando o fallback for acionado.

---

## 4. SEO internacional

### 4.1 hreflang em todas as páginas

```html
<link rel="alternate" hreflang="pt-br" href="https://casademadeira.com.br/pt/modelos/casa-de-madeira-modelo-brasil" />
<link rel="alternate" hreflang="en-us" href="https://casademadeira.com.br/en/models/brazil-wood-house-model" />
<link rel="alternate" hreflang="es" href="https://casademadeira.com.br/es/modelos/casa-de-madera-modelo-brasil" />
<link rel="alternate" hreflang="x-default" href="https://casademadeira.com.br/" />
```

Implementar via `metadata.alternates` no Next.js:

```ts
export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { locale, slug } = params;
  const entry = await getModel(slug, locale);
  return {
    title: entry.seo_title,
    description: entry.seo_description,
    alternates: {
      canonical: `/${locale}/models/${slug}`,
      languages: {
        'pt-BR': `/pt/modelos/${entry.slugs.pt}`,
        'en-US': `/en/models/${entry.slugs.en}`,
        'es': `/es/modelos/${entry.slugs.es}`,
        'x-default': '/',
      },
    },
  };
}
```

### 4.2 Sitemap multilíngue

- Índice: `/sitemap.xml` aponta para 3 sitemaps.
- Por idioma: `/pt/sitemap.xml`, `/en/sitemap.xml`, `/es/sitemap.xml`.
- Cada URL inclui `hreflang` via extensão `xhtml:link` (opcional, mas recomendado).

### 4.3 URLs amigáveis por idioma

Evitar slugs genéricos em inglês/español que percam intenção local. Exemplos:

| PT | EN | ES |
|---|---|---|
| `/pt/casa-de-madeira-bh` | `/en/wood-house-belo-horizonte` | `/es/casa-de-madera-belo-horizonte` |
| `/pt/como-funciona` | `/en/how-it-works` | `/es/como-funciona` |
| `/pt/obras-realizadas` | `/en/completed-projects` | `/es/obras-realizadas` |

Manter consistência: termos técnicos como "wood house", "casa de madera", "casa de madeira" são mais reconhecíveis que traduções literais.

---

## 5. Componentes de UI afetados

### 5.1 Seletor de idioma

- Local: header, footer ou ambos.
- Formato: dropdown ou botões `PT | EN | ES`.
- Comportamento: troca apenas o prefixo do locale, mantendo a página atual. Se a página não existir no idioma destino, redireciona para a home do idioma.
- Acessibilidade: `aria-label="Mudar idioma"`, role="combobox" no dropdown.

### 5.2 Direção de texto

Todos os idiomas são LTR, sem necessidade de RTL.

### 5.3 Formatação de números, datas e moeda

```ts
const formatArea = (n: number, locale: string) =>
  new Intl.NumberFormat(locale, { minimumFractionDigits: 2 }).format(n);

// pt-BR: 139,30 m²
// en-US: 139.30 m²
// es: 139,30 m²
```

Moeda: manter `BRL` para todos os idiomas, pois a operação é no Brasil. Formatar conforme locale.

### 5.4 Formulários

- Labels, placeholders e mensagens de erro vindos do dicionário JSON.
- Validação mantém a mesma lógica; mensagens de erro traduzidas.
- WhatsApp CTA: manter número brasileiro, mas a mensagem pré-preenchida muda de idioma.

---

## 6. Tradução de conteúdo

### 6.1 Prioridade de tradução

| Prioridade | Conteúdo | Nota |
|---|---|---|
| P0 | UI/UX (menus, botões, formulários) | Via JSON i18n |
| P0 | Home + páginas institucionais | Conteúdo fixo do site |
| P0 | Modelos de casa (nome, descrição, SEO) | 47 modelos × 2 idiomas = ~100 entradas |
| P1 | Páginas de captura local (LPs) | BH, Lagoa Santa, Matozinhos etc. |
| P1 | FAQ geral e por modelo | Alto impacto AEO |
| P2 | Blog / base de conhecimento | Artigos AEO podem ser traduzidos sob demanda |
| P2 | Depoimentos e obras realizadas | Pode manter pt-BR com fallback |

### 6.2 Qualidade da tradução

- **Não usar tradução automática direta no frontend**.
- Usar tradução profissional ou revisão humana para EN/ES.
- Manter glossário consistente:
  - PT: "casa de madeira", "casas pré-fabricadas"
  - EN: "wood house", "prefabricated wooden house"
  - ES: "casa de madera", "casa prefabricada de madera"

### 6.3 Imagens e mídia

- Galerias de modelos **não precisam ser traduzidas** (são as mesmas imagens).
- Imagens com texto embutido devem ter versões por idioma (raro, mas possível para infográficos).
- Alt text deve ser localizado no Strapi.

---

## 7. Analytics, Consent Mode e GTM

### 7.1 Eventos por idioma

Manter os mesmos eventos (`form_submit`, `whatsapp_click`, `model_view`), mas adicionar parâmetro `language`/`locale` em todos:

```js
dataLayer.push({ event: 'form_submit', locale: 'en', model_slug: 'brazil' });
```

### 7.2 Consent Mode v2

- Banner de cookies já contempla escolha de idioma via dicionário.
- Opções de consentimento (`ad_storage`, `analytics_storage`, etc.) são iguais para todos os idiomas.

### 7.3 GA4 / GSC

- Uma propriedade GA4 com dimensão `language` (padrão) é suficiente.
- GSC: cadastrar as 3 versões de property (prefix `/pt/`, `/en/`, `/es/`) além do domínio raiz.

---

## 8. Impacto no plano de fases

A internacionalização será incorporada como **requisito transversal**, não como fase isolada. Ajustes:

- **FASE 1 (Arquitetura)**: incluir mapa de URLs multilíngues e slugs por idioma.
- **FASE 2 (Design)**: validar seletor de idioma e densidade de texto em EN/ES (geralmente 10–30% maior que PT).
- **FASE 3 (Desenvolvimento)**: implementar `[locale]`, middleware, dicionários e fetch localizado do Strapi.
- **FASE 4 (Conteúdo)**: traduzir P0 e P1; configurar fallback pt-BR.
- **FASE 5 (SEO)**: hreflang, sitemaps separados, canonicals e testes de idioma.
- **FASE 6 (Deploy)**: validar redirects da raiz e GSC por locale.

---

## 9. Riscos e mitigações

| Risco | Impacto | Mitigação |
|---|---|---|
| Tradução automática ruim | SEO e credibilidade prejudicados | Usar tradutor + revisor; glossário fixo |
| Slugs duplicados entre idiomas | Conflito de URL | Strapi valida unicidade por locale |
| Hreflang incorreto | Indexação errada no Google | Testar com GSC e ferramentas hreflang |
| Manutenção de 3 idiomas | Custo contínuo alto | Fallback pt-BR; traduzir sob demanda |
| Conteúdo EN/ES desatualizado | Informação divergente | Processo de publicação sincronizada |

---

## 10. Próximos passos imediatos

1. **Validar escopo**: todos os 3 idiomas no mesmo domínio com subdiretórios? Ou prefere começar só com EN e depois ES?
2. **Definir glossário base**: aprovar termos técnicos em EN/ES.
3. **Atualizar arquitetura de informação**: lista de slugs por idioma para cada página.
4. **Decisão de tradução**: você fornece as traduções ou quer que eu gere primeira versão (com revisão humana depois)?
5. **Ajustar protótipos v2**: adicionar seletor de idioma nas 3 versões de layout.

Assim que validar, atualizo os protótipos e a arquitetura do Strapi.

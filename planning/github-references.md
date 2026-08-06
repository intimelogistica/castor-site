# Referências de Repositórios GitHub — Castor Site

Lista de repositórios e templates selecionados como referência visual/UX para a segunda rodada de protótipos do novo site da Castor Casas de Madeira.

## Como usar este arquivo

Cada repositório abaixo pode ser clonado localmente para inspeção de componentes, tipografia, grid, cores e micro-interações:

```bash
gh repo clone <owner>/<repo>
```

---

## 1. Direção Premium (fotografia, arquitetura, impacto visual)

Perfil: hero imersivo, tipografia serifada/grande, poucos elementos, foco em imagens de obra/modelo.

| Repositório | Stack | O que aproveitar |
|-------------|-------|------------------|
| [mariovida/zona](https://github.com/mariovida/zona) | Next.js + Tailwind | Portfólio de arquitetura com layouts assimétricos e tipografia elegante |
| [yecos/NexoStudio](https://github.com/yecos/NexoStudio) | Next.js | Studio de arquitetura, fotografia full-bleed e transições suaves |
| [vladimirbalaur18/xLineDesignWeb](https://github.com/vladimirbalaur18/xLineDesignWeb) | Next.js | Design minimalista e alto contraste para projetos premium |
| [nurd0tid/eleveta](https://github.com/nurd0tid/eleveta) | Next.js 15 + Tailwind 4 | Layout moderno, bento grid e componentes refinados |

---

## 2. Direção Catálogo (descoberta, filtros, grid de produtos)

Perfil: galeria de modelos, filtros sutis, cards ricos, navegação por categorias.

| Repositório | Stack | O que aproveitar |
|-------------|-------|------------------|
| [Sara12-2/luxury-real-estate-landing-page](https://github.com/Sara12-2/luxury-real-estate-landing-page) | React + Tailwind | Hero imobiliário de luxo, cards de imóveis e seção de features |
| [eslamalawy/Nexter](https://github.com/eslamalawy/Nexter) | HTML/CSS/Sass | Grid sofisticado de propriedades, tipografia e composição visual |
| [nahor-dev/wealthome-landing](https://github.com/nahor-dev/wealthome-landing) | HTML/CSS/JS | Landing page de imóveis de luxo com foco em fotografia e prova social |
| [ionandrei44/real-estate-landing-page](https://github.com/ionandrei44/real-estate-landing-page) | Next.js | Padrões de listagem e detalhe de propriedades |
| [saipranay47/bento-grid-portfolio](https://github.com/saipranay47/bento-grid-portfolio) | HTML/CSS | Grid tipo Bento para organizar modelos e diferenciais |

---

## 3. Direção Conversão (CTAs, prova social, formulários)

Perfil: copy persuasiva, botões de alto contraste, depoimentos, garantias, formulário otimizado.

| Repositório | Stack | O que aproveitar |
|-------------|-------|------------------|
| [cruip/open-react-template](https://github.com/cruip/open-react-template) | React + Tailwind | Landing page moderna com seções de conversão bem definidas |
| [cruip/tailwind-landing-page-template](https://github.com/cruip/tailwind-landing-page-template) | HTML + Tailwind | Mesma família Cruip, versão estática, fácil de inspecionar |
| [ixartz/Next-JS-Landing-Page-Starter-Template](https://github.com/ixartz/Next-JS-Landing-Page-Starter-Template) | Next.js + Tailwind | Starter completo com CTA, features, testimonials e FAQ |
| [leoMirandaa/shadcn-landing-page](https://github.com/leoMirandaa/shadcn-landing-page) | Next.js + shadcn/ui | Componentes de conversão com shadcn, dark mode e animações |
| [Blazity/next-saas-starter](https://github.com/Blazity/next-saas-starter) | Next.js | Padrões de pricing, CTA e prova social para produtos |

---

## 4. Listas e repositórios de recursos

Úteis para descobrir mais templates, componentes e padrões de design.

| Repositório | Descrição |
|-------------|-----------|
| [nicolesaidy/awesome-web-design](https://github.com/nicolesaidy/awesome-web-design) | Lista curada de recursos de web design |
| [birobirobiro/awesome-shadcn-ui](https://github.com/birobirobiro/awesome-shadcn-ui) | Componentes e recursos para shadcn/ui |
| [nextjs/saas-starter](https://github.com/nextjs/saas-starter) | Starter oficial Next.js para SaaS, boas práticas de App Router |
| [nordicgiant2/awesome-landing-page](https://github.com/nordicgiant2/awesome-landing-page) | Coleção de landing pages de alta qualidade |
| [Lumacodes/devfolio-template](https://github.com/Lumacodes/devfolio-template) | Template de portfólio moderno, animações e micro-interações |

---

## Notas

- Todos os repositórios são públicos e podem ser inspecionados sem autenticação extra.
- A escolha final de padrões será feita durante a aplicação das skills `claude-design` e `popular-web-designs`.
- Os protótipos HTML finais devem combinar elementos das três direções acima, priorizando:
  1. Fotografia de qualidade dos modelos Castor
  2. Tipografia serifada para títulos e sans-serif clean para UI
  3. Grid assimétrico / bento
  4. Micro-interações e estados de hover refinados
  5. Paleta sofisticada (sem cair no vermelho genérico de template)

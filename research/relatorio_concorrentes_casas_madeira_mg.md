# Relatório de Concorrentes — Casas de Madeira em Minas Gerais

**Data:** 05/08/2026  
**Nicho:** Fabricantes/construtoras de casas de madeira pré-fabricadas no Brasil, especialmente MG (BH, Lagoa Santa, Matozinhos).  
**Fonte:** DuckDuckGo + Bing (primeiras páginas) para as palavras-chave solicitadas. Portais (OLX, VivaReal, Airbnb, Trovit etc.) foram descartados.

---

## 1. Concorrentes identificados (10 sites reais)

| # | Empresa | URL | Descrição breve | Stack estimado |
|---|---------|-----|-----------------|----------------|
| 1 | **Doce Lar de Madeira** | [docelardemadeira.com.br](https://www.docelardemadeira.com.br/) | Construtora de casas pré-fabricadas sustentáveis na região de BH. | Wix |
| 2 | **Madecasa** | [madecasa.com.br](https://madecasa.com.br/) | Fábrica de casas de madeira prontas e pré-fabricadas em BH. | WordPress + Elementor + jQuery |
| 3 | **Chalé de Madeira** | [chaledemadeira.com](https://chaledemadeira.com/) | Kits de casas, chalés, tiny houses e celeiros pré-fabricados. | WordPress |
| 4 | **Castor Casas de Madeira** | [casademadeira.com.br](https://casademadeira.com.br/) | Casas pré-fabricadas de madeira maciça com showroom em Lagoa Santa/Matozinhos. | WordPress + Elementor + jQuery |
| 5 | **Casa de Madeira HM** | [casademadeirahm.com.br](https://www.casademadeirahm.com.br/) | Empresa de casas pré-fabricadas de madeira em BH/MG. | WordPress + Elementor + jQuery |
| 6 | **Aliança Casas de Madeira** | [aliancacasasdemadeira.com.br](https://aliancacasasdemadeira.com.br/) | Construtora de casas de madeira com foco em lares sustentáveis. | WordPress + Elementor + jQuery |
| 7 | **Casa & Campo** | [casaecampo.com.br](https://casaecampo.com.br/) | Há 25+ anos no mercado de casas de madeira maciça pré-fabricadas. | Site muito leve / possivelmente SPA/JS |
| 8 | **Diamond House** | [casaprefabricada.com.br](https://www.casaprefabricada.com.br/) | Casas pré-fabricadas de madeira de alto padrão. | WordPress + Elementor + WooCommerce + jQuery |
| 9 | **Casas Paraná** | [casasparana.com.br](https://casasparana.com.br/) | Especialista em casas pré-fabricadas (atua em MG). | WordPress + Elementor + jQuery |
| 10 | **Real Casas Pré Fabricadas** | [realcasas.com.br](https://realcasas.com.br/) | Construtora de casas de madeira desde 2010. | Site muito leve / possivelmente SPA/JS |

---

## 2. Análise técnica comparativa

| Empresa | Tempo (ms) | Tamanho (KB) | Title otimizado? | Meta description? | H1 | Schema | FAQ detectado | Open Graph | Sitemap | robots.txt | llms.txt |
|---------|-----------:|-------------:|------------------|-------------------|-----|--------|---------------|------------|---------|------------|----------|
| Doce Lar de Madeira | 3.836 | 369,7 | Sim | Sim (cortada) | 0 | Nenhum | Sim | Sim | Sim | Sim | Ausente |
| Madecasa | 2.698 | 156,9 | Sim | Sim | 4* | Nenhum | Sim | Sim | Sim | Sim | Ausente |
| Chalé de Madeira | 1.818 | 108,2 | Sim | Sim | 0 | Nenhum | Sim | Sim | Sim | Sim | Ausente |
| Castor Casas | 2.858 | 109,3 | Sim | **Ausente** | 0 | Nenhum | Sim | **Não** | Sim | Sim | Ausente |
| Casa de Madeira HM | 2.033 | 269,4 | Sim | Sim | 0 | Nenhum | Sim | Sim | Sim | Sim | Ausente |
| Aliança Casas | 2.438 | 188,9 | Básico | **Ausente** | 0 | Nenhum | Sim | **Não** | Sim | Sim | Ausente |
| Casa & Campo | 2.482 | **3,5** | Sim | Sim | 0 | Nenhum | Não | Sim | **Não** | Sim | Ausente |
| Diamond House | 3.173 | 237,8 | Sim | Sim | 1 | **FAQPage** | Sim | Sim | Sim | Sim | Ausente |
| Casas Paraná | 1.150 | 147,2 | Sim | Sim (longa) | 0 | Nenhum | Sim | Sim | Sim | Sim | Ausente |
| Real Casas | 1.733 | **16,4** | Básico | Sim | 0 | Nenhum | Não | Sim | **Não** | Sim | Ausente |

\* H1s da Madecasa eram apenas números de etapa ("01.", "02.", "03.") — pouco semântico para SEO.

### Observações técnicas

- **Schema.org / Rich Snippets:** Apenas **Diamond House** implementou schema `FAQPage` na página inicial. Nenhum concorrente usa `LocalBusiness`, `Organization`, `Product` ou `BreadcrumbList` visíveis na home.
- **llms.txt:** Nenhum dos 10 sites possui `/llms.txt`.
- **H1:** A maioria não possui H1 na home (ou usa H1 sem valor semântico). Apenas Diamond House tem H1 descritivo.
- **Imagens / acessibilidade:** HM e Casas Paraná têm quase 0% de imagens com `alt`. Aliança e Chalé de Madeira se destacam com >90% de `alt text`.
- **Sitemap:** Casa & Campo e Real Casas não possuem `/sitemap.xml` acessível.
- **Velocidade:** todos carregam em 1,1s–3,8s no primeiro byte/render HTML. Casa & Campo e Real Casas são casos atípicos (conteúdo parece carregar via JS, pois o HTML bruto tem apenas 3,5KB e 16,4KB).

---

## 3. Design / experiência visual (estimativa)

| Empresa | Design | Justificativa |
|---------|--------|---------------|
| Doce Lar de Madeira | **Moderno médio** | Wix, responsivo, mas home sem H1 e pesada (370KB) |
| Madecasa | **Moderno** | Elementor, boa estrutura de headings, imagens otimizadas |
| Chalé de Madeira | **Moderno** | WordPress leve, imagens com alt, site limpo |
| Castor Casas | **Moderno** | Elementor, visual clean, mas falta meta description e OG |
| Casa de Madeira HM | **Moderno** | Elementor, muitas imagens (125), porém alt text negligenciado |
| Aliança Casas | **Moderno** | Elementor, bastante conteúdo (1.316 palavras), bom alt text |
| Casa & Campo | **Indefinido / leve** | HTML mínimo; pode ser site antigo ou SPA sem SSR |
| Diamond House | **Moderno** | Elementor + WooCommerce, mais completo, FAQ estruturado |
| Casas Paraná | **Moderno** | Elementor, rápido, porém headings fracos e alt text ausente |
| Real Casas | **Antigo / leve** | HTML mínimo, pouco conteúdo indexável, aparência provavelmente datada |

---

## 4. Otimização para IA / AEO (Answer Engine Optimization)

| Empresa | AEO Score | Pontos fortes | Pontos fracos |
|---------|-----------:|---------------|---------------|
| Doce Lar | 2/4 | FAQ detectado, meta desc | Sem H1, sem schema |
| Madecasa | 3/4 | Title/meta, FAQ, headings | Sem schema |
| Chalé de Madeira | 2/4 | Meta, FAQ, imagens otimizadas | Sem H1, sem schema |
| Castor Casas | 1/4 | FAQ detectado | Sem meta desc, sem H1, sem schema |
| Casa HM | 2/4 | Meta, FAQ | Sem H1, sem schema, alt text ruim |
| Aliança | 1/4 | Muito conteúdo, FAQ | Sem meta desc, sem H1, sem schema |
| Casa & Campo | 1/4 | Meta desc, OG | Sem FAQ, sem schema, sem sitemap |
| Diamond House | **4/4** | H1, FAQ, schema FAQPage, meta, OG | Poderia ter LocalBusiness/Product |
| Casas Paraná | 2/4 | Meta, FAQ | Sem schema, H1/alt fracos |
| Real Casas | 1/4 | Meta desc | Sem FAQ, sem schema, sem sitemap, pouco conteúdo |

**Conclusão AEO:** o nicho está **muito imaturo** em otimização para IA. Apenas um concorrente (Diamond House) usa schema de FAQ; nenhum tem `llms.txt`, schema `LocalBusiness`, `Organization` ou `BreadcrumbList` na home. Isso representa uma grande janela de oportunidade.

---

## 5. Oportunidades de diferenciação para um novo site

### 5.1 SEO técnico (baixa concorrência)
- Implementar **schema LocalBusiness + Organization + BreadcrumbList + FAQPage + Product/Service** desde o lançamento.
- Criar **sitemap.xml** e **robots.txt** otimizados, com URLs canônicas claras.
- Garantir **H1 único e semântico** em todas as páginas (meta problema do nicho).
- Otimizar **alt text** de 100% das imagens (HM e Casas Paraná falham aqui).
- Melhorar **Core Web Vitals**: vários sites usam Elementor com muitos scripts; um site mais enxuto (Next.js / Astro / WordPress otimizado) pode vencer em velocidade.

### 5.2 AEO / visibilidade em IA
- Criar **página `/llms.txt`** com dados estruturados sobre a empresa, modelos, preços, processo, diferenciais e FAQs.
- Desenvolver seção de **FAQ rica e bem estruturada** com schema JSON-LD (perguntas reais de clientes: preço, prazo, madeira, manutenção, financiamento, etc.).
- Produzir **conteúdo em formato de respostas diretas** para ser citado em respostas de IA (ChatGPT, Perplexity, Gemini).
- Adicionar **schema Speakable** e conteúdo conversacional nas páginas principais.

### 5.3 Conteúdo local
- Criar **landing pages específicas** para cidades-alvo: Lagoa Santa, Matozinhos, Belo Horizonte, Pedro Leopoldo, Sete Lagoas, Nova Lima, Contagem.
- Publicar **cases de obra com fotos, endereço aproximado, depoimentos em vídeo** e schema `Review`/`Testimonial`.
- Criar **comparativos honestos** (madeira vs. alvenaria, custo por m², tempo de obra) — conteúdo com alta intenção de busca e alto potencial de citação por IA.

### 5.4 Design e conversão
- Focar em **design moderno, fotografia de alta qualidade e navegação mobile-first** (o público busca muito no celular).
- Implementar **calculadora/cotador online** de casas por m² para captar leads qualificados.
- Incluir **chatbot de WhatsApp** bem posicionado (a maioria já tem WhatsApp, mas raramente integrado com automação).
- Criar **catálogo interativo de modelos** com filtros por metragem, quartos e preço estimado.

### 5.5 Estratégia de autoridade
- Construir **perfil no Google Business Profile** otimizado para cada região de atuação.
- Buscar **backlinks locais** (câmaras de dirigentes lojistas, associações de construção, prefeituras, blogs de arquitetura e turismo rural).
- Publicar **estudos de caso e guias** (ex.: "Quanto custa uma casa de madeira em MG em 2026?").

---

## 6. Resumo executivo

O mercado de casas de madeira em Minas Gerais é **digitalmente imaturo**. A maioria dos concorrentes usa WordPress + Elementor, tem sites visualmente aceitáveis, mas com **falhas básicas de SEO técnico e praticamente nenhuma otimização para motores de resposta/IA**. Apenas **Diamond House** se destaca com schema FAQPage. Nenhum concorrente possui `llms.txt`, schema LocalBusiness ou conteúdo estruturado para IA.

Um novo entrante pode se diferenciar rapidamente combinando:
1. **SEO técnico impecável** (H1, schema, sitemap, alt text, velocidade).
2. **AEO estruturado** (FAQ schema, llms.txt, conteúdo em formato de resposta).
3. **Estratégia local** (landing pages por cidade e Google Business Profile).
4. **Conversão** (calculadora, catálogo interativo, fotos/vídeos de obras reais).

---

*Arquivos gerados nesta pesquisa:*
- `research_competitors.py` — script de coleta de resultados nos buscadores.
- `analyze_competitors.py` — script de análise SEO/AEO técnica.
- `analyze_competitors_deep.py` — script de análise profunda de headings, imagens, OG, etc.
- `competitors_analysis.json` — dados brutos da análise técnica.
- `competitors_deep_analysis.json` — dados brutos da análise profunda.

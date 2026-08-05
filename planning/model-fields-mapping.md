# Mapeamento de Campos — Modelos de Casa

> Baseado na análise dos sites de referência: Castor (atual), Diamond House, Madecasa e Chalé de Madeira.

---

## 1. Resumo por concorrente

### Castor Casas (atual)
- **47 modelos** extraídos do site atual.
- Estrutura padrão por modelo:
  - Nome: "Casa de Madeira Modelo [País/Cidade]"
  - Área Coberta (Casa)
  - Área da Varanda
  - Área Total
  - Suítes
  - Quartos
  - Banheiros sociais
  - Lavanderia
  - Cozinha americana
  - Varanda
  - Galeria de imagens (7–9 fotos)
  - Destaque principal (1 imagem grande)
  - Aviso: "Os projetos são sugestões iniciais, podemos fazer um novo projeto..."
- Faixa de área total: **103,13 m² a 306,55 m²**.
- Todos os modelos têm cozinha americana e quase todos têm varanda.

### Chalé de Madeira
- Produto tipo "Kit pré-fabricado".
- Campos por modelo:
  - Nome: "Kit de Casa Pré-Fabricada Modelo [Nome] | Área m²"
  - Preço: "Sob consulta"
  - Área Construída
  - Área Total / Terreno recomendado (ex: 6 m x 25 m)
  - Medidas (ex: 5,00 m x 23,00 m)
  - Quartos
  - Banheiros
  - Garantia (ex: 15 anos)
  - Peso do Kit
  - Formas de pagamento
  - Vídeo do YouTube
  - Memorial descritivo (itens inclusos no kit)
  - Galeria de imagens

### Madecasa
- Páginas individuais de modelo (ex: /individual/, /individual02/, /individual03/).
- Campos por modelo:
  - Nome: "Tiradentes", "Governador Valadares"
  - Área útil
  - Área da cobertura
  - Fachada (largura em metros)
  - Lateral (profundidade em metros)
  - Opções de madeira: Tauri Champanhe, Angelim Pedra, Paraju Maçaranduba
  - Opções de telhado: claro / vermelho
  - Opções de janela: blindex / madeira
  - Imagens das variações
  - "Opinião do arquiteto" por tipo de madeira

### Diamond House
- Site bloqueado para scraping direto, mas é o único concorrente com **FAQPage schema**.
- Sugere importância de FAQ por modelo/página.

---

## 2. Campos obrigatórios sugeridos para o CMS (Strapi)

### Content-type: `house-model` (Modelo de Casa)

#### Identificação
| Campo | Tipo | Obrigatório | Observação |
|-------|------|:-----------:|-------------|
| `name` | String | Sim | Ex: "Modelo Brasil" |
| `slug` | UID | Sim | Baseado no nome |
| `tagline` | String | Não | Subtítulo curto |
| `description` | Rich text / Blocks | Sim | Descrição AEO do modelo |
| `short_description` | Text | Não | Resumo para cards |

#### Imagens
| Campo | Tipo | Obrigatório | Observação |
|-------|------|:-----------:|-------------|
| `featured_image` | Media (imagem) | Sim | Foto principal do modelo |
| `gallery` | Media (múltiplas) | Sim | Galeria de fotos |
| `floor_plan` | Media (imagem/PDF) | Não | Planta baixa |
| `video_url` | String (URL) | Não | YouTube/vídeo da obra |

#### Áreas e dimensões
| Campo | Tipo | Obrigatório | Observação |
|-------|------|:-----------:|-------------|
| `area_total_m2` | Decimal | Sim | Área total (casa + varanda) |
| `area_covered_m2` | Decimal | Sim | Área coberta interna |
| `area_balcony_m2` | Decimal | Não | Área de varanda |
| `area_util_m2` | Decimal | Não | Área útil (estilo Madecasa) |
| `area_roof_m2` | Decimal | Não | Área da cobertura |
| `facade_width_m` | Decimal | Não | Largura da fachada |
| `lateral_depth_m` | Decimal | Não | Profundidade lateral |
| `kit_dimensions` | String | Não | Ex: "5,00 m x 23,00 m" |

#### Cômodos e configuração
| Campo | Tipo | Obrigatório | Observação |
|-------|------|:-----------:|-------------|
| `bedrooms` | Integer | Sim | Número de quartos |
| `suites` | Integer | Não | Número de suítes |
| `bathrooms` | Integer | Sim | Banheiros sociais + suítes |
| `floors` | Integer | Sim | 1 ou 2 pavimentos |
| `has_laundry` | Boolean | Não | Possui lavanderia |
| `has_american_kitchen` | Boolean | Não | Cozinha americana |
| `has_balcony` | Boolean | Não | Possui varanda |
| `has_living_room` | Boolean | Não | Sala de estar |
| `has_dining_room` | Boolean | Não | Sala de jantar |
| `has_office` | Boolean | Não | Escritório |
| `has_pantry` | Boolean | Não | Despensa |
| `garage_spots` | Integer | Não | Vagas de garagem |

#### Acabamento e personalização
| Campo | Tipo | Obrigatório | Observação |
|-------|------|:-----------:|-------------|
| `wood_type` | Relation (wood-types) | Não | Tauri, Angelim Pedra, etc. |
| `roof_type` | Relation (roof-types) | Não | Telhado claro/vermelho |
| `window_type` | Relation (window-types) | Não | Blindex/madeira |
| `warranty_years` | Integer | Não | Garantia estrutural |
| `kit_weight_kg` | Decimal | Não | Peso do kit |

#### Comercial
| Campo | Tipo | Obrigatório | Observação |
|-------|------|:-----------:|-------------|
| `price_display` | String | Não | "Sob consulta" ou "A partir de R$ X" |
| `includes` | Rich text / Blocks | Não | Memorial descritivo / itens inclusos |
| `payment_methods` | Component | Não | Pix, boleto, cartão, financiamento |

#### Navegação e destaque
| Campo | Tipo | Obrigatório | Observação |
|-------|------|:-----------:|-------------|
| `categories` | Relation (categories) | Sim | 2 quartos, 3 quartos, 1 pavimento, etc. |
| `tags` | Relation (tags) | Não | Popular, Sob medida, etc. |
| `is_highlighted` | Boolean | Não | Destacar na home |
| `display_order` | Integer | Não | Ordem manual |
| `is_published` | Boolean | Sim | Publicado? |

#### SEO/AEO
| Campo | Tipo | Obrigatório | Observação |
|-------|------|:-----------:|-------------|
| `seo_title` | String | Não | Meta title |
| `seo_description` | Text | Não | Meta description |
| `seo_keywords` | String | Não | Keywords foco |
| `canonical_url` | String | Não | URL canônica |
| `faq` | Relation (faqs) | Não | FAQ específico do modelo |

---

## 3. Content-types auxiliares

### `category`
- `name`: String (ex: "2 Quartos", "1 Pavimento", "Chalés")
- `slug`: UID
- `description`: Rich text
- `type`: Enumeration (`room_count`, `floor_count`, `house_type`)
- `seo_title`, `seo_description`
- `display_order`: Integer

### `wood-type`
- `name`: String (ex: "Angelim Pedra")
- `slug`: UID
- `description`: Rich text
- `image`: Media
- `durability`: Text
- `architect_opinion`: Rich text

### `roof-type`
- `name`: String (ex: "Telhado Vermelho")
- `image`: Media

### `window-type`
- `name`: String (ex: "Janela Blindex")
- `image`: Media

### `faq`
- `question`: String
- `answer`: Rich text
- `category`: Relation
- `pages`: Relation (house-model, page, article)

---

## 4. Regras de inferência

- `bedrooms` deve incluir suítes: se um modelo tem "2 suítes", `bedrooms` é pelo menos 2.
- `bathrooms` = banheiros sociais + suítes.
- `area_total_m2` = `area_covered_m2` + `area_balcony_m2` (quando ambos existirem).
- Todo modelo deve ter pelo menos: nome, slug, featured_image, gallery, area_total_m2, bedrooms, bathrooms.

---

## 5. Exemplo migrado — Modelo Brasil (Castor)

| Campo | Valor |
|-------|-------|
| name | Casa de Madeira Modelo Brasil |
| slug | casa-de-madeira-modelo-brasil |
| area_total_m2 | 139,30 |
| area_covered_m2 | 97,87 |
| area_balcony_m2 | 41,43 |
| bedrooms | 3 |
| suites | 1 |
| bathrooms | 1 |
| has_laundry | true |
| has_american_kitchen | true |
| has_balcony | true |
| floors | 1 |
| categories | 3 Quartos, 1 Pavimento |

---

## 6. Próximos passos

1. Validar este mapeamento com a equipe Castor.
2. Criar os content-types no Strapi.
3. Migrar os 47 modelos existentes usando script de importação.
4. Criar FAQ por modelo.
5. Produzir descrições AEO únicas para cada modelo.

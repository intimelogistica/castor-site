# Arquitetura de Informação — Castor Casas de Madeira

## 1. Mapa de páginas

### Institucionais
- `/` — Home
- `/sobre` — Quem Somos
- `/como-funciona` — Processo de construção
- `/obras-realizadas` — Cases de obras
- `/depoimentos` — Depoimentos de clientes
- `/contato` — Contato
- `/localizacao` — Lojas/showroom (Lagoa Santa, Matozinhos)

### Catálogo
- `/modelos` — Todos os modelos
- `/modelos/[slug]` — Página de modelo individual
- `/modelos/2-quartos`, `/modelos/3-quartos`... — Filtros por quartos
- `/modelos/1-pavimento`, `/modelos/2-pavimentos`

### LPs de captura local
- `/casa-de-madeira-bh`
- `/casa-de-madeira-lagoa-santa`
- `/casa-de-madeira-matozinhos`
- `/casa-de-madeira-nova-lima`
- `/casa-de-madeira-pedro-leopoldo`
- `/casa-de-madeira-sete-lagoas`

### Base de conhecimento (blog/AEO)
- `/blog` — Lista de artigos
- `/blog/[slug]` — Artigo
- `/duvidas-frequentes` — FAQ geral

### Legado
- Redirects 301 do WordPress antigo para novas URLs.

## 2. Taxonomia

### Categorias de modelo
- Por quartos: 1 quarto, 2 quartos, 3 quartos, 4 quartos, 5 quartos
- Por pavimento: 1 pavimento, 2 pavimentos
- Por tipo: Casa, Chalé, Sobrado, Loft

### Tags
- Popular, Sob medida, Compacta, Familiar, Com varanda, Com lavanderia

## 3. Keyword map (primeira camada)

| Página | Keyword principal | Intenção |
|--------|-------------------|----------|
| Home | casas de madeira mg | Transacional |
| /modelos | modelos de casas de madeira | Navegacional |
| /modelos/brasil | casa de madeira modelo brasil 139m2 | Transacional |
| /sobre | construtora de casas de madeira bh | Institucional |
| /obras-realizadas | obras casas de madeira mg | Prova social |
| /contato | orçamento casa de madeira | Transacional |
| /casa-de-madeira-bh | casa de madeira belo horizonte | Local |
| /casa-de-madeira-lagoa-santa | casa de madeira lagoa santa | Local |
| /blog/custo-m2 | quanto custa casa de madeira mg | Informacional |
| /blog/madeira-vs-alvenaria | casa de madeira vs alvenaria | Informacional |

## 4. Componentes principais

- Header fixo com CTA WhatsApp
- Hero com headline + CTA
- Filtro/catálogo de modelos
- Card de modelo (imagem, nome, área, quartos, banheiros, CTA)
- Formulário de orçamento
- Depoimentos
- FAQ accordion
- Footer
- WhatsApp float

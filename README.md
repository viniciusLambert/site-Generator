# 📝 Site Generator

Um gerador de sites estáticos elegante e robusto desenvolvido em Python com **Programação Orientada a Objetos**, capaz de transformar arquivos Markdown em páginas HTML totalmente formatadas.

## ✨ Características

- 🔄 **Conversão Markdown → HTML**: Transforma arquivos `.md` em páginas HTML completas
- 🏗️ **Arquitetura Limpa**: Estrutura baseada em Domain-Driven Design (DDD)
- 📁 **Geração Recursiva**: Processa diretórios inteiros mantendo a estrutura de pastas
- 🎨 **Sistema de Templates**: Suporte a templates HTML customizáveis
- 🖼️ **Gerenciamento de Assets**: Copia automaticamente arquivos estáticos (CSS, imagens, etc.)
- ⚡ **OOP Puro**: Código orientado a objetos, modular e testável
- ✅ **Testado**: Suite completa de testes unitários

## 🎯 Markdown Suportado

O gerador suporta os seguintes elementos Markdown:

- **Cabeçalhos** (`#`, `##`, `###`, etc.)
- **Negrito** (`**texto**`) e **Itálico** (`*texto*`)
- **Links** (`[texto](url)`)
- **Imagens** (`![alt](src)`)
- **Citações** (`> texto`)
- **Listas ordenadas** e **não-ordenadas**
- **Blocos de código** (` ```código``` `)
- **Código inline** (`` `código` ``)

## 🏛️ Arquitetura

O projeto segue princípios de **Clean Architecture** com separação clara de responsabilidades:

```
src/
├── domain/              # Entidades e tipos de domínio
│   ├── text_node.py     # Representação de nós de texto
│   ├── html_node.py     # Nós HTML abstratos
│   ├── leaf_node.py     # Nós folha (elementos sem filhos)
│   ├── parent_node.py   # Nós pai (elementos com filhos)
│   └── text_type.py     # Enumeração de tipos de texto
│
├── usecases/            # Casos de uso e lógica de negócio
│   ├── converter/       # Conversores Markdown → HTML
│   ├── markdown_parser/ # Parsers de Markdown
│   └── generator/       # Geradores de páginas
│
└── infrastructure/      # Infraestrutura e I/O
    └── copy_static_to_public.py
```

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone <seu-repositorio>
cd site-Generator
```

2. Certifique-se de ter Python 3 instalado:
```bash
python3 --version
```

## 📖 Uso

### Geração Básica

Execute o gerador de sites:

```bash
./main.sh
```

Ou manualmente:

```bash
PYTHONPATH=src python3 src/main.py
```

### Geração com Servidor Local

Para visualizar o site gerado com servidor HTTP local:

```bash
./main.sh
# Acesse http://localhost:8888 no navegador
```

### Estrutura de Diretórios

```
.
├── content/         # Seus arquivos Markdown (.md)
├── template.html    # Template HTML para as páginas
├── static/          # Arquivos estáticos (CSS, imagens)
└── docs/            # Site gerado (HTML de saída)
```

### Exemplo de Uso

1. Coloque seus arquivos Markdown em `content/`:
```markdown
# Meu Primeiro Post

Olá, este é um **texto em negrito** e este é *itálico*.

## Links e Imagens

[Visite meu site](https://example.com)

![Descrição da imagem](/images/foto.png)
```

2. Personalize o `template.html`:
```html
<!doctype html>
<html>
  <head>
    <title>{{ Title }}</title>
    <link href="/index.css" rel="stylesheet" />
  </head>
  <body>
    <article>{{ Content }}</article>
  </body>
</html>
```

3. Execute o gerador:
```bash
./main.sh
```

4. O HTML será gerado em `docs/` com a mesma estrutura de `content/`

## 🏗️ Como Funciona

### Pipeline de Conversão

```
Markdown File → Text Nodes → HTML Nodes → HTML String → HTML File
```

1. **Parsing**: O arquivo Markdown é lido e dividido em blocos
2. **Tokenização**: Cada bloco é convertido em `TextNode`s
3. **Conversão**: `TextNode`s são transformados em `HTMLNode`s
4. **Renderização**: `HTMLNode`s geram HTML válido
5. **Template**: O HTML é injetado no template
6. **Saída**: Arquivo HTML final é escrito em disco

## 🧪 Testes

Execute a suite de testes:

```bash
./test.sh
```

Ou manualmente:

```bash
PYTHONPATH=src python3 -m pytest tests/
```

### Cobertura de Testes

O projeto inclui testes para:
- ✅ Nós de domínio (TextNode, HTMLNode, LeafNode, ParentNode)
- ✅ Conversores de Markdown
- ✅ Parsers de blocos
- ✅ Extratores de metadados
- ✅ Pipeline completo de geração

## 📁 Estrutura do Projeto

```
site-Generator/
├── src/
│   ├── domain/              # Entidades de domínio
│   ├── usecases/            # Lógica de negócio
│   ├── infrastructure/      # I/O e infraestrutura
│   └── main.py             # Ponto de entrada
├── tests/                   # Testes unitários
├── content/                 # Conteúdo Markdown (entrada)
├── static/                  # Assets estáticos
├── docs/                    # Site gerado (saída)
├── template.html            # Template HTML base
├── main.sh                  # Script de execução
└── test.sh                  # Script de testes
```

## 🎨 Personalização

### Modificar o Template

Edite `template.html` para customizar o layout. Use as variáveis:
- `{{ Title }}` - Substituído pelo título extraído do Markdown
- `{{ Content }}` - Substituído pelo HTML gerado

### Adicionar Estilos

Coloque seus arquivos CSS em `static/` e eles serão copiados automaticamente para `docs/`.

## 🛠️ Tecnologias

- **Python 3** - Linguagem principal
- **OOP** - Paradigma de programação orientada a objetos
- **Clean Architecture** - Separação de responsabilidades
- **Pytest** - Framework de testes (recomendado)

## 📝 Licença

Este projeto foi desenvolvido como parte do curso [Build a Static Site Generator](https://www.boot.dev/courses/build-static-site-generator-python) da [Boot.dev](https://www.boot.dev).

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se livre para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abrir um Pull Request

---

Desenvolvido com ❤️ usando IA somente para consulta.

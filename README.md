# Vector Search & Custom Ranking Engine

Este repositório contém a implementação do núcleo de processamento e ranqueamento de um Banco de Dados Vetorial (VectorDB). O motor foi projetado para simular o comportamento de sistemas de Busca Semântica de alta performance, comumente integrados a arquiteturas RAG (Retrieval-Augmented Generation).

O objetivo principal do projeto é calcular o alinhamento conceitual entre uma consulta (query) do usuário e documentos indexados, aplicando regras de negócio dinâmicas para reordenar os resultados.

---

## Engenharia Reversa e Abordagem Matemática

Diferente de uma busca tradicional por palavras-chave, este motor processa Embeddings (vetores de dimensão 5 que representam o significado semântico dos textos).

A arquitetura final foi deduzida através do isolamento de variáveis e modelagem matemática de cenários de teste reais:

1. Proximidade Semântica Base: Utiliza a Similaridade de Cosseno para calcular o ângulo entre o vetor da consulta e os vetores candidatos no espaço multidimensional.

2. Fator de Normalização Dinâmico: Identificou-se que o motor aplica uma divisão do score pela Norma Infinita (L∞) do vetor da consulta. Em código, isso se traduz como o maior valor absoluto contido na query:
   max(abs(q) for q in query)

3. Penalização de Escopo: Uma regra de conformidade foi mapeada no backend: documentos cujo primeiro elemento do embedding seja negativo (vetor[0] < 0) sofrem uma penalização severa, tendo seu score final dividido pela constante 3.0.

---

## Estrutura do Projeto

O código foi estruturado seguindo as melhores práticas de desenvolvimento, separando as regras de negócio dos ambientes de validação:

├── src/
│   └── pipeline.py       # Núcleo do algoritmo de busca e ordenação
├── tests/
│   └── test_pipeline.py  # Suíte de testes automatizados com dados reais
└── .gitignore            # Proteção contra versionamento de caches do Python

---

## Tecnologias e Execução

O motor foi construído utilizando Python 3.10+ de forma pura, contando exclusivamente com o módulo nativo math. Esta abordagem garante dependência zero de bibliotecas externas, assegurando portabilidade, tempos de resposta previsíveis e execução extremamente leve.

### Como rodar os testes locais

Para garantir a confiabilidade do motor contra cenários de dados puramente positivos ou com variações negativas, execute a suíte de testes integrada diretamente no terminal:

python -m unittest tests/test_pipeline.py

---

## Como subir este repositório para o GitHub

Caso ainda não tenha configurado o repositório remoto, execute os comandos abaixo dentro da pasta do projeto:

# Adiciona a URL do repositório remoto
git remote add origin https://github.com/cassiobrito708/vector-search-ranking-engine.git

# Renomeia a branch principal para 'main' (se necessário)
git branch -M main

# Envia o código para o GitHub
git push -u origin main --force

Atencao: Certifique-se de que o repositorio vector-search-ranking-engine ja foi criado no seu GitHub antes de executar o push.

---

## Contato

Desenvolvido por Cassio Brito
Acompanhe meus projetos ou entre em contato pelo meu perfil do GitHub: https://github.com/cassiobrito708

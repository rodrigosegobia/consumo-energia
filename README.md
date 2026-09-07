# ⚡ Calculadora de Consumo Elétrico Inteligente

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-181717?style=for-the-badge&logo=github&logoColor=white)
![Energia](https://img.shields.io/badge/Energia-Elétrica-FFD700?style=for-the-badge&logo=flash&logoColor=black)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

## 📌 Sobre o projeto

A **Calculadora de Consumo Elétrico Inteligente** é um programa em **Python**
criado para ajudar qualquer pessoa a estimar quanto um aparelho eletrônico
consome de energia por mês, a partir de informações simples de uso no dia a dia.

O objetivo é tornar visível — de forma rápida e didática — o impacto que
aparelhos como geladeiras, ventiladores, chuveiros e televisores têm na
conta de luz, incentivando o consumo consciente de energia. 💡🌱

## 🐍 Linguagem utilizada

- **Python 3**

## 🧮 Fórmula utilizada

O consumo mensal (em kWh) é calculado a partir da potência do aparelho (W)
e do tempo médio de uso diário (h):

```
consumoMensal = (potencia * horasDia * 30) / 1000
```

Além disso, o programa estima o **custo mensal em reais**, multiplicando o
consumo pelo valor fixo de **R$ 0,75 por kWh**:

```
custoEstimado = consumoMensal * 0.75
```

## ▶️ Como executar o programa

1. Certifique-se de ter o **Python 3** instalado na sua máquina.
2. Clone este repositório:
   ```bash
   git clone https://github.com/rodrigosegobia/consumo-energia.git
   ```
3. Acesse a pasta do projeto:
   ```bash
   cd consumo-energia
   ```
4. Execute o programa:
   ```bash
   python app.py
   ```
5. Informe o nome do aparelho, a potência (em watts) e as horas médias de
   uso diário quando solicitado.

## 🖥️ Exemplo de uso

```
Digite o nome do aparelho: Geladeira
Digite a potencia do aparelho em watts (W): 62.5
Digite o tempo medio de uso diario em horas: 24

Aparelho: Geladeira
Consumo estimado: 45.0 kWh/mes
Custo estimado: R$ 33.75 por mes
```

## 🗂️ Estrutura do projeto

```
projetos/
└── consumo-energia/
    ├── app.py
    └── README.md
```

## 👨‍💻 Autor

Projeto desenvolvido como parte de um programa de iniciação em tecnologia,
com foco em lógica de programação e boas práticas de versionamento com Git
e GitHub.
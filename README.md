# Classificador de Imagens de Cães e Gatos 🐶🐱

Este projeto utiliza uma Rede Neural Convolucional (CNN) para classificar imagens de cães e gatos. Ele é desenvolvido em Python utilizando TensorFlow e Keras, com o objetivo de distinguir entre as duas classes de animais em imagens.

## Índice

1. [Sobre o Projeto](#sobre-o-projeto)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Instalação](#instalação)
4. [Como Usar](#como-usar)
5. [Arquitetura do Modelo](#arquitetura-do-modelo)
6. [Resultados](#resultados)
7. [Contribuição](#contribuição)
8. [Contato](#contato)
9. [Licença](#licença)

---

## Sobre o Projeto

Este projeto é um classificador de imagens que distingue entre cães e gatos usando Deep Learning. O objetivo é utilizar uma rede neural convolucional (CNN) para treinar o modelo com um conjunto de dados de imagens, permitindo que ele identifique as características visuais de cães e gatos.

## Tecnologias Utilizadas

As principais tecnologias e bibliotecas usadas neste projeto são:

- **Python**: Linguagem principal usada para a implementação.
- **TensorFlow/Keras**: Framework de Deep Learning utilizado para construir e treinar a CNN.
- **ImageDataGenerator**: Recurso da Keras para a geração e pré-processamento de imagens.

## Instalação

### Pré-requisitos

Certifique-se de ter o Python instalado e as dependências necessárias listadas no `requirements.txt`.

### Passos de Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/classificador-caes-gatos.git
2. Acesse o diretório do projeto:
   ```bash
   cd classificador-caes-gatos
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
4. Adicione seu conjunto de dados nas pastas ```dataset/training_set``` e ```dataset/test_set``` com as imagens organizadas em subdiretórios ```cats``` e ```dogs```.

## Como Usar
**Para treinar o modelo:**  
  - Execute o script principal para iniciar o treinamento da rede neural:
    ```bash
    python classi.py    
  - O modelo treinado será salvo como ```classifica_cachorro_gato.h5```, Você pode usá-lo para prever novas imagens com o script
    ```bash
    python testador.py
  
## Arquitetura do Modelo
O modelo utilizado é uma Rede Neural Convolucional (CNN) composta pelas seguintes camadas:
- Camadas Convolucionais: Extraem características das imagens (bordas, texturas, etc.)
- Camadas de Pooling: Reduzem a dimensionalidade das características extraídas, mantendo informações relevantes.
- Camadas Densas: Classificam as imagens com base nas características extraídas pelas camadas convolucionais.

**Arquitetura em detalhes**
    ```bash
    
    Conv2D(32 filtros, tamanho 3x3, ReLU)
    MaxPooling2D(pool size 2x2)
    
    Conv2D(64 filtros, tamanho 3x3, ReLU)
    MaxPooling2D(pool size 2x2)
      
    Conv2D(128 filtros, tamanho 3x3, ReLU)
    MaxPooling2D(pool size 2x2)
    
    Flatten
    Dense(512 unidades, ReLU)
    Dropout(0.5)
    Dense(1 unidade, Sigmoid)  # Para classificação binária

## Resultados
Acurácia no Conjunto de Teste  
Após o treinamento, o modelo foi avaliado utilizando um conjunto de dados separado. A acurácia final obtida foi 74.04%.

## Licença
- Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.

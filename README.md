#Classificador de Imagens de Cães e Gatos 🐶🐱 
Este projeto utiliza uma rede neural convolucional (CNN) para classificar imagens.

Carregamento e preparação dos dados:

As imagens são organizadas em diretórios para treino e teste. 
Um gerador de imagens (ImageDataGenerator) é usado para redimensionar as imagens e normalizar os valores dos pixels.  

Construção do modelo: 

Uma CNN é projetada com várias camadas convolucionais, pooling e densas, permitindo que o modelo aprenda a reconhecer padrões visuais característicos de cães e gatos.  

Treinamento e validação: 

O modelo é treinado utilizando as imagens de treinamento e validado com um conjunto de validação.  
Durante o treinamento, o modelo ajusta seus pesos para minimizar o erro de classificação.  

Avaliação:  

O desempenho do modelo é testado com um conjunto de dados separado (conjunto de teste) para medir sua acurácia em imagens que ele nunca viu.  

Salvamento do modelo:  

Após o treinamento, o modelo treinado é salvo para que possa ser reutilizado posteriormente.  

Previsão em novas imagens:  

O modelo salvo pode ser carregado para realizar previsões em novas imagens. Essas imagens são redimensionadas e normalizadas antes de o modelo prever se elas contêm um cachorro ou gato, com uma estimativa de confiança.  

##ACURÁCIA: 74.04%

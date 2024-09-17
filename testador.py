import tensorflow as tf
from tensorflow.keras.preprocessing import image # type: ignore
import numpy as np

# Carregar o modelo salvo
model = tf.keras.models.load_model('classifica_cachorro_gato.h5')

# Carregar a imagem
img_path = 'input_img/cat/cat_56.jpg'
img = image.load_img(img_path, target_size=(150, 150))  # Redimensionar para o tamanho que a rede espera

# Converter a imagem para array NumPy
img_array = image.img_to_array(img)

# Normalizar os valores (igual ao pré-processamento do treinamento)
img_array = img_array / 255.0

# Adicionar uma dimensão para representar o batch (batch_size = 1)
img_array = np.expand_dims(img_array, axis=0)

# Fazer a previsão
prediction = model.predict(img_array)

# Interpretar o resultado
if prediction[0] > 0.5:
    print(f"É um cachorro! Confiança: {prediction[0][0] * 100:.2f}%")
else:
    print(f"É um gato! Confiança: {(1 - prediction[0][0]) * 100:.2f}%")

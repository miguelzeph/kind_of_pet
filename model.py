import tensorflow as tf

# LOAD
model = tf.keras.models.load_model('./pet_model.h5')

def predicoes(path):
    # Abrir IMG
    sample_image = tf.keras.preprocessing.image.load_img(r'./some_img_for_test/'+str(path),
                                                    target_size=(224,224))
    plt.imshow(sample_image)
    # Img to Array
    sample_image = tf.keras.preprocessing.image.img_to_array(sample_image)
    # Colocar no formado (1,224,224,3)
    sample_image = np.expand_dims(sample_image,axis=0)
    # Normalizar de acordo com o Resnet50
    sample_image = tf.keras.applications.resnet50.preprocess_input(sample_image)
    # prever
    predictions = model.predict(sample_image)
    
    #return predictions
    
    saida = {
        'birds':   predictions[0][0],
        'cats':    predictions[0][1],
        'dogs':    predictions[0][2],
        'fishs':   predictions[0][3],
        'hamsters':predictions[0][4],
        'monkeys': predictions[0][5],
        'reptiles':predictions[0][6],
    }
    return saida

# Predict
#predicoes('cat.1.jpg')
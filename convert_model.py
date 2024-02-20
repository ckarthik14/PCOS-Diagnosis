from keras.models import load_model
import tensorflowjs as tfjs

loaded_model = load_model('model1.keras')

tfjs.converters.save_keras_model(loaded_model, "./")
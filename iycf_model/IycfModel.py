from pyexpat import model


from tensorflow.keras.models import load_model
import os

class IycfModel():
    def __init__(self, model, model_dir='ML_MODELS'):
        self.model=model
        self.model_dir = model_dir
        
    def get_model(self):
        return load_model(os.path.join(self.model_dir, self.model))

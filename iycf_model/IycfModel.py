from numpy.lib.shape_base import expand_dims
from tensorflow.keras.utils import get_file, load_img, img_to_array
from tensorflow.keras.models import load_model
from tensorflow.nn import softmax
from numpy import argmax, max, array
import os

class IycfModel():
    def __init__(self, model, model_dir='ML_MODELS'):
        self.model=model
        self.model_dir = model_dir
        self.class_predications = array(['123123', '607000', '607001'])
        
    # def get_model(self):
    #     return load_model(os.path.join(self.model_dir, self.model))

    def predict_class(self, image):
        img_path = os.path.join('files', '607000', image)
        img = load_img(img_path, target_size= (128,128))
        img_array = img_to_array(img)
        img_array = expand_dims(img_array, 0)
        model = load_model(os.path.join(self.model_dir, self.model))
        pred = model.predict(img_array)
        score = softmax(pred[0])
        class_prediction = self.class_predictions[argmax(score)]
        model_score = round(max(score) * 100, 2)

        return {
            "model-prediction": class_prediction,
            "model-prediction-confidence-score": model_score
            }
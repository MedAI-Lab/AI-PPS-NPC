

from tensorflow import keras
from tensorflow.keras.applications.efficientnet import EfficientNetB7, preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from tensorflow.keras.utils import to_categorical


# CNN applied for deep feature extractor
base_model = EfficientNetB7(include_top=False, weights='imagenet')
model = Model(inputs=base_model.input, outputs=base_model.get_layer('block7d_add').output)
model.summary()

#-- See the paper for implementation details
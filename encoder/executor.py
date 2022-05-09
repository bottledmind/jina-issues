import tensorflow as tf
from jina import Executor, requests
from docarray import DocumentArray, Document


class EncodingExecutor(Executor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.model = tf.keras.models.load_model('encoder/model')
        # self.model = tf.keras.models.load_model('model')
        # m = tf.keras.applications.EfficientNetB0(include_top=False, input_shape=(224, 224, 3))
        # self.model = tf.keras.models.Sequential([
        #     m,
        #     tf.keras.layers.GlobalMaxPool2D()
        # ])

    @requests
    def encode(self, docs: 'DocumentArray', **kwargs):
        docs.embed(self.model, to_numpy=True)
        for doc in docs[...]:
            doc.pop('tensor')

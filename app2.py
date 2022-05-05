from docarray import Document, DocumentArray
import tensorflow as tf

inputs = DocumentArray([
    Document(uri='./resources/cat1.jpg'),
    Document(uri='./resources/dog1.jpg')
])

inputs.apply(lambda doc: doc.load_uri_to_image_tensor(224, 224))

index_docs = DocumentArray([
    Document(uri='./resources/cat2.jpg'),
    Document(uri='./resources/dog2.png')
])
index_docs.apply(lambda doc: doc.load_uri_to_image_tensor(224, 224))

strategy = tf.distribute.get_strategy()
physical_devices = tf.config.experimental.list_physical_devices('GPU')

for device in physical_devices:
    tf.config.experimental.set_memory_growth(device, True)

with strategy.scope():
    model1 = tf.keras.models.load_model('encoder/executor/model')
    model2 = tf.keras.models.load_model('encoder/executor/model')
    model3 = tf.keras.models.load_model('encoder/executor/model')
    model4 = tf.keras.models.load_model('encoder/executor/model')
    model5 = tf.keras.models.load_model('encoder/executor/model')

for i in range(1000):
    inputs.embed(model1)
    index_docs.embed(model2)
    inputs.embed(model3)
    index_docs.embed(model4)
    inputs.embed(model5)
    print(i)

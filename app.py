from docarray import Document, DocumentArray
from jina import Flow

from encoder.executor.encoding_executor import EncodingExecutor
from index.index_executor import IndexExecutor
from preprocessing.preprocessing_executor import PreprocessingExecutor

inputs = DocumentArray([
    Document(uri='./resources/cat1.jpg'),
    Document(uri='./resources/dog1.jpg')
])
index_docs = DocumentArray([
    Document(uri='./resources/cat2.jpg'),
    Document(uri='./resources/dog2.png')
])

f = Flow(protocol='http', port=8080) \
    .add(uses=PreprocessingExecutor) \
    .add(uses=EncodingExecutor, replicas=5) \
    .add(uses=IndexExecutor)

# f = Flow(protocol='http', port=8080) \
#     .add(uses=PreprocessingExecutor) \
#     .add(uses='docker://my_containerized_executor:latest') \
#     .add(uses=IndexExecutor)

with f:
    # f.block()
    f.post('index', index_docs)
    for i in range(1000):
        f.post('search', inputs)
        print(i)

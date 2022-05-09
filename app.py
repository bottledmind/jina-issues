from docarray import Document, DocumentArray
from jina import Flow

from encoder.executor import EncodingExecutor
from index.index_executor import IndexExecutor
from preprocessing.executor import PreprocessingExecutor

inputs = DocumentArray([
    Document(uri='./resources/cat1.jpg'),
    Document(uri='./resources/dog1.jpg')
])
index_docs = DocumentArray([
    Document(uri='./resources/cat2.jpg'),
    Document(uri='./resources/dog2.png')
])

f = Flow(protocol='http', port=8080) \
    .add(uses='docker://preprocessing:latest') \
    .add(uses=EncodingExecutor) \
    .add(uses=IndexExecutor)

with f:
    f.block()

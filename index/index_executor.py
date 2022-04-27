import os
from jina import Executor, requests
from docarray import DocumentArray


class IndexExecutor(Executor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._da = DocumentArray()

    @requests(on='/index')
    def add(self, docs: 'DocumentArray', **kwargs):
        self._da.extend(docs)
        docs.clear()
        print(docs)

    @requests(on='/clear')
    def clear(self, **kwargs):
        self._da.clear()

    @requests(on='/search')
    def search(self, docs: 'DocumentArray', **kwargs):
        docs.match(self._da, metric='euclidean')
        # del docs[...][:, 'embedding']
        # print(len(list(1 for doc in docs[...] if doc.embedding is not None)))
        list(docs[...].map(lambda doc: doc.pop('embedding')))
        # for doc in docs[...]:
        #     doc.pop('embedding')
        # for doc in docs[...]:
        #     print(doc.embedding)\

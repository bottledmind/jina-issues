import os
from jina import Executor, requests
from docarray import DocumentArray


def add_name(doc: 'Document'):
    doc.tags['name'] = os.path.basename(doc.uri)
    return doc


class PreprocessingExecutor(Executor):
    @requests
    def preprocess(self, docs: 'DocumentArray', **kwargs):
        docs.apply(lambda doc: doc.load_uri_to_image_tensor(224, 224))
        docs.apply(add_name)
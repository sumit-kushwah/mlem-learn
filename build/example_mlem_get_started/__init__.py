import os

from mlem.core.metadata import load_meta

model = load_meta(os.path.join(os.path.dirname(__file__), "model"), load_value=True)

def _create_method(name):
    def method(*args, **kwargs):
        return getattr(model, name)(*args, **kwargs)
    method.__name__ = name
    return method


predict = _create_method("predict")

predict_proba = _create_method("predict_proba")

sklearn_predict = _create_method("sklearn_predict")

sklearn_predict_proba = _create_method("sklearn_predict_proba")

# evaluate.py
import json

from sklearn import metrics
from sklearn.datasets import load_iris

from mlem.api import apply


def main():
    data, y_true = load_iris(return_X_y=True, as_frame=True)
    y_pred = apply("rf", data, method="predict_proba")
    roc_auc = metrics.roc_auc_score(y_true, y_pred, multi_class="ovr")

    with open("metrics.json", "w") as fd:
        json.dump({"roc_auc": roc_auc}, fd, indent=4)



if __name__ == "__main__":
    main()
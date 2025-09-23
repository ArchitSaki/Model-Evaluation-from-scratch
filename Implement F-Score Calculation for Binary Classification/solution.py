import numpy as np

def f_score(y_true, y_pred, beta=1, pos_label=1):
    """
    Calculate F-beta Score for binary classification.
    
    Parameters
    ----------
    y_true : list or numpy array
        Ground truth labels
    y_pred : list or numpy array
        Predicted labels
    beta : float, default=1
        Weight of recall in the harmonic mean (beta=1 → F1-score)
    pos_label : int or str, default=1
        The class to treat as positive
    
    Returns
    -------
    float : F-beta score (rounded to 3 decimals)
    """

    tp, fp = 0, 0
    for yt, yp in zip(y_true, y_pred):
        if yp == pos_label:
            if yt == yp:
                tp += 1
            else:
                fp += 1
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0

    
    tp, fn = 0, 0
    for yt, yp in zip(y_true, y_pred):
        if yt == pos_label:
            if yp == yt:
                tp += 1
            else:
                fn += 1
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0

    
    if precision == 0 and recall == 0:
        return 0.0
    fbeta = (1 + beta**2) * (precision * recall) / ((beta**2 * precision) + recall)
    return round(fbeta, 3)

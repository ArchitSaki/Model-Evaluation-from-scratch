tp, fp = 0, 0  # initialize counts

    for yt, yp in zip(y_true, y_pred):
        if yp == pos_label:       # only look at predicted positives
            if yt == yp:          # true positive
                tp += 1
            else:                 # false positive
                fp += 1

    # handle case where denominator is zero
    if tp + fp == 0:
        return 0.0

    return tp / (tp + fp)

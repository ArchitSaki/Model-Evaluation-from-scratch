def recall(y_true, y_pred, pos_label=1):

    tp, fn = 0, 0  # initialize counts

    for yt, yp in zip(y_true, y_pred):
        if yt == pos_label:       # only look at actual positives
            if yp == yt:          # true positive
                tp += 1
            else:                 # false negative
                fn += 1

    # handle case where denominator is zero
    if tp + fn == 0:
        return 0.0

    return tp / (tp + fn)


def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
	tp,fp,tn,fn=0,0,0,0
    for yt,yp in zip(actual,predicted):
        if yt==1 and yp==1:
            tp+=1
        if yt==0 and yp==1:
            fp+=1
        if yt==0 and yp==0:
            tn+=1
        if yt==1 and yp==0:
            fn+=1
    confusion_matrix=[[tp,fn],[fp,tn]]
    accuracy=(tp+tn)/(tp+tn+fp+fn)
    precision=tp/(tp+fp)
    recall=tp/(fn+tp)
    negativePredictive=tn/(tn+fn)
    specificity=tn/(tn+fp)
    f1=2*((precision*recall)/(precision+recall))

	return confusion_matrix, round(accuracy, 3), round(f1, 3), round(specificity, 3), round(negativePredictive, 3)

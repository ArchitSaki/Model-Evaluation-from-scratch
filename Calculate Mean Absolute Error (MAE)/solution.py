import numpy as np

def mae(y_true, y_pred):
	"""
	Calculate Mean Absolute Error between two arrays.

	Parameters:
	y_true (numpy.ndarray): Array of true values
    y_pred (numpy.ndarray): Array of predicted values

	Returns:
	float: Mean Absolute Error rounded to 3 decimal places
	"""
    sum=0
    n=len(y_true)
    
    try:
        m = len(y_true[0])
    except TypeError:
        m = 1

    if m < 2:
        for yt,yp in zip(y_true,y_pred):
            sum+=abs(yt-yp)
        val=sum/n
    else:
        for y_row,y_row_p in zip(y_true,y_pred):
            if len(y_row) != len(y_row_p):
                raise ValueError("Number of output features must match")
            for yt,yp in zip(y_row,y_row_p):

                sum+=abs(yt-yp)

	    val=sum/(n*m)
	return round(val,3)

import math

def log_softmax(x):
    max_x = max(x)  
    exp_shifted = [math.exp(val - max_x) for val in x]
    sum_exp = sum(exp_shifted)
    log_sum_exp = math.log(sum_exp)
    
    return [(val - max_x) - log_sum_exp for val in x]

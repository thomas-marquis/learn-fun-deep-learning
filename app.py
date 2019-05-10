import math as m
import statistics as stats


class Formal_neron:
    def __init__(self, 
                 weight=[], 
                 agregate_params=[],
                 activate_params=[],
                 agregate=lambda y: None, 
                 activate=lambda y: 0):
        self.weight = weight
        self.agregate_params = agregate_params
        self.activate_params = activate_params
        self.agregate = agregate
        self.activate = activate
    
    def process(self, x_vect=[]):
        y = self.agregate(x_vect, self.weight, *self.agregate_params)
        
        return self.activate(y, *self.activate_params)
    
    
def agregate(x_vect, weight, b=0):
    y = 0
    for idx, x in enumerate(x_vect):
        y += weight[idx] * x
    
    return y + b


def activate_factory(threshold):
    def activate(y, a=0):
        sigm = m.pow((1 + m.exp(-a * y)), -1)
        print(y, sigm)
        
        return sigm > threshold
    
    return activate


def loss_0_1_function(y_actual, y_expected):
    return 1 if y_actual == y_expected else 0


def loss_hinge_function(y_actual, y_expected):
    return max([0, 1 - (y_actual * y_expected)])


def loss_cross_entropy_function(y_actual, y_expected):
    return 


def loss_average_function(y_actual_vect, y_expected_vect, loss=lambda y1, Y2: 0):
    if len(y_actual_vect) != len(y_expected_vect):
        raise Exception("Both y vect must have same length")
    
    return stats.mean([loss(y_actual, y_expected_vect[idx]) 
                       for idx, y_actual in enumerate(y_actual_vect)])


print("execution started")

data_vect = range(10)

neron_1 = Formal_neron(
        weight=[1 for i in range(10)],
        agregate=agregate,
        activate=activate_factory(0.5),
        agregate_params=[0])

res = neron_1.process(data_vect)

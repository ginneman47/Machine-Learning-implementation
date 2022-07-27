#adaline - gradient descent rule learning implementation for ANDNOT gate truth table as an input example.


import math as meth
import numpy as np

inputX = [1,1,-1,-1];
inputY = [1,-1,1,-1];
output = [-1,1,-1,-1];

inputLength = len(inputX);
theta = 0.2;
bias = 0.2;
yin=0;
replace=0;
isErrorZero = False;
isDelW1Zero = False;
isDelW2Zero = False;
epoch = 0;

class Perceptron:
    
    def __init__(self):
        self.thisWeight1 = 0.2;
        self.thisWeight2 = 0.2;
        self.delWeight1 = 0;
        self.delWeight2 = 0;
        self.delBias = 0;
        self.sumWeighted=0;
        
    def sigmoid(self,x):
        return 1/1-np.exp(-x);
    def binarySigmoid(x):
        return (1-np.exp(-x))/(1+np.exp(-x));
        
    def weightedSum(self):
        global yin;
        global replace;
        global epoch;
        for i in range(0,inputLength):
            self.sumWeighted = inputX[i]*self.thisWeight1 + inputY[i]*self.thisWeight2 + bias;
            replace = self.sumWeighted;
            yin = self.sigmoid(replace);
            if((output[i]-yin)!=0):
                self.updateBias(output[i]);
                self.updateWeights(output[i],inputX[i],inputY[i]);
        
        epoch = epoch + 1;    
        
        if(isDelW1Zero == True and isDelW2Zero == True):
            return ;
        
        else:
            self.weightedSum();
        
    def updateBias(self,actual):
        global bias;
        bias = bias + theta * (actual - yin);
    
    def updateWeights(self,actual,input1,input2):
        global isDelW1Zero;
        global isDelW2Zero;
        
        self.delWeight1 = theta * (actual - yin) * input1 * (yin*(1-yin));
        if(self.delWeight1 == 0):
            isDelW1Zero = True;
        self.delWeight2 = theta * (actual - yin) * input2 * (yin*(1-yin));
        if(self.delWeight2 == 0):
            isDelW2Zero = True;
        self.thisWeight1 = self.thisWeight1 + self.delWeight1;
        self.thisWeight2 = self.thisWeight2 + self.delWeight2;
        
        
    def predict(self,inputx,inputy):
        global replace;
        print(type(self.thisWeight1));
        print(type(self.thisWeight2));
        replace = self.thisWeight1*float(inputx) + self.thisWeight2*float(inputY) +bias;
        self.result = sigmoid(replace);
        return self.result;
        

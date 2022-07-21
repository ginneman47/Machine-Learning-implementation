#basic perceptron training module (no widrow hoff learning is implemented)

import math as meth

#intializing variables and intial values
inputX = [1,1,-1,-1];
inputY = [1,-1,1,-1];
target = [1,-1,-1,-1];
bias =1;
weights = [0,0];
delW1=0;
delw2=0;
delbias=0;
alpha =1;
counter=0;
updatedSum = 0;
class Perceptron:
    def marginalize(self,value):
        if(value>0):
            return 1;
        elif(value==0):
            return 0;
        else:
            return -1;
            
    def weightedSum(self):
        global bias;
        global updatedSum;
        global counter;
        for i in range(0, len(inputX)):
            delW1 = alpha * inputX[i] * target[i];
            delW2 = alpha * inputY[i] * target[i];
            delbias = alpha * target[i];
            bias = bias + delbias;
            weights[0] = weights[0] +delW1;
            weights[1] = weights[1] +delW2;
            self.totalSum = inputX[i]*weights[0] + inputY[i]*weights[1] +bias;
            updatedSum  = self.totalSum;
            self.totalSum = self.marginalize(self.totalSum);
            if(self.totalSum == target[i]):
                counter=counter + 1;
        
        if(counter!=len(inputX)):
            counter=0;
            self.weightedSum();
        elif(counter==len(inputX)):
            return;
            
        
p1 = Perceptron();
p1.weightedSum();
print(weights);
print(bias);

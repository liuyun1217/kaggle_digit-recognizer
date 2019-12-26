import csv
import numpy as np
import pandas as pd
import random
from keras.utils.np_utils import to_categorical
import matplotlib.pyplot as plt

def output_res(resList,file):
    with open(file,'w') as myfile:
        mywriter = csv.writer(myfile)
        mywriter.writerows(resList)

def gen_res():
    resList = [['ImageId','Label'],]
    for i in range(1,28001):
        resLabel = str(random.randint(0,9))
        resCol = [i,resLabel]
        resList.append(resCol)
    return resList




if __name__ == '__main__':
    #x = gen_res()
    #output_res(x,'res.csv')
    trainTest = pd.read_csv('trainTest.csv')
    trainTest_Y = trainTest['label']
    trainTest_X = trainTest.drop(labels = ['label'],axis = 1)
    trainTest_X = trainTest_X/255.0
    picVec2 = trainTest_X.values.reshape(-1,28,28,1)
    print(picVec2[0][:,:,0])
    #trainTest_Y = to_categorical(trainTest_Y,num_classes=10)
    p2 = plt.imshow(picVec2[0][:,:,0])
    plt.show()

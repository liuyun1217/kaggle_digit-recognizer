import csv
import random
import matplotlib.pyplot as plt

def input_data(file):
    with open(file,'r') as myfile:
        fileCsv = csv.reader(myfile)
        fileVec = []
        for i in fileCsv:
            fileVec.append(i[1:])
    return fileVec
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

def picList2Vec(picList):
    picVec = []
    for i in range(0,784,28):
        picVec.append(picList[i:i+28])
    return picVec
def plt_pic(picVec):
    plt.imshow(picVec, interpolation="none", cmap="afmhot")
    plt.show()



if __name__ == '__main__':
    #x = gen_res()
    #output_res(x,'res.csv')
    fileVec = input_data('trainTest.csv')
    picList1 = fileVec[1]
    picVec1 = picList2Vec(picList1)
    plt_pic(picVec1)

import os
import csv
import pickle

import numpy
import pandas as pd
import numpy as np
import binascii
import collections
import tensorflow as tf



def eachFile(filepath,typefile):
    pathDir = os.listdir(filepath)
    allDirs=[]
    for allDir in pathDir:
        child = filepath+'\\'+allDir
        allDirs.append(child)



    allfiles=[]

    for j in allDirs:


        for file in os.listdir(j):

            child=j+'\\'+file

            allfiles.append(child)
    # print(allfiles)
    labels=[]

    list=[]
    for i in allfiles:

        list.append(i)
        # print(i)
        list.append(i.split('\\')[-2])
        # print(list)
    final_data=np.array(list)
    final_data=np.reshape(final_data,(-1,2))



    pd.DataFrame(final_data).to_csv(typefile,header=['数据路径','标签'],index=False)

def getMatrixfrom_pcap(filename):
    with open(filename, 'rb') as f:
        content = f.read()

    hexst = binascii.hexlify(content)

    fh = numpy.array([int(hexst[i:i+2],16) for i in range(0, len(hexst), 2)])
    # rn = len(fh)/width
    fh = numpy.reshape(fh,(28,28))

    fh = numpy.uint8(fh)


    return fh

def data(csvpath):
    train_path = csvpath
    train_df = pd.read_csv(train_path)
    a = train_df['数据路径']

    datas=numpy.zeros((len(a),28,28))
    for j,i in enumerate(a):
        temp=getMatrixfrom_pcap(i)

        datas[j]=temp

    return datas

def labels(csvpath,biaoqian=5):
    if biaoqian==5:
        train_path = csvpath
        train_df = pd.read_csv(train_path)
        train_df.head()

        a = train_df['标签']
        keydict = {}

        for i, key in enumerate(collections.Counter(a)):
            keydict[key] = i

        labels = []
        for i in a:
            labels.append(keydict[i])
        print(labels)

        classes = len(set(a))
        labels = tf.constant(labels)
        output = tf.one_hot(labels, classes)
        sess = tf.Session()
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            output = sess.run(output)
            print("output of one-hot is : \n",output)
            # print(output.shape)
        return output
    else :
        train_path = csvpath
        train_df = pd.read_csv(train_path)
        train_df.head()

        a = train_df['标签']
        labels = []
        for i in range(len(a)):
            labels.append(biaoqian)
        classes = 2
        labels = tf.constant(labels)
        output = tf.one_hot(labels, classes)
        sess = tf.Session()
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            output = sess.run(output)
            print("output of one-hot is : \n", output)
            # print(output.shape)
        return output
        # for filename in a:
if __name__ == '__main__':
    try:
        print('删除test.csv-------------')
        os.remove('test.csv')
        print('删除train.csv-------------')
        os.remove('train.csv')
        print('删除train.pkl-------------')
        os.remove('train.pkl')
        print('删除test.pkl-------------')
        os.remove('test.pkl')
        print('删除train_labels.pkl-------------')
        os.remove('train_labels.pkl')
        print('删除test_labels.pkl-------------')
        os.remove('test_labels.pkl')
    except Exception as e:
        # print(e)
        pass

    #输入train或者test文件夹名称，可以生成路径和标签的CSV文件
    eachFile(r'testdata','test.csv')
    datas = data(r'test.csv')
    f = open(r'test.pkl', 'wb')
    pickle.dump(datas, f)
    label = labels(r'test.csv')#0,1,   0是良性，1是恶性，默认不填写两种分类文件夹自己定义标签
    # print(label)
    f = open(r'test_labels.pkl', 'wb')
    pickle.dump(label, f)



    eachFile(r'traindata','train.csv')
    datas = data(r'train.csv')
    f = open(r'train.pkl', 'wb')
    pickle.dump(datas, f)
    #label
    label = labels(r'train.csv')
    # print(label)
    f = open(r'train_labels.pkl', 'wb')
    pickle.dump(label, f)



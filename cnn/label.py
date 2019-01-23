
# coding: utf-8

# In[50]:
import pickle

import pandas as pd
import collections
import tensorflow as tf
import numpy


# In[12]:

def labels(csvpath):
    train_path=csvpath
    train_df = pd.read_csv(train_path)
    train_df.head()


    a=train_df['标签']
    keydict={}

    for i,key in enumerate(collections.Counter(a)):

            keydict[key]=i

    labels=[]
    for i in a:
        labels.append(keydict[i])


    classes=len(set(a))
    labels = tf.constant(labels)
    output = tf.one_hot(labels,classes)
    sess = tf.Session()
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        output = sess.run(output)
        # print("output of one-hot is : \n",output)
        # print(output.shape)
    return output

if __name__ == '__main__':
    label=labels(r'F:\fast\cnn\train.csv')
    print(label)
    f=open(r'train_labels.pkl','wb')
    pickle.dump(label,f)
    # label=pickle.load(f)
    # print(label)


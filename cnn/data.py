import numpy
from PIL import Image
import binascii
import errno
import os
import pandas as pd
import pickle




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
    # for filename in a:

if __name__ == '__main__':
  datas=data(r'F:\fast\cnn\train.csv')
  f=open(r'train.pkl','wb')
  pickle.dump(datas,f)


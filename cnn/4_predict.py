
import numpy as np
from keras.applications.imagenet_utils import decode_predictions
from keras.preprocessing import image
from keras.applications import *
import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
import data
from keras.models import load_model

ts=data.getMatrixfrom_pcap(r'C:\Users\Administrator\Desktop\测试数据集\data3\3_ProcessedSession\TrimedSession\Train\m\Miuref-DNS.pcap.UDP_8-8-8-8_53_10-0-2-108_49530.pcap')
# print(ts)
ts=ts.reshape(1,1,28,28)

model=load_model('model2class.h5')

y=model.predict(ts)

print(y)
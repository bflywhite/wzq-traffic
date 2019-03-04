import scapy.all as scapy
import os

import os

pcaps = []


def gci(filepath):
    # 遍历filepath下所有文件，包括子目录 递归的方式
    global pcaps
    files = os.listdir(filepath)
    print(files)
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            gci(fi_d)
        else:
            pcaps.append(os.path.join(filepath, fi_d))
            # print(os.path.join(filepath, fi_d))


def changIp():

    for pcap in pcaps:
        count=0
        list_a = []
        packeges = scapy.rdpcap(pcap)
        while (count != 1):
            for p in packeges:
                try:
                    temp=p
                    if temp.haslayer("DNS"):

                        temp["IP"].src = '0.0.0.0'
                        temp["IP"].dst = '0.0.0.0'
                        list_a.append(temp)
                except Exception as e:
                    print(e)
                    pass
            count = count + 1
        scapy.wrpcap(pcap, list_a)


if __name__ == '__main__':
    # 输入脚本处理后的文件夹路径 eg：C:\Users\Administrator\Desktop\测试数据集\12-21\2_Session\AllLayers
    # 把所有数据包的源和目的IP都写为0.0.0.0

    gci(r'C:\Users\Administrator\Desktop\12-21\2_Session\AllLayers\asd')

    changIp()


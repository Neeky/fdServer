#!/usr/local/python/bin/python3
import argparse
import requests
import os

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--serverUrl',default='http://www.workstudio.com/shibor/init/upload',
                        help='服务器接收shiborInit操作的地址')
    parser.add_argument('--file-dir',default='/tmp/shibor/',help='shibor历史数据所在的文件路径')
    args=parser.parse_args()
    #从文件中读出shibor的历史数据
    shiborHistoryFiles=['{0}{1}'.format(args.file_dir,vf) for vf in os.listdir(args.file_dir)]
    #shiborHistoryFiles=['/tmp/shibor/2016shibor.txt',/tmp/shibor/2017/shibor.txt']
    for vf in shiborHistoryFiles:
        #循环目录下的每一个文件
        #前两行不是数据这里要去掉
        print("----------------{0}".format(vf))
        lines=[line for line in open(vf,encoding='gbk')][2:]
        for line in lines:
            #把行处理成列表
            tmp=line.replace('     ',',')
            tmp=tmp.replace(' ','')
            data=tmp.split(',')[:9]
            #处理后的样子 ['2016-01-04', '1.9950', '2.3350', '2.9040', '3.0010', '3.0860', '3.2000', '3.2500']
            print(data)
            data[0]=data[0]+' 11:00'
            datas={}
            datas['pushDate']=data[0]
            datas['oneNight']=data[1]
            datas['oneWeek']=data[2]
            datas['twoWeek']=data[3]
            datas['oneMonth']=data[4]
            datas['threeMonth']=data[5]
            datas['sixMonth']=data[6]
            datas['nineMonth']=data[7]
            datas['oneYear']=data[8]
            requests.post('http://www.workstudio.com/shibor/init/upload/',data=datas)




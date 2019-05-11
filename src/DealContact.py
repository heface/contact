# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 15:41:31 2019

@author: hca3085
"""

import base64
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import CHAR,INT

class Contact:
    def __init__(self,id=0,name='',telHome='',telWork='',telWork1='',\
            telCell='',telCell1='',telCell2='',\
            email='',group='',qq='',department='',team='',\
            address='',birthday='',mem='',flag=''):           
        self._id = id                 #自增主键
        self._name = name             #姓名
        self._telHome = telHome       #home tel
        self._telWork = telWork       #工作电话
        self._telWork1 = telWork1     #工作电话
        self._telCell = telCell       #移动电话
        self._telCell1 = telCell1     #移动电话
        self._telCell2 = telCell2     #移动电话
        self._email = email           #电子邮件地址
        self._group = group           #分组
        self._qq = qq                 #QQ号码
        self._department = department #公司/部门
        self._team = team             #团队
        self._address = address       #地址
        self._birthday = birthday     #生日
        self._mem = mem               #备注
        self._flag = flag             #来源标记

    def __str__(self):
        return 'name=%s;telHome=%s;telWork=%s;telWork1=%s;\
                telCell=%s;telCell1=%s;telCell2=%s;\
                email=%s;group=%s;qq=%s;department=%s;\
                address=%s;birthday=%s;mem=%s' % \
                (self._name,self._telHome,self._telWork,self._telWork1,\
                self._telCell,self._telCell1,self._telCell2,\
                self._email,self._group,self._qq,self._department,self._team\
                self._address,self._birthday,self._mem,self._flag)
        
    def __repr__(self):
        return 'name=%s;telCell=%s;telWork=%s;email=%s;group=%s' % \
                (self._name,self._telCell,self._telWork,self._email,\
                self._group)

#读取导出通讯录中的姓名
def _getName(name):
    newName = name
    #print("name=%s" % name)
    try:
        if newName[0] == '=':
            newName = newName[1:]
        byteName = [int(i,16) for i in newName.split('=')]
        return bytes(byteName).decode(encoding='utf-8')
    except:
        print("error name=%s" % name)
        return name

def _getGroup(group):
    if group.find(':::') > 0:
        gn = ''
        for item in group.split(' ::: '):
            gn = gn+'||'+_getName(item)
        return gn
    else:
        return _getName(group)

#写入导出通讯录中的姓名
def _setName(name):
    newName = str(name.encode(encoding='utf-8'))
    return newName[2:-1].replace('\\x','=').upper()

def processContact(contact):
    contactInstance = Contact()
    name = 'FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:'
    telCell = 'TEL;CELL:'
    telWork = 'TEL;WORK:'
    email = 'EMAIL;HOME:'
    group = 'X-GROUP-MEMBERSHIP;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:'

    for item in contact:
        #print("item=%s" % item)
        if item.find(name) == 0:
            contactInstance._name = _getName(item[43:-1])
        if item.find(telCell) == 0:
            contactInstance._telCell = item[9:-1]
        if item.find(telWork) == 0:
            contactInstance._telWork = item[9:-1]
        if item.find(email) == 0:
            contactInstance._email = item[11:-1]
        if item.find(group) == 0:
            contactInstance._group = _getGroup(item[59:-1])
    return contactInstance

def processContactToDict(contact,conDict):
    name = 'FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:'
    telCell = 'TEL;CELL:'
    telWork = 'TEL;WORK:'
    email = 'EMAIL;HOME:'
    group = 'X-GROUP-MEMBERSHIP;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:'

    for item in contact:
        #print("item=%s" % item)
        if item.find(name) == 0:
            conDict['name'].append(_getName(item[43:-1]))
        if item.find(telCell) == 0:
            conDict['telCell'].append(item[9:-1])
        if item.find(telWork) == 0:
            conDict['telWork'].append(item[9:-1])
        if item.find(email) == 0:
            conDict['email'].append(item[11:-1])
        if item.find(group) == 0:
            conDict['group'].append(_getGroup(item[59:-1]))


def parseContact(filename):
    contactList = []
    '''测试华为手机导出的通讯录格式，以便将csv格式的通讯录,
    整理成符合华为的存储格式导入'''   
    f = open(filename,"r")
    strBuf = []
    flag = False
    for line in f.readlines():
        if line.find('END:VCARD')>=0:
            flag = False
            contactList.append(processContact(strBuf))
            strBuf = []
            continue
        if flag:
            strBuf.append(line)
            continue
        if line.find('BEGIN:VCARD')>=0:
            flag = True
            continue        

    f.close()
    print('--------------contact list--------------')
    for item in contactList:
        print(item)

def parseContactToDict(filename):
    contactDict = {'name':[],'telHome':[],'telWork':[],'telCell':[],
        'email':[],'c_group':[],'qq':[],'department':[],'team':[],
        'address':[],'birthday':[],'mem':[],'flag':[]}
    '''测试华为手机导出的通讯录格式，以便将csv格式的通讯录,
    整理成符合华为的存储格式导入'''   
    f = open(filename,"r")
    strBuf = []
    flag = False
    for line in f.readlines():
        if line.find('END:VCARD')>=0:
            flag = False
            contactList.append(processContact(strBuf))
            strBuf = []
            continue
        if flag:
            strBuf.append(line)
            continue
        if line.find('BEGIN:VCARD')>=0:
            flag = True
            continue
    f.close()
    print('--------------contact list--------------')
    for item in contactDict:
        print(item)    
    return contactDict
        
def _format(arrayItem):
    '''针对读入的通讯录数据，去掉双引号和空格'''
    if len(arrayItem) >= 2:
        return arrayItem[1:-1].strip()
    else:
        return arrayItem
    

def parseCSVContact(filename):
    '''解析csv格式的通讯录备份文件，生成华为导出格式的通讯录文件'''
    contactList = []
    f = open(filename,"r",encoding='gbk')
    for line in f.readlines():
        a = line.split(",")
        contactInstance = Contact(name=_format(a[0])+_format(a[1]),\
                telHome=_format(a[6]),telWork=_format(a[13]),\
                telWork1=_format(a[14]),telCell=_format(a[18]),\
                telCell1=_format(a[19]),telCell2=_format(a[20]),\
                email=_format(a[16]),group=_format(a[23]),qq=_format(a[5]),\
                department=_format(a[21]),birthday=_format(a[22]),\
                mem=_format(a[15]),\
                address=_format(a[8])+_format(a[9])+_format(a[10])+\
                _format(a[11])+_format(a[12]))
        contactList.append(contactInstance)        
    f.close()
    
    print('--------------contact list--------------')
    #for item in contactList:
    #    print(item)    
    return contactList

def parseCSVToDict(filename):
    '''解析csv格式的通讯录备份文件，生成字典类型'''
    contactDict = {'name':[],'telHome':[],'telWork':[],'telCell':[],
        'email':[],'c_group':[],'qq':[],'department':[],'team':[],
        'address':[],'birthday':[],'mem':[],'flag':[]}
    f = open(filename,"r",encoding='gbk')
    for line in f.readlines():
        a = line.split(",")        
        contactDict['name'].append(_format(a[0])+_format(a[1]))
        contactDict['telHome'].append(_format(a[6]),telWork=_format(a[13]))
        contactDict['telWork'].append(_format(a[14]),telCell=_format(a[18]))
        contactDict['telCell'].append(_format(a[19]),telCell2=_format(a[20]))
        contactDict['email'].append(_format(a[16]))
        contactDict['c_group'].append(_format(a[23]))
        contactDict['qq'].append(_format(a[5]))
        contactDict['department'].append(_format(a[21]))
        contactDict['birthday'].append(_format(a[22]))
        contactDict['mem'].append(_format(a[15]))
        contactDict['address'].append(_format(a[8])+_format(a[9])+_format(a[10])+_format(a[11])+_format(a[12])))
        contactDict['team'].append('')
        contactDict['flag'].append('android')
    f.close()

    print('--------------contact list--------------')
    #for item in contactDict:
    #    print(item)    
    return contactDict
    
    
def _writeContact(f,contact):
    f.write("BEGIN:VCARD\n")
    #姓名
    name = _setName(contact._name)
    f.write("N;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:;{};;;\n".format(name))
    f.write("FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:{}\n".format(name))
    #电子邮件地址
    f.write("EMAIL;HOME:{}\n".format(contact._email))
    #电话
    f.write("TEL;CELL:{}\n".format(contact._telCell))
    f.write("TEL;WORK:{}\n".format(contact._telWork))
    #分组
    f.write("X-GROUP-MEMBERSHIP;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:{}\n"\
            .format(_setName(contact._group)))
    f.write("END:VCARD\n")

def generateContactVCF(contactList):
    '''根据联系人列表，生成可导入的VCF格式文件'''
    f = open("D:/tmp/contact/CONTACT.vcf","w")
    for item in contactList:
        _writeContact(f,item)    
    f.close()

def getPosition():
    line = '''"姓","名","前缀","后缀","昵称","QQ","家庭电话","单位",
            "商务地址 国家/地区","商务地址 市/县","商务地址 省/市/自治区",
            "商务地址 街道","商务地址 邮政编码","工作电话","工作电话 2",
            "备注","电子邮件","家庭邮箱","其他手机","其他手机 2","其他手机 3",
            "公司/部门","生日","qq同步助手 分组",'''
    a = line.split(',')
    for i in range(len(a)):
        print("%d,%s" % (i,a[i].strip()))

def writeSql():
    print('connect db...')
    db=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='123456',\
            db='heLocalDB',charset='utf8')
    cursor=db.cursor()#使用cursor()方法获取操作游标

    sql = "select * from Contact"
    cursor.execute(sql)
    info = cursor.fetchall()
    print(info)

    db.commit()
    cursor.close() #关闭游标  
    db.close()#关闭数据库连接
    print('close db')

def writeByDF(contactDict):
    connect_info = 'mysql+pymysql://username:passwd@host:3306/dbname?charset=utf8'
    engine = create_engine(connect_info) #use sqlalchemy to build link-engine

    contactDict = parseCSVToDict("../data/2018-10-04-20-55-20-contact-14.csv")
    
    df = pd.DataFrame(contactDict)
    #DataFrame.to_sql(name, con, schema=None, if_exists='fail', index=True, index_label=None, chunksize=None, dtype=None)
    #dtype = {'id': INT(), 'name': CHAR(length=2), 'score': CHAR(length=2)
    df.to_sql('Contact', engine, schema=None, if_exists='fail', index=True, index_label=None, chunksize=None)

    contactDict = parseContactToDict("../data/00001.vcf")
    df = pd.DataFrame(contactDict)
    df.to_sql('Contact', engine, schema=None, if_exists='fail', index=True, index_label=None, chunksize=None)

    contactDict = parseContactToDict("../data/00002.vcf")
    df = pd.DataFrame(contactDict)
    df.to_sql('Contact', engine, schema=None, if_exists='fail', index=True, index_label=None, chunksize=None)

    contactDict = parseContactToDict("../data/PHONE00001.vcf")
    df = pd.DataFrame(contactDict)
    df.to_sql('Contact', engine, schema=None, if_exists='fail', index=True, index_label=None, chunksize=None)
    
if __name__ == "__main__":
    contactList = parseCSVContact(\
            "../data/2018-10-04-20-55-20-contact-14.csv")
    for item in contactList[1:3]:
        print(item)
    #generateContactVCF(contactList)
    
    #parseCSVContact("D:/tmp/contact/testContact.csv")
    
    #parseContact("../data/00001.vcf")
    
    #parseContact("../data/00002.vcf")
   
    #parseContact("../data/PHONE00001.vcf")

    #parseContact("../tel/00002.vcf")
    
    #parseContact("../data/CONTACT.vcf")

    #parseContact("../tel/00001.vcf")

    #_getName("E4=BA=8C=E6=A2=85")
    #print(_getName("=E9=83=91=E7=90=B3=E8=BD=AF=E9=80=9A"))
   
    #print(_getName("=E6=9D=8E=E9=A2=96=E5=AE=A2=E6=9C=8D"))
   
    #print(_getName("=E5=88=98=E8=B6=85"))
    #print(_setName('二梅'))
    #testBase64()
    
    #getPosition()
    

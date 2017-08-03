from django.db import models
from datetime import datetime
from fdServer.exceptions import ShortInput
# Create your models here.

class Company(models.Model):
    """
    用于保存公司的基本信息,数据长度最小定义到32
    """
    name=models.CharField(help_text='公司名',max_length=32)
    stockCode=models.CharField(help_text='证券代码',max_length=32,primary_key=True)
    section=models.CharField(help_text='版块 中小企业板|创业板 ...',max_length=32)
    mainPage=models.CharField(help_text='公司在cninfo中的主页地址',max_length=128)

    #以下是公司简介中的内容
    fullName=models.CharField(max_length=64,default='',help_text='公司全称')
    briefName=models.CharField(max_length=64,default='',help_text='公司简称')
    enlishName=models.CharField(max_length=128,default='',help_text='英文名称')
    registeredAddress=models.CharField(max_length=64,default='',help_text='注册地址')
    legalPerson=models.CharField(max_length=64,default='',help_text='法定代表人')
    secretaries=models.CharField(max_length=64,default='',help_text='董秘')
    registeredCapital=models.DecimalField(max_digits=32,decimal_places=4,default=0,help_text='注册资本')
    industry=models.CharField(max_length=32,default='',help_text='行业种类')
    postalCode=models.CharField(max_length=32,default='',help_text='邮政编码')
    companyPhone=models.CharField(max_length=64,default='',help_text='公司电话')
    companyFax=models.CharField(max_length=64,default='',help_text='公司传真')
    companyWebsite=models.CharField(max_length=128,default='',help_text='公司网址')
    listingTime=models.DateTimeField(default='1000-01-01 01:01:01',help_text='上市时间')
    prospectusTime=models.DateTimeField(default='1000-01-01 01:01:01',help_text='招股时间')
    issuedQuantity=models.DecimalField(max_digits=16,decimal_places=0,default=0,help_text='发行数量')
    issuePrice=models.DecimalField(max_digits=16,decimal_places=4,default=0,help_text='发行价格')
    ipoPERate=models.DecimalField(max_digits=16,decimal_places=2,default=0,help_text='发行市盈率')
    issueMode=models.CharField(max_length=64,default='',help_text='发行方式')
    leadUnderwrite=models.CharField(max_length=64,default='',help_text='主承销商')
    issueRecommender=models.CharField(max_length=64,default='',help_text='上市推荐人')
    sponsor=models.CharField(max_length=64,default='',help_text='保荐机构')    
    #lastupdated 用于表示最近一次更新的时间
    lastUpdate=models.DateTimeField(default=datetime.now(),help_text='招股时间')

    def fromJson(self,jdt):
        try:
            self.name=jdt['companyName'].strip()
            self.stockCode=jdt['stockCode'].strip()
            self.section=jdt['section'].strip()
            self.mainPage=jdt['mainPage'].strip()
        except Exception as e:
            em="exception occur in cninfo.models.Company.fromJson :{0}".format(e)
            print(em)
            print('print input data jdt : {0}'.format(jdt))
            raise e
    
    def fromJsonAddBrief(self,jdt):
        print(jdt)
        try:
            if jdt['status'] == 'shortinput':
                raise ShortInput('exception fdServer.exceptions.ShortInput in cninfo.models.fromJsonAddBrief')
            self.fullName=jdt['fullName']
            self.briefName=jdt['briefName']
            self.enlishName=jdt['enlishName']
            self.registeredAddress=jdt['registeredAddress']
            self.legalPerson=jdt['legalPerson']
            self.secretaries=jdt['secretaries']
            self.registeredCapital=jdt['registeredCapital']
            self.industry=jdt['industry']
            self.postalCode=jdt['postalCode']
            self.companyPhone=jdt['companyPhone']
            self.companyFax=jdt['companyFax']
            self.companyWebsite=jdt['companyWebsite']
            self.listingTime=jdt['listingTime'] if jdt['listingTime'] != '' else '4096-01-01'
            self.prospectusTime=jdt['prospectusTime'] if jdt['prospectusTime'] !='' else '4096-01-01' 
            self.issuedQuantity=jdt['issuedQuantity']
            self.issuePrice=jdt['issuePrice']
            self.ipoPERate=jdt.setdefault('ipoPERate',0)
            self.issueMode=jdt['issueMode']
            self.issueMode=jdt['issueMode']
            self.leadUnderwrite=jdt['leadUnderwrite']
            self.issueRecommender=jdt['issueRecommender']
            self.sponsor=jdt['sponsor']
        except ShortInput as e:
            print("warning accur in cninfo.models.fromJsonAddBrief :{0}".format(e))
        except Exception as e:
            em="exception accur in cninfo.models.fromJsonAddBrief :{0}".format(e)
            print(em)
            raise e


 

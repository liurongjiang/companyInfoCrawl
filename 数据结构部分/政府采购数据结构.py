# -*- coding:utf-8 -*-
'''
    @author: liurj
    @createDate: 2018/3/7
    '''

#招标、采购类公告
zbgg = {
    "siteName": "",         #网站名称
    "channelName": "",      #频道名称
    "snapshotUrl": "",      #快照链接
    "bulletinType": "",     #公告类型

    "title": "",            #标题
    "pubdate": "",          #发布日期
    "content": "",          #正文
    "sourceUrl": "",        #原文链接
    "dataSource": "",       #信息来源
    "crawlDate": "",        #抓取日期

    "budget": "",           #预算金额
    "region": "",           #行政区域
    "otherInfo": "",        #其他信息
    "bidderQuali": "",      #投标人资格要求
    "projectName": "",      #项目名称
    "projectNumber": "",    #项目编号、采购编号
    "packageNumber": "",    #分包个数
    "purchaseContent": "",  #采购内容、品目
    "bidInfo": {        #投标信息
        "startDate": "",    #投标开始时间
        "endTDate": "",     #投标截止日期
        "address": "",      #投标地址
    }, 

    "bidOpenInfo": {    #开标信息
        "startDate": "",    #开标时间
        "address": "",      #开标地点
    }, 
    "bidFileInfo": {    #招标文件信息
        "startDate": "",    #开始时间
        "endTDate": "",     #结束时间
        "address": "",      #地址
        "price": "",        #售价
        "getMethod": ""     #获取方式
    }, 
    "purchaserInfo": {  #采购人、采购单位信息
        "name": "",         #名称
        "address": "",      #地址
        "contacts": "",     #联系人
        "contactNumber": "" #联系电话
    },
    "agencyInfo": {     #代理机构
        "name": "",         #名称
        "address": "",      #地址
        "contacts": "",     #联系人
        "contactNumber": "",#联系电话
    }, 
    "attachFileInfo": { #附件
        "name": "",         #名称
        "sourceUrl": "",    #链接
        "type": ""          #类型
    }
}
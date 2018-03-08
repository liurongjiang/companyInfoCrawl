#coding=utf-8

#招标、采购公告
zbcg_gg = {
    "siteId": "",           #站点id
    "beTest": "",           #数据分类（测试、正式）
    "contentId": "",        #正文id
    "channelId": "",        #频道id
    "themeClsfy": "",       #主题编号
    "noticeId": "",         #关联编号

    "projectType": "",      #项目行业分类   
    "siteName": "",         #网站名称
    "channelName": "",      #频道名称
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
    
    "bidInfo": {            #投标信息
        "startDate": "",    #投标开始时间
        "endTDate": "",     #投标截止日期
        "address": "",      #投标地址
    }, 

    "bidOpenInfo": {        #开标信息
        "startDate": "",    #开标时间
        "address": "",      #开标地点
    }, 
    "bidFileInfo": {        #招标文件信息
        "startDate": "",    #开始时间
        "endTDate": "",     #结束时间
        "address": "",      #地址
        "price": "",        #售价
        "getMethod": ""     #获取方式
    }, 
    "purchaserInfo": {      #采购人、采购单位信息
        "name": "",         #名称
        "address": "",      #地址
        "contacts": "",     #联系人
        "contactNumber": "" #联系电话
    },
    "agencyInfo": {         #代理机构
        "name": "",         #名称
        "address": "",      #地址
        "contacts": "",     #联系人
        "contactNumber": "",#联系电话
    }, 
    "attachFileInfo": []
}

#中标、成交公告
zbcj_gg = {
    "siteId": "",           #站点id
    "beTest": "",           #数据分类（测试、正式）
    "contentId": "",        #正文id
    "channelId": "",        #频道id
    "themeClsfy": "",       #主题编号
    "noticeId": "",         #关联编号

    "siteName": "",         #网站名称
    "channelName": "",      #频道名称
    "bulletinType": "",     #公告类型
    "projectType": "",      #项目行业分类   

    "title": "",            #标题
    "pubdate": "",          #发布日期
    "content": "",          #正文
    "sourceUrl": "",        #原文链接
    "dataSource": "",       #信息来源
    "crawlDate": "",        #抓取日期

    "region": "",           #行政区域
    "projectName": "",      #项目名称
    "projectNumber": "",    #项目编号、采购编号
    "purchaseContent": "",  #采购内容、品目
    "bidDate": "",          #中标时间
    "otherInfo": "",        #其他信息
    "purchaserInfo": {      #采购人、采购单位信息
        "name": "",         #名称
        "address": "",      #地址
        "contacts": "",     #联系人
        "contactNumber": "" #联系电话
    },
    "expertReviewer": "",    #评审专家名单
    "agencyInfo": {         #代理机构
        "name": "",         #名称
        "address": "",      #地址
        "contacts": "",     #联系人
        "contactNumber": "",#联系电话
        "agencyAmount":"",  #代理金额
        "chargeStandard": ""#代理费收费标准
    }, 

    "candidates": [],       #中标候选人
    "supplierInfo": [],     #供应商信息
    "complaintInfo": [],    #质疑、投诉
    "attachFileInfo": []    #附件
}

attachFile = { 
    "name": "",         #名称
    "sourceUrl": "",    #链接
    "type": ""          #类型
}

complaintInfo = {  
    "name": "",         #单位名称
    "tel": ""           #电话
}

candidates = {
    "name":"",      #候选人名称
    "order":"",     #候选人排名
}

supplierInfo = {
    "name":"",          #名称
    "address":"",       #地址
    "bidAmount ":"",    #中标金额
    "packageNo":""      #包号
}

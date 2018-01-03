#1法院公告
fygg = {
    "rowkeySource": "发布时间+当事人+法院名称",   #rowkey来源
    "rowkey": "",               #md5
    "fyggId": "",               #法院公告ID，法院公告唯一标识
    "sortTime": "",             #发布时间
    "body": "",                 #公告内容
    "pname": "",                #当事人
    "court": "",                #法院名称
    "ggType": "",               #公告类型
    "Release unit": "",         #发布单位
    "privince": "",             #省份
}

#2开庭公告
ktgg = {
    "rowkeySource": "案号",     #rowkey来源
    "rowkey": "",               #md5
    "ktggId": "",               #开庭公告ID，开庭公告唯一的标识
    "sortTime": "",             #开庭时间
    "body": "",                 #内容
    "title": "",                #标题
    "court": "",                #法院名称
    "courtroom": "",            #开庭地点
    "caseCause": "",            #案由
    "caseNo": "",               #案号
    "plaintiff": "",            #原告
    "party": "",                #当事人
    "judge": "",                #法官
    "defendant": "",            #被告
    "Release unit": "",         #发布单位
    "privince": "",             #省份
}

#3裁判文书
cpws = {
    "rowkeySource": "案号",      #rowkey来源
    "rowkey": "",               #md5
    "body": "",                 #内容
    "partys": [
        #2诉讼当事人集合
        {
            "birthday": "",     #当事人生日
            "title": "",        #当事人称号
            "partytype": "",    #当事人类型
            "lawOffice": "",    #律师事务所
            "status": "",       #当事人立场
            "pname": "",        #当事人名称
            "idcardNo": "",     #当事人身份证号码
            "lawyer": "",       #委托辩护人
        }
    ],
    "court": "",                #法院名称
    "sortTime": "",             #审结时间
    "title": "",                #标题
    "caseCause": "",            #案由
    "judgeResult": "",          #判决结果
    "trialProcedure": "",       #审理程序
    "cpwsId": "",               #法海自定义id
    "judge": "",                #审判员
    "caseType": "",             #文书类型
    "caseNo": "",               #案号
    "yiju": "",                 #依据法律条文
    "dataType": "",             #cpws
    "courtRank": "",            #未知
    "anyou": "",                #未知
    "anyouType": ""             #未知
}

#4执行公告
zxgg = {
    "rowkeySource": "案号",      #rowkey来源
    "rowkey": "",               #md5
    "zxggId": "",               #执行公告ID，执行公告唯一的标识
    "sortTime": "",             #立案时间
    "body": "",                 #内容
    "title": "",                #标题
    "pname": "",                #被执行人姓名
    "court": "",                #执行法院名称
    "caseNo": "",               #案号
    "caseState": "",            #案件状态
    "idcardNo": "",             #身份证/组织机构代码
    "execMoney": "",            #执行标的
    "proposer": "",             #申请人
    "Release unit": "",         #发布单位
    "privince": "",             #省份
}

#5 失信公告
dishonestyNotice = {
    "rowkeySource": "案号",      #rowkey来源
    "rowkey": "",               #md5
    "frfzr": "",                #法定代表人或者负责人姓名
    "age": "",                  #年龄
    "sex": "",                  #性别
    "body": "",                 #全部内容
    "lxqk": "",                 #被执行人的履行情况
    "yiwu": "",                 #生效法律文书确定的义务
    "court": "",                #执行法院
    "yjdw": "",                 #做出执行依据单位
    "sortTime": "",             #立案时间时间戳
    "province": "",             #省份
    "sortTimeString": "",       #立案时间
    "jtqx": "",                 #失信被执行人行为具体情形
    "pname": "",                #被执行人姓名/名称
    "postTime": "",             #发布时间
    "yjCode": "",               #执行依据文号
    "sxggId": "",               #法海自定义id
    "caseNo": "",               #案号
    "idcardNo": "",             #身份证号码/组织机构代码
    "ylx": "",                  #已履行部分
    "wlx": "",                  #未履行部分
    "datafrom": "",             #数据来源
    "dataType": ""              #sxgg
}
#6 案件流程
ajlc = {
    "rowkeySource": "案号",      #rowkey来源
    "rowkey": "",               #md5
    "ajlcId": "",               #案件流程ID，案件流程唯一标识
    "sortTime": "",             #立案时间
    "body": "",                 #内容
    "court": "",                #法院名称
    "pname": "",                #当事人
    "caseType": "",             #案件类别
    "caseCause": "",            #案由
    "ajlcStatus": "",           #案件流程状态
    "caseNo": "",               #案号
    "organizer": "",            #组织单位
    "filingDate": "",           #归档日期
    "chiefJudge": "",           #主审法官
    "clerk": "",                #书记员
    "clerkPhone": "",           #书记员电话
    "actionObject": "",         #诉讼标的
    "member": "",               #法庭成员    
    "sentencingDate": "",       #判决日期
    "trialLimitDate": "",       #审判期限
    "effectiveDate": "",        #有效日期
     "Release unit": "",        #发布单位
     "privince": "",            #省份 
}

#7网贷黑名单
wdhmd = {
    "rowkeySource": "案号",      #rowkey来源
    "rowkey": "",               #md5
    "wdhmdId": "",              #网贷黑名单ID，网贷黑名单唯一标识
    "sortTime": "",             #贷款时间
    "pname": "",                #姓名
    "body": "",                 #内容
    "sex": "",                  #性别
    "phone": "",                #电话
    "updateTime": "",           #信息更新时间
    "execCourt": "",            #执行法院
    "whfx": "",                 #未还/罚息
    "idcardNo": "",             #身份证号
    "birthPlace": "",           #籍贯地址
    "bjbx": "",                 #本金/本息
    "caseNo": "",               #案号
    "address": "",              #居住地址
    "email": "",                #邮箱地址
    "age": "",                  #年龄
    "datasource": "",           #数据来源单位名称
    "yhje": "",                 #已还金额
    "mobile": "",               #手机号
    "Release unit": "",         #发布单位
    "privince": ""              #省份
}










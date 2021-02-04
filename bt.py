"""

           _               _       
     /\   | |             | |      
    /  \  | |__  _   _  __| |_   _ 
   / /\ \ | '_ \| | | |/ _` | | | |
  / ____ \| |_) | |_| | (_| | |_| |
 /_/    \_\_.__/ \__,_|\__,_|\__,_|
                                   
                                   
 * 宝塔面板站点操作Python库
 * @ 作者 Abudu
 * @ 参考 阿良 or Youngxj(二次开发)
 * @ 官方API文档 https://www.bt.cn/api-doc.pdf
 * @ 博客 https://www.abudu.top
 * @ 版本 0.1
"""

"""    完成情况
   
      系统状态相关接口   ---163
    GetSystemTotal  获取系统基础统计 √
    GetDiskInfo  获取磁盘分区信息 √
    GetNetWork  获取实时状态信息(CPU、内存、网络、负载) √
    GetTaskCount 检查是否有安装任务 √
    UpdatePanel 检查面板更新 √
   	  网站管理相关接口  ---184
   	Websites  获取网站列表 √
   	Webtypes  获取网站分类 √
   	GetSiteID  获取指定站点ID若站点不存在则返回-1 √
   	GetPHPVersion  获取已安装的 PHP 版本列表 √
    GetSitePHPVersion  获取指定网站运行的PHP版本 √
    SetPHPVersion  修改指定网站的PHP版本 √
    GetTypeID     获取分类ID若分类不存在则返回0 √
    SetHasPwd  开启并设置网站密码访问 √
    CloseHasPwd  关闭网站密码访问 √
    GetDirUserINI  获取网站几项开关（防跨站、日志、密码访问） √
   	WebAddSite   创建网站 √
   	WebDeleteSite  删除网站 √
   	WebSiteStop  停用网站 √
   	WebSiteStart  启用网站 √
   	WebSetEdate  设置网站有效期 √
   	WebSetPs  修改网站备注 √
   	WebBackupList  获取网站备份列表 √
   	WebToBackup  创建网站备份 √
   	WebDelBackup  删除网站备份 √
   	WebDoaminList  获取网站域名列表 √
    GetDirBinding  获取网站域名绑定二级目录信息 √
    AddDirBinding  添加网站子目录域名 √
    DelDirBinding  删除网站绑定子目录 √
    GetDirRewrite  获取网站子目录伪静态规则 √
   	WebAddDomain  添加网站域名 √
   	WebDelDomain  删除网站域名  √
    GetSiteLogs  获取网站日志 √
    GetSecurity  获取网站盗链状态及规则信息 √
    SetSecurity  设置网站盗链状态及规则信息 √
    GetSSL  获取SSL状态及证书详情 √
    HttpToHttps  强制HTTPS √
    CloseToHttps 关闭强制HTTPS √
    SetSSL  设置SSL证书 √
    CloseSSLConf  关闭SSL √
    WebGetIndex  获取网站默认文件 √
    WebSetIndex  设置网站默认文件 √
    GetLimitNet  获取网站流量限制信息 √
    SetLimitNet  设置网站流量限制信息 √
    CloseLimitNet  关闭网站流量限制 √
    Get301Status  获取网站301重定向信息 √
    Set301Status  设置网站301重定向信息 √
   	GetRewriteList 获取可选的预定义伪静态列表 √
   	GetFileBody  获取指定预定义伪静态规则内容(获取文件内容) √
   	SaveFileBody  保存伪静态规则内容(保存文件内容) √
    GetProxyList  获取网站反代信息及状态 √
    CreateProxy  添加网站反代信息 √
    ModifyProxy  修改网站反代信息 √

      Ftp管理  ---803
    WebFtpList 获取FTP信息列表 √
    SetUserPassword  修改FTP账号密码 √
    GetFTPID  根据Ftp_Username获取FTPID √
    SetStatus  启用/禁用FTP √

      Sql管理  ---855
    WebSqlList 获取SQL信息列表 √
    ResDatabasePass 修改SQL账号密码 √
    GetSQLID 根据数据库名获取SQLID √
    SQLToBackup  创建sql备份 √
    SQLDelBackup  删除sql备份 √

    download  下载备份文件 ×

      插件管理  ---913
    deployment  宝塔一键部署列表 √
    SetupPackage 部署任务
"""
config = {
    "AddDirBinding": "/site?action=AddDirBinding",
    "CloseHasPwd": "/site?action=CloseHasPwd",
    "CloseLimitNet": "/site?action=CloseLimitNet",
    "CloseSSLConf": "/site?action=CloseSSLConf",
    "CloseToHttps": "/site?action=CloseToHttps",
    "CreateProxy": "/site?action=CreateProxy",
    "DelDirBinding": "/site?action=DelDirBinding",
    "Get301Status": "/site?action=Get301Status",
    "GetDirBinding": "/site?action=GetDirBinding",
    "GetDirRewrite": "/site?action=GetDirRewrite",
    "GetDirUserINI": "/site?action=GetDirUserINI",
    "GetDiskInfo": "/system?action=GetDiskInfo",
    "GetFileBody": "/files?action=GetFileBody",
    "GetLimitNet": "/site?action=GetLimitNet",
    "GetNetWork": "/system?action=GetNetWork",
    "GetPHPVersion": "/site?action=GetPHPVersion",
    "GetProxyList": "/site?action=GetProxyList",
    "GetRewriteList": "/site?action=GetRewriteList",
    "GetSSL": "/site?action=GetSSL",
    "GetSecurity": "/site?action=GetSecurity",
    "GetSiteLogs": "/site?action=GetSiteLogs",
    "GetSitePHPVersion": "/site?action=GetSitePHPVersion",
    "GetSystemTotal": "/system?action=GetSystemTotal",
    "GetTaskCount": "/ajax?action=GetTaskCount",
    "HttpToHttps": "/site?action=HttpToHttps",
    "ModifyProxy": "/site?action=ModifyProxy",
    "ResDatabasePass": "/database?action=ResDatabasePassword",
    "SQLDelBackup": "/database?action=DelBackup",
    "SQLToBackup": "/database?action=ToBackup",
    "SaveFileBody": "/files?action=SaveFileBody",
    "Set301Status": "/site?action=Set301Status",
    "SetHasPwd": "/site?action=SetHasPwd",
    "SetLimitNet": "/site?action=SetLimitNet",
    "SetPHPVersion": "/site?action=SetPHPVersion",
    "SetSSL": "/site?action=SetSSL",
    "SetSecurity": "/site?action=SetSecurity",
    "SetStatus": "/ftp?action=SetStatus",
    "SetUserPassword": "/ftp?action=SetUserPassword",
    "SetupPackage": "/plugin?action=a&name=deployment&s=SetupPackage",
    "UpdatePanel": "/ajax?action=UpdatePanel",
    "WebAddDomain": "/site?action=AddDomain",
    "WebAddSite": "/site?action=AddSite",
    "WebBackupList": "/data?action=getData&table=backup",
    "WebDelBackup": "/site?action=DelBackup",
    "WebDelDomain": "/site?action=DelDomain",
    "WebDeleteSite": "/site?action=DeleteSite",
    "WebDoaminList": "/data?action=getData&table=domain",
    "WebFtpList": "/data?action=getData&table=ftps",
    "WebGetIndex": "/site?action=GetIndex",
    "WebSetEdate": "/site?action=SetEdate",
    "WebSetIndex": "/site?action=SetIndex",
    "WebSetPs": "/data?action=setPs&table=sites",
    "WebSiteStart": "/site?action=SiteStart",
    "WebSiteStop": "/site?action=SiteStop",
    "WebSqlList": "/data?action=getData&table=databases",
    "WebToBackup": "/site?action=ToBackup",
    "Websites": "/data?action=getData&table=sites",
    "Webtypes": "/site?action=get_site_types",
    "deployment": "/plugin?action=a&name=deployment&s=GetList&type=0",
    "download": "/download?filename="
}


## 导入依赖库
import json
import requests
from time import time
from hashlib import md5

## 定义主要函数
def PingBaoTa(ip, port):  # 拼接链接
    return "http://" + ip + ":" + port

def GetMd5(s):  # 参考了Demo.py
    m = md5()
    m.update(s.encode("utf-8"))
    return m.hexdigest()

def GetKeyData(apikey):  # 签名算法
    now_time = time()
    p_data = {
        "request_token": GetMd5(str(now_time) + "" + GetMd5(apikey)),
        "request_time": now_time
    }
    return p_data

## 定义功能（功能详见data.py）
# 系统状态相关接口
def GetSystemTotal(btpanel, btkey):  # 获取系统基础统计
    url = btpanel + config["GetSystemTotal"]
    return requests.post(url, GetKeyData(btkey)).json()

def GetDiskInfo(btpanel, btkey):  # 获取磁盘分区信息
    url = btpanel + config["GetDiskInfo"]
    return requests.post(url, GetKeyData(btkey)).json()

def GetNetWork(btpanel, btkey):  # 获取实时状态信息(CPU、内存、网络、负载)
    url = btpanel + config["GetNetWork"]
    return requests.post(url, GetKeyData(btkey)).json()

def GetTaskCount(btpanel, btkey):  # 检查是否有安装任务
    url = btpanel + config["GetTaskCount"]
    return requests.post(url, GetKeyData(btkey)).json()

def UpdatePanel(btpanel, btkey):  # 检查面板更新
    url = btpanel + config["UpdatePanel"]
    return requests.post(url, GetKeyData(btkey)).json()

# 网站管理相关接口
def Websites(btpanel, btkey):  # 获取网站列表
    url = btpanel + config["Websites"]
    return requests.post(url, GetKeyData(btkey)).json()

def Webtypes(btpanel, btkey):  # 获取网站分类
    url = btpanel + config["Webtypes"]
    return requests.post(url, GetKeyData(btkey)).json()

def GetPHPVersion(btpanel, btkey):  # 获取已安装的 PHP 版本列表
    url = btpanel + config["GetPHPVersion"]
    return requests.post(url, GetKeyData(btkey)).json()

def GetSitePHPVersion(btpanel, btkey):  # 获取指定网站运行的PHP版本
    url = btpanel + config["GetSitePHPVersion"]
    return requests.post(url, GetKeyData(btkey)).json()

def SetPHPVersion(btpanel, btkey, site, php):  # 修改指定网站PHP版本 $site=网站名;$php=PHP版本如73
    data = GetKeyData(btkey)
    data["siteName"] = site
    data["version"] = php
    url = btpanel + config["SetPHPVersion"]
    return requests.post(url, data).json()

def GetSiteID(btpanel, btkey, site):   # 获取指定站点ID 若站点不存在则返回-1
    data = Websites(btpanel, btkey)["data"]
    for i in data:
        if i["name"] == site:
            return i["id"]
    return -1

def GetSitePath(btpanel, btkey, site):   # 获取指定站点目录 若站点不存在则返回-1
    data = Websites(btpanel, btkey)["data"]
    for i in data:
        if i["name"] == site:
            return i["path"]
    return -1

def SetHasPwd(btpanel, btkey, site, username, passwd):  # 开启并设置网站密码访问 $site=网站名;$username=用户名;$passwd=密码
    data = GetKeyData(btkey)
    data["id"] = GetSiteID(btpanel, btkey, site)
    data["username"] = username
    data["password"] = passwd
    url = btpanel + config["SetHasPwd"]
    return requests.post(url, data).json()

def CloseHasPwd(btpanel, btkey, site):  # 关闭网站密码访问 $site=网站名
    data = GetKeyData(btkey)
    data["id"] = GetSiteID(btpanel, btkey, site)
    url = btpanel + config["CloseHasPwd"]
    return requests.post(url, data).json()

def GetDirUserINI(btpanel, btkey, site):  # 获取网站几项开关（防跨站、日志、密码访问）$site=网站名
    data = GetKeyData(btkey)
    data["id"] = GetSiteID(btpanel, btkey, site)
    data["path"] = GetSitePath(btpanel, btkey, site)
    url = btpanel + config["GetDirUserINI"]
    return requests.post(url, data).json()

def GetTypeID(btpanel, btkey, _type):  # 获取分类ID $_type=分类名，若不存在则返回0
    data = Webtypes(btpanel, btkey)
    for i in data:
        if i["name"] == _type:
            return i["id"]
    return 0

def WebAddSite(btpanel, btkey, site, _type, ps, ftp="false", ftp_username=None,ftp_password=None, sql="false", sql_codeing="utf8mb4", datauser=None, datapassword=None):  # 创建网站
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   网站主域名
    _type                  网站分类名
    ps                     网站备注
    ftp="false"            是否开启FTP (true/false)
    ftp_username=None      FTP用户名
    ftp_password=None      FTP密码 
    sql="false"            是否开启SQL (true/false)
    sql_codeing="utf8mb4"  MySQL数据库格式,默认为utf8mb4
    datauser=None          数据库用户名
    datapassword=None      数据库密码
    """
    data = GetKeyData(btkey)
    data["webname"] = json.dumps({"domain":site,"domainlist":[],"count":0})
    data["path"] = "/www/wwwroot/" + site
    data["type_id"] = GetTypeID(btpanel, btkey, _type)
    data["type"] = "PHP"
    data["version"] = GetPHPVersion(btpanel, btkey)[-1]["version"]
    data["port"] = "80"
    data["ps"] = ps
    data["ftp"] = ftp
    if ftp_password != None and ftp_username != None and ftp == "true":
        data["ftp_username"] = ftp_username
        data["ftp_password"] = ftp_password
    data["sql"] = sql
    if datauser != None and datapassword != None and sql == "true":
        data["datauser"] = datauser
        data["datapassword"] = datapassword
        data["codeing"] = sql_codeing
    url = btpanel + config["WebAddSite"]
    return requests.post(url, data).json()

def WebDeleteSite(btpanel, btkey, site, ftp="false", database="false", path="false"):  # 删除网站
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   网站名
    ftp="false"            是否删除FTP (true/false)
    database="false"       是否删除数据库 (true/false)
    path="false"           是否删除站点根目录 (true/false)
    """
    url = btpanel + config["WebDeleteSite"]
    data = GetKeyData(btkey)
    data["id"] = GetSiteID(btpanel, btkey, site)
    data["webname"] = site
    data["ftp"] = ftp
    data["database"] = database 
    data["path"] = path
    return requests.post(url, data).json()

def WebSiteStop(btpanel, btkey, site):  # 停用网站
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   网站名
    """
    url = btpanel + config["WebSiteStop"]
    data = GetKeyData(btkey)
    data["id"] = str(GetSiteID(btpanel, btkey, site))
    data["name"] = site
    return requests.post(url, data).text

def WebSiteStart(btpanel, btkey, site):  # 启用网站
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   网站名
    """
    url = btpanel + config["WebSiteStart"]
    data = GetKeyData(btkey)
    data["id"] = GetSiteID(btpanel, btkey, site)
    data["name"] = site
    return requests.post(url, data).json()

def WebSetEdate(btpanel, btkey, site, edate):  # 设置网站到期时间
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   网站名
    edate                  到期时间 格式为xxxx-xx-xx 若需永久请输入0000-00-00
    """
    url = btpanel + config["WebSetEdate"]
    data = GetKeyData(btkey)
    data["id"] = GetSiteID(btpanel, btkey, site)
    data["edate"] = edate
    return requests.post(url, data).json()

def WebSetPs(btpanel, btkey, site, ps):  # 修改网站备注
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   网站名
    ps                     备注
    """
    url = btpanel + config["WebSetPs"]
    data = GetKeyData(btkey)
    data["id"] = GetSiteID(btpanel, btkey, site)
    data["ps"] = ps
    return requests.post(url, data).json()

def WebBackupList(btpanel, btkey, site, p="1", limit="5", tojs="get_site_backup"):  # 获取网站备份列表
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   网站名
    p                      当前分页
    limit                  每页取回的数据行数
    tojs                   分页 JS 回调,若不传则构造 URI 分页连接
    """
    url = btpanel + config["WebBackupList"]
    data = GetKeyData(btkey)
    data["search"] = GetSiteID(btpanel, btkey, site)
    data["p"] = p
    data["limit"] = limit
    data["type"] = "0"
    data["tojs"] = tojs
    return requests.post(url, data).json()

def WebToBackup(btpanel, btkey, site):  # 创建网站备份
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   网站名
    """
    url = btpanel + config["WebToBackup"]
    data = GetKeyData(btkey)
    data["id"] = GetSiteID(btpanel, btkey, site)
    return requests.post(url, data).json()

def WebDelBackup(btpanel, btkey, id):  # 删除网站备份
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    id                     备份列表 ID
    """
    url = btpanel + config["WebDelBackup"]
    data = GetKeyData(btkey)
    data["id"] = id
    return requests.post(url, data).json()

def WebDoaminList(btpanel, btkey, site):  # 获取网站域名列表
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   网站名
    """
    url = btpanel + config["WebDoaminList"]
    data = GetKeyData(btkey)
    data["search"] = GetSiteID(btpanel, btkey, site)
    data["list"] = "true"
    return requests.post(url, data).json()

def GetDirBinding(btpanel, btkey, site):  # 获取网站域名绑定二级目录信息
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   网站名
    """
    url = btpanel + config["GetDirBinding"]
    data = GetKeyData(btkey)
    data["id"] = GetSiteID(btpanel, btkey, site)
    return requests.post(url, data).json()

def AddDirBinding(btpanel, btkey, site, domain, dirName):  # 添加网站子目录域名
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   网站名
    domain                 域名
    dirName                目录
    """
    url = btpanel + config["AddDirBinding"]
    data = GetKeyData(btkey)
    data["id"] = GetSiteID(btpanel, btkey, site)
    data["domain"] = domain
    data["dirName"] = dirName
    return requests.post(url, data).json()

def DelDirBinding(btpanel, btkey, dirid):  # 删除网站绑定子目录
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    dirid                  子目录ID
    """
    url = btpanel + config["DelDirBinding"]
    data = GetKeyData(btkey)
    data["id"] = dirid
    return requests.post(url, data).json()

def GetDirRewrite(btpanel, btkey, dirid):  # 获取网站子目录绑定伪静态信息
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    dirid                  子目录ID
    """
    url = btpanel + config["GetDirRewrite"]
    data = GetKeyData(btkey)
    data["id"] = dirid
    return requests.post(url, data).json()

def WebAddDomain(btpanel, btkey, site, domain):  # 添加网站域名
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   网站名
    domain                 新增的域名
    """
    url = btpanel + config["WebAddDomain"]
    data = GetKeyData(btkey)
    data["id"] = GetSiteID(btpanel, btkey, site)
    data["webname"] = site
    data["domain"] = domain
    return requests.post(url, data).json()

def WebDelDomain(btpanel, btkey, site, domain, port):  # 删除网站域名
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   网站名
    domain                 删除的域名
    port                   删除的域名的端口
    """
    url = btpanel + config["WebDelDomain"]
    data = GetKeyData(btkey)
    data["id"] = GetSiteID(btpanel, btkey, site)
    data["webname"] = site
    data["domain"] = domain
    data["port"] = port
    return requests.post(url, data).json()

def GetSiteLogs(btpanel, btkey, site):  # 获取网站日志
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   网站名
    """
    url = btpanel + config["GetSiteLogs"]
    data = GetKeyData(btkey)
    data["siteName"] = site
    return requests.post(url, data).json()

def GetSecurity(btpanel, btkey, site):  # 获取网站盗链状态及规则信息
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   域名
    """
    url = btpanel + config["GetSecurity"]
    data = GetKeyData(btkey)
    data["id"] = GetSiteID(btpanel, btkey, site)
    data["name"] = site
    return requests.post(url, data).json()

def SetSecurity(btpanel, btkey, site, fix, domains, status):  # 获取网站盗链状态及规则信息
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   网站名
    fix                    URL后缀  如"jpg,jpeg,gif,png,js,css"
    domains                许可域名  
    status                 启用防盗链状态: "true"/"false"
    """
    url = btpanel + config["SetSecurity"]
    data = GetKeyData(btkey)
    data["id"] = GetSiteID(btpanel, btkey, site)
    data["name"] = site
    data["fix"] = fix
    data["domains"] = domains
    data["status"] = status
    return requests.post(url, data).json()

def GetSSL(btpanel, btkey, site):  # 获取SSL状态及证书详情
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   域名
    """
    url = btpanel + config["GetSSL"]
    data = GetKeyData(btkey)
    data["siteName"] = site
    return requests.post(url, data).json()

def HttpToHttps(btpanel, btkey, site):  # 开启强制HTTPS
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   域名
    """
    url = btpanel + config["HttpToHttps"]
    data = GetKeyData(btkey)
    data["siteName"] = site
    return requests.post(url, data).json()

def CloseToHttps(btpanel, btkey, site):  # 关闭强制HTTPS
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   域名
    """
    url = btpanel + config["CloseToHttps"]
    data = GetKeyData(btkey)
    data["siteName"] = site
    return requests.post(url, data).json()

def SetSSL(btpanel, btkey, site, key, csr, type="1"):  # 设置SSL证书
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    type                   类型 (暂不明确用途 
    site                   域名
    key                    证书key
    csr                    证书PEM
    """
    url = btpanel + config["SetSSL"]
    data = GetKeyData(btkey)
    data["type"] = type
    data["siteName"] = site
    data["key"] = key
    data["csr"] = csr
    return requests.post(url, data).json()

def CloseSSLConf(btpanel, btkey, site, updateOf="1"):  # 关闭SSL
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   域名
    updateOf               修改状态码 (暂不明确用途
    """
    url = btpanel + config["CloseSSLConf"]
    data = GetKeyData(btkey)
    data["siteName"] = site
    data["updateOf"] = updateOf
    return requests.post(url, data).json()

def WebGetIndex(btpanel, btkey, site):  # 获取网站默认文件
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   网站名
    """
    url = btpanel + config["WebGetIndex"]
    data = GetKeyData(btkey)
    data["id"] = GetSiteID(btpanel, btkey, site)
    return requests.post(url, data).json()

def WebSetIndex(btpanel, btkey, site, index):  # 设置网站默认文件
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   网站名
    index                  默认文件内容，如 "api.php,index.php,index.html,index.htm,default.php,default.htm,default.html"
    """
    url = btpanel + config["WebSetIndex"]
    data = GetKeyData(btkey)
    data["id"] = GetSiteID(btpanel, btkey, site)
    data["Index"] = index
    return requests.post(url, data).json()

def GetLimitNet(btpanel, btkey, site):   # 获取网站流量限制信息
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   网站名
    """
    url = btpanel + config["GetLimitNet"]
    data = GetKeyData(btkey)
    data["id"] = GetSiteID(btpanel, btkey, site)
    return requests.post(url, data).json()

def  SetLimitNet(btpanel, btkey, site, perserver, perip, limit_rate):   # 设置网站流量限制信息
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   网站名
    perserver              并发限制
    perip                  单IP限制
    limit_rate             流量限制
    """
    url = btpanel + config["GetLimitNet"]
    data = GetKeyData(btkey)
    data["id"] = GetSiteID(btpanel, btkey, site)
    data["perserver"] = perserver
    data["perip"] = perip
    data["limit_rate"] = limit_rate
    return requests.post(url, data).json()

def CloseLimitNet(btpanel, btkey, site):   # 关闭网站流量限制
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   网站名
    """
    url = btpanel + config["CloseLimitNet"]
    data = GetKeyData(btkey)
    data["id"] = GetSiteID(btpanel, btkey, site)
    return requests.post(url, data).json()

def Get301Status(btpanel, btkey, site):   # 获取网站301重定向信息
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   网站名
    """
    url = btpanel + config["Get301Status"]
    data = GetKeyData(btkey)
    data["siteName"] = site
    return requests.post(url, data).json()

def Set301Status(btpanel, btkey, site, toDomain, srcDomain, type):   # 设置网站301重定向信息
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   网站名
    toDomain               目标Url
	srcDomain              来自Url
	type                   类型
    """
    url = btpanel + config["Set301Status"]
    data = GetKeyData(btkey)
    data["siteName"] = site
    data['toDomain'] = toDomain
    data['srcDomain'] = srcDomain
    data['type'] = type
    return requests.post(url, data).json()

def GetRewriteList(btpanel, btkey, site):   # 获取可选的预定义伪静态列表
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   网站名
    """
    url = btpanel + config["GetRewriteList"]
    data = GetKeyData(btkey)
    data["siteName"] = site
    return requests.post(url, data).json()

def GetFileBody(btpanel, btkey, path, type):   # 获取预置伪静态规则内容（文件内容）
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    path                   规则名（站点名）
	type                   0->获取内置伪静态规则；1->获取当前站点伪静态规则
    """
    url = btpanel + config["GetFileBody"]
    data = GetKeyData(btkey)
    if type:
        path_dir = "vhost/rewrite"
    else:
        path_dir = "rewrite/nginx"
    """
    获取当前站点伪静态规则
	/www/server/panel/vhost/rewrite/user_hvVBT_1.test.com.conf
	获取内置伪静态规则
	/www/server/panel/rewrite/nginx/EmpireCMS.conf
	保存伪静态规则到站点
	/www/server/panel/vhost/rewrite/user_hvVBT_1.test.com.conf
	/www/server/panel/rewrite/nginx/typecho.conf
    """
    data['path'] = '/www/server/panel/' + path_dir + '/' + path + '.conf'
    return requests.post(url, data).json()

def SaveFileBody(btpanel, btkey, path, _data, encoding="utf-8", type=0):   # 保存伪静态规则内容(保存文件内容)
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    path                   规则名（站点名）
	_data                  规则内容
	encoding               规则编码强转utf-8
	type                   0->系统默认路径；1->自定义全路径
    """
    url = btpanel + config["SaveFileBody"]
    data = GetKeyData(btkey)
    if type:
        path_dir = path
    else:
        path_dir = '/www/server/panel/vhost/rewrite/' + path + '.conf'
    data['path'] = path_dir
    data['data'] = _data
    data['encoding'] = encoding
    return requests.post(url, data).json()

def GetProxyList(btpanel, btkey, site):   # 获取网站反代信息及状态
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    site                   网站名
    """
    url = btpanel + config["GetProxyList"]
    data = GetKeyData(btkey)
    data["sitename"] = site
    return requests.post(url, data).json()

def ModifyProxy(btpanel, btkey, cache, proxyname, cachetime, proxydir, proxysite, todomain, advanced, sitename, subfilter, type):   # 修改网站反代信息
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    cache                  是否缓存
	proxyname              代理名称
	cachetime              缓存时长 /小时
	proxydir               代理目录
	proxysite              反代URL
	todomain               目标域名
	advanced               高级功能：开启代理目录
	sitename               网站名
	subfilter              文本替换json格式[{"sub1":"百度","sub2":"白底"},{"sub1":"","sub2":""}]
	type                   开启或关闭 0关;1开
    """
    url = btpanel + config["GetProxyList"]
    data = GetKeyData(btkey)
    data['cache'] = cache
    data['proxyname'] = proxyname
    data['cachetime'] = cachetime
    data['proxydir'] = proxydir
    data['proxysite'] = proxysite
    data['todomain'] = todomain
    data['advanced'] = advanced
    data['sitename'] = sitename
    data['subfilter'] = subfilter
    data['type'] = type
    return requests.post(url, data).json()

def CreateProxy(btpanel, btkey, cache, proxyname, cachetime, proxydir, proxysite, todomain, advanced, sitename, subfilter, type):   # 添加网站反代信息
    """
    btpanel                面板地址,可用PingBaoTa()拼接
    btkey                  API密匙
    cache                  是否缓存
	proxyname              代理名称
	cachetime              缓存时长 /小时
	proxydir               代理目录
	proxysite              反代URL
	todomain               目标域名
	advanced               高级功能：开启代理目录
	sitename               网站名
	subfilter              文本替换json格式[{"sub1":"百度","sub2":"白底"},{"sub1":"","sub2":""}]
	type                   开启或关闭 0关;1开
    """
    url = btpanel + config["CreateProxy"]
    data = GetKeyData(btkey)
    data['cache'] = cache
    data['proxyname'] = proxyname
    data['cachetime'] = cachetime
    data['proxydir'] = proxydir
    data['proxysite'] = proxysite
    data['todomain'] = todomain
    data['advanced'] = advanced
    data['sitename'] = sitename
    data['subfilter'] = subfilter
    data['type'] = type
    return requests.post(url, data).json()

# Ftp管理
def WebFtpList(btpanel, btkey, page='1', limit='15', type='-1', order='id desc', tojs='', search=''):   # 获取网站FTP列表
    """
	page   当前分页
	limit  取出的数据行数
	type   分类标识 -1: 分部分类 0: 默认分类
	order  排序规则 使用 id 降序：id desc 使用名称升序：name desc
	tojs   分页 JS 回调,若不传则构造 URI 分页连接
	search 搜索内容
	"""
    url = btpanel + config["WebFtpList"]
    data = GetKeyData(btkey)
    data['p'] = page
    data['limit'] = limit
    data['type'] = type
    data['order'] = order
    data['tojs'] = tojs
    data['search'] = search
    return requests.post(url, data).json()

def GetFTPID(btpanel, btkey, ftp_username):  # 根据Ftp_Username获取FTPID
    # ftp_username为FTP用户名
    data = WebFtpList(btpanel, btkey)
    for i in data['data']:
        if i['name'] == ftp_username:
            return i['id']
    return -1

def SetUserPassword(btpanel, btkey, ftp_username, new_password):  # 修改FTP账号密码
    """
    ftp_username 用户名
	new_password 密码
    """
    url = btpanel + config["SetUserPassword"]
    data = GetKeyData(btkey)
    data["id"] = GetFTPID(btpanel, btkey, ftp_username)
    data["ftp_username"] = ftp_username
    data["new_password"] = new_password
    return requests.post(url, data).json()

def SetStatus(btpanel, btkey, ftp_username, status):  # 启用/禁用FTP
    """
    ftp_username 用户名
	status       状态 0->关闭;1->开启
    """
    url = btpanel + config["SetStatus"]
    data = GetKeyData(btkey)
    data["id"] = GetFTPID(btpanel, btkey, ftp_username)
    data["username"] = ftp_username
    data["status"] = status
    return requests.post(url, data).json()

# Sql管理
def WebSqlList(btpanel, btkey, page='1', limit='15', type='-1', order='id desc', tojs='', search=''):   # 获取SQL信息列表
    """
	page   当前分页
	limit  取出的数据行数
	type   分类标识 -1: 分部分类 0: 默认分类
	order  排序规则 使用 id 降序：id desc 使用名称升序：name desc
	tojs   分页 JS 回调,若不传则构造 URI 分页连接
	search 搜索内容
	"""
    url = btpanel + config["WebSqlList"]
    data = GetKeyData(btkey)
    data['p'] = page
    data['limit'] = limit
    data['type'] = type
    data['order'] = order
    data['tojs'] = tojs
    data['search'] = search
    return requests.post(url, data).json()

def GetSQLID(btpanel, btkey, sql_username):  # 根据数据库名获取SQLID
    # sql_username为SQL用户名
    data = WebSqlList(btpanel, btkey)
    for i in data['data']:
        if i['name'] == sql_username:
            return i['id']
    return -1

def ResDatabasePass(btpanel, btkey, ftp_username, new_password):  # 修改数据库账号密码
    """
    ftp_username 数据库名
	new_password 新密码
    """
    url = btpanel + config["ResDatabasePass"]
    data = GetKeyData(btkey)
    data["id"] = GetSQLID(btpanel, btkey, ftp_username)
    data["name"] = ftp_username
    data["password"] = new_password
    return requests.post(url, data).json()

def SQLToBackup(btpanel, btkey, database_name):  # 创建sql备份
    """
    database_name 数据库名
    """
    url = btpanel + config["SQLToBackup"]
    data = GetKeyData(btkey)
    data["id"] = GetSQLID(btpanel, btkey, database_name)
    return requests.post(url, data).json()

def SQLDelBackup(btpanel, btkey, id):  # 删除sql备份
    """
    id 备份ID
    """
    url = btpanel + config["SQLDelBackup"]
    data = GetKeyData(btkey)
    data["id"] = id
    return requests.post(url, data).json()

# 插件管理
def deployment(btpanel, btkey, search=False):  # 获取宝塔一键部署列表
    """
    search 搜索关键词
    """
    url = btpanel + config["deployment"]
    if search:
        url = url + "&search=" + search
        print(url)
    data = GetKeyData(btkey)
    return requests.post(url, data).json()

def SetupPackage(btpanel, btkey, dname, site_name, php_version):  # 宝塔一键部署执行
    """
    dname         部署程序名
	site_name     部署到网站名
	php_version   PHP版本
    """
    url = btpanel + config["SetupPackage"]
    data = GetKeyData(btkey)
    data['dname'] = dname
    data['site_name'] = site_name
    data['php_version'] = php_version
    return requests.post(url, data).json()

# Demo
if __name__ == "__main__":
    _ApiKey = "xxxxxxxxxxxxxxxx"
    _BtPanel = "127.0.0.1"
    _Port = "8888"
    _Url = PingBaoTa(_BtPanel, _Port)
    print(GetSystemTotal(_Url, _ApiKey))

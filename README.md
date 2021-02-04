# BtPanel-Python-SDK
 * @ 作者 Abudu
 * @ 参考 阿良 or Youngxj(二次开发)
 * @ 官方API文档 https://www.bt.cn/api-doc.pdf
 * @ 博客 https://www.abudu.top
 * @ Github https://github.com/am-abudu/BtPanel-API-Python-SDK
 * @ 版本 0.1
# 完成情况（可用方法）
## 系统状态相关接口
+  GetSystemTotal  获取系统基础统计 √
+  GetDiskInfo  获取磁盘分区信息 √
+  GetNetWork  获取实时状态信息(CPU、内存、网络、负载) √
+  GetTaskCount 检查是否有安装任务 √
+  UpdatePanel 检查面板更新 √
## 网站管理相关接口
+  Websites  获取网站列表 √
+  Webtypes  获取网站分类 √
+  GetSiteID  获取指定站点ID若站点不存在则返回-1 √
+  GetPHPVersion  获取已安装的 PHP 版本列表 √
+  GetSitePHPVersion  获取指定网站运行的PHP版本 √
+  SetPHPVersion  修改指定网站的PHP版本 √
+  GetTypeID     获取分类ID若分类不存在则返回0 √
+  SetHasPwd  开启并设置网站密码访问 √
+  CloseHasPwd  关闭网站密码访问 √
+  GetDirUserINI  获取网站几项开关（防跨站、日志、密码访问） √
+  WebAddSite   创建网站 √
+  WebDeleteSite  删除网站 √
+  WebSiteStop  停用网站 √
+  WebSiteStart  启用网站 √
+  WebSetEdate  设置网站有效期 √
+  WebSetPs  修改网站备注 √
+  WebBackupList  获取网站备份列表 √
+  WebToBackup  创建网站备份 √
+  WebDelBackup  删除网站备份 √
+  WebDoaminList  获取网站域名列表 √
+  GetDirBinding  获取网站域名绑定二级目录信息 √
+  AddDirBinding  添加网站子目录域名 √
+  DelDirBinding  删除网站绑定子目录 √
+  GetDirRewrite  获取网站子目录伪静态规则 √
+  WebAddDomain  添加网站域名 √
+  WebDelDomain  删除网站域名  √
+  GetSiteLogs  获取网站日志 √
+  GetSecurity  获取网站盗链状态及规则信息 √
+  SetSecurity  设置网站盗链状态及规则信息 √
+  GetSSL  获取SSL状态及证书详情 √
+  HttpToHttps  强制HTTPS √
+  CloseToHttps 关闭强制HTTPS √
+  SetSSL  设置SSL证书 √
+  CloseSSLConf  关闭SSL √
+  WebGetIndex  获取网站默认文件 √
+  WebSetIndex  设置网站默认文件 √
+  GetLimitNet  获取网站流量限制信息 √
+  SetLimitNet  设置网站流量限制信息 √
+  CloseLimitNet  关闭网站流量限制 √
+  Get301Status  获取网站301重定向信息 √
+  Set301Status  设置网站301重定向信息 √
+  GetRewriteList 获取可选的预定义伪静态列表 √
+  GetFileBody  获取指定预定义伪静态规则内容(获取文件内容) √
+  SaveFileBody  保存伪静态规则内容(保存文件内容) √
+  GetProxyList  获取网站反代信息及状态 √
+  CreateProxy  添加网站反代信息 √
+  ModifyProxy  修改网站反代信息 √
## Ftp管理
+  WebFtpList 获取FTP信息列表 √
+  SetUserPassword  修改FTP账号密码 √
+  GetFTPID  根据Ftp_Username获取FTPID √
+  SetStatus  启用/禁用FTP √
## Sql管理
+  WebSqlList 获取SQL信息列表 √
+  ResDatabasePass 修改SQL账号密码 √
+  GetSQLID 根据数据库名获取SQLID √
+  SQLToBackup  创建sql备份 √
+  SQLDelBackup  删除sql备份 √
## 插件管理 
+  deployment  宝塔一键部署列表 √
+  SetupPackage 部署任务 √

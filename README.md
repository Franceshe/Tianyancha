# Tianyancha
输入目标企业的模糊名称/简称，一行代码将目标企业的制定工商信息分类保存为Excel/JSON文件。

* **模拟登录**：基于Selenium的Xpath来定位登录框并传入个人账户信息,一次登录大概6-9秒。
* **关键字的模糊识别**：利用天眼查搜索框的已有模糊检索能力，方便用户仅能提供部分关键字的情况。
* **元素定位**：特殊表格（比如'baseInfo'）使用了Selenium提供的API，具体请参考[Locating Elements](https://selenium-python.readthedocs.io/locating-elements.html)。一般表格使用pandas的[read_html](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_html.html)方法。

## 使用方法 Instruction
**输入更换为自己的天眼查账户、密码和查询关键字。** 生成的结果文件请参考`北京鸿智慧通实业有限公司.xlsx`和`中信证券股份有限公司.json`。

运行下面的示例代码将执行：“用户User输入密码Password登录后，爬取关键字为Keyword的企业的工商信息(baseInfo)，结果返回table_dict并保存为JSON文件。”
```python
from tianyancha import Tianyancha
table_dict = Tianyancha(username='User', password='Password').tianyancha_scraper(keyword='Keyword', table='baseInfo', export='json')
```

### 函数参数 Function Parameters
Tianyancha.**tianyancha_scraper**(keyword, table='all', use_default_exception=True, change_page_interval=2, export='xlsx'):

| 参数  | 类型 | 说明  | 范例 |
|---|---| --- | --- |
| keyword| string | 公司名称，支持模糊或部分检索。| "北京鸿智慧通实业有限公司" |
| table  | list or string, default 'all' | 需要爬取的表格信息。和官方的元素名称一致，具体请参考表格名称中英文对照表。 | ['baseInfo', 'staff', 'invest'] |
| use_default_exception | boolean, default True | 是否使用默认的排除列表。以忽略低价值表格为代价来加快爬取速度。| False|
| change_page_interval| float, default 2 | 爬取多页的时间间隔(秒)。避免频率过快IP地址被官方封禁。| 1.5 |
| export | string, default 'xlsx' | 输出保存格式，'xlsx'/'json'。 | 'json'|


### 表格参数对照表   Table Parameters Mapping Chart
参数结尾有"*"的为可能有误的参数名称，请手工复查`div._container_`后面的内容。

<table><tbody>

  <table width="713" border="0" cellpadding="0" cellspacing="0" style='width:427.80pt;border-collapse:collapse;table-layout:fixed;'>
    <td></td>
    <th >名称</th>
    <th >参数</th>
    <th >说明</th>
   </tr>
   <tr>
    <th rowspan="12">上市信息&nbsp;Listed information</th>
    <td>股票行情</td>
    <td>volatilityNum</td>
    <td ></td>
   </tr>
   <tr>
    <td>企业简介</td>
    <td >stockNum</td>
    <td ></td>
   </tr>
   <tr  >
    <td >高管信息</td>
    <td >seniorPeople</td>
    <td ></td>
   </tr>
   <tr  >
    <td >参股控股</td>
    <td >holdingCompany</td>
    <td ></td>
   </tr>
   <tr  >
    <td >上市公告</td>
    <td >announcement</td>
    <td ></td>
   </tr>
   <tr>
    <td >十大股东</td>
    <td >topTenNum</td>
    <td ></td>
   </tr>
   <tr>
    <td >十大流通</td>
    <td >tenTradableNum</td>
    <td ></td>
   </tr>
   <tr>
    <td >发行相关</td>
    <td >issuanceRelatedNum</td>
    <td ></td>
   </tr>
   <tr  >
    <td >股本结构</td>
    <td >shareStructure</td>
    <td ></td>
   </tr>
   <tr  >
    <td >股本变动</td>
    <td >equityChange</td>
    <td ></td>
   </tr>
   <tr >
    <td >分红情况</td>
    <td >bonus</td>
    <td ></td>
   </tr>
   <tr >
    <td >配股情况</td>
    <td >allotment</td>
    <td ></td>
   </tr>
   <tr >
   </tr>
   <tr>
    <th rowspan="14">公司背景&nbsp;Company background</th>
    <td >工商信息</td>
    <td >baseInfo</td>
    <td >企业基础工商信息，包含统一社会信用代码/注册资本/注册日期/法定代表人/经营范围等信息。</td>
   </tr>
   <tr >
    <td >天眼风险</td>
    <td >riskInfo</td>
    <td ></td>
   </tr>
   <tr>
    <td >股权穿透图</td>
    <td >graphTreeInfo</td>
    <td ></td>
   </tr>
   <tr>
    <td >主要人员</td>
    <td >staff</td>
    <td ></td>
   </tr>
   <tr>
    <td >股东信息 </td>
    <td >holder</td>
    <td ></td>
   </tr>
   <tr >
    <td >对外投资</td>
    <td >invest</td>
    <td ></td>
   </tr>
   <tr >
    <td >最终受益人</td>
    <td >humanholding</td>
    <td ></td>
   </tr>
   <tr >
    <td >实际控制权</td>
    <td >companyholding</td>
    <td ></td>
   </tr>
   <tr >
    <td >财务简析</td>
    <td >financialAnalysis*</td>
    <td >付费可见内容。</td>
   </tr>
   <tr >
    <td >企业关系</td>
    <td >graph</td>
    <td ></td>
   </tr>
   <tr >
    <td >变更记录</td>
    <td >changeinfo</td>
    <td ></td>
   </tr>
   <tr >
    <td >历史沿革</td>
    <td >graphTimeInfo</td>
    <td ></td>
   </tr>
   <tr  >
    <td >公司年报</td>
    <td >report*</td>
    <td ></td>
   </tr>
   <tr >
    <td >分支机构</td>
    <td >branch</td>
    <td ></td>
   </tr>
   <tr >
   </tr>
   <tr>
    <th rowspan="6">司法风险&nbsp;Judicial risk</th>
    <td >开庭公告</td>
    <td >announcementCount</td>
    <td ></td>
   </tr>
   <tr >
    <td >法律诉讼</td>
    <td >lawsuit</td>
    <td ></td>
   </tr>
   <tr >
    <td >法院公告</td>
    <td >court</td>
    <td ></td>
   </tr>
   <tr >
    <td >失信人信息</td>
    <td >dishonest</td>
    <td ></td>
   </tr>
   <tr >
    <td >被执行人</td>
    <td >zhixing</td>
    <td ></td>
   </tr>
   <tr  >
    <td >司法协助</td>
    <td ></td>
    <td ></td>
   </tr>
   <tr >
   </tr >
   <tr>
    <th rowspan="10" ing>经营风险 Operational risks</th>
    <td >经营异常</td>
    <td >abnormal</td>
    <td ></td>
   </tr>
   <tr  >
    <td >行政处罚</td>
    <td >punish,
         punishmentCreditchina</td>
    <td ></td>
   </tr>
   <tr >
    <td >严重违法</td>
    <td ></td>
    <td ></td>
   </tr>
   <tr >
    <td >股权出质</td>
    <td >equity</td>
    <td ></td>
   </tr>
   <tr >
    <td >动产抵押</td>
    <td ></td>
    <td ></td>
   </tr>
   <tr  >
    <td >欠税公告</td>
    <td ></td>
    <td ></td>
   </tr>
   <tr >
    <td >司法拍卖</td>
    <td >judicialSale</td>
    <td ></td>
   </tr>
   <tr >
    <td >清算信息</td>
    <td ></td>
    <td ></td>
   </tr>
   <tr >
    <td >知识产权出质</td>
    <td ></td>
    <td ></td>
   </tr>
   <tr >
    <td >公示催告</td>
    <td >publicnoticeItem</td>
    <td ></td>
   </tr>
   <tr >
   </tr >
   <tr >
    <th   rowspan="5" >公司发展&nbsp;Company development</th>
    <td >融资历史</td>
    <td >rongzi</td>
    <td ></td>
   </tr>
   <tr  >
    <td >核心团队</td>
    <td >teamMember</td>
    <td ></td>
   </tr>
   <tr >
    <td >企业业务</td>
    <td >firmProduct</td>
    <td ></td>
   </tr>
   <tr >
    <td >投资事件</td>
    <td >touzi</td>
    <td ></td>
   </tr>
   <tr >
    <td >竞品信息</td>
    <td >jingpin</td>
    <td ></td>
   </tr>
   <tr  >
    <th  rowspan="12" >经营状况 Operation status </th>
    <td >招聘信息</td>
    <td >recruit</td>
    <td ></td>
   </tr>
   <tr  >
    <td >行政许可</td>
    <td >licensing
    licensingXyzg</td>
    <td ></td>
   </tr>
   <tr >
    <td >税务评级</td>
    <td >taxcredit</td>
    <td ></td>
   </tr>
   <tr >
    <td >抽查检查</td>
    <td >check</td>
    <td ></td>
   </tr>
   <tr >
    <td >资质证书</td>
    <td >certificate</td>
    <td ></td>
   </tr>
   <tr >
    <td >招投标信息</td>
    <td >bid</td>
    <td ></td>
   </tr>
   <tr  >
    <td >产品信息</td>
    <td >product</td>
    <td ></td>
   </tr>
   <tr >
    <td >微信公众号</td>
    <td >wechat</td>
    <td ></td>
   </tr>
   <tr  >
    <td >进出口信用</td>
    <td >importAndExport</td>
    <td ></td>
   </tr>
   <tr >
    <td >债券信息</td>
    <td >bond</td>
    <td ></td>
   </tr>
   <tr >
    <td >购地信息</td>
    <td >purchaselandV2</td>
    <td ></td>
   </tr>
   <tr  >
    <td >电信许可</td>
    <td >permission</td>
    <td ></td>
   </tr>
   <tr >
   </tr >
   <tr >
    <th rowspan="5">知识产权 Intellectual property</td>
    <td >商标信息</td>
    <td >tminfo</td>
    <td ></td>
   </tr>
   <tr >
    <td >专利信息</td>
    <td >patent</td>
    <td ></td>
   </tr>
   <tr >
    <td >软件著作权</td>
    <td >copyright</td>
    <td ></td>
   </tr>
   <tr >
    <td >作品著作权</td>
    <td >copyrightWorks</td>
    <td ></td>
   </tr>
   <tr >
   <td >网站备案</td>
   <td >icp</td>
   <td ></td>
   </tr >
   <tr  >
    <th rowspan="13">历史信息&nbsp;Past</td>
   </tr>
   <tr >
    <td >工商信息</td>
    <td >pastICCount</td>
    <td ></td>
   </tr>
   <tr >
    <td >股东信息</td>
    <td >pastHolderCount</td>
    <td ></td>
   </tr>
   <tr >
    <td >对外投资</td>
    <td >pastInvestCount</td>
    <td ></td>
   </tr>
   <tr >
    <td >开庭公告</td>
    <td >pastAnnouncementCount</td>
    <td ></td>
   </tr>
   <tr >
    <td >法律诉讼</td>
    <td >passtLawsuitCount</td>
    <td ></td>
   </tr>
   <tr >
    <td >法院公告</td>
    <td >pastCourtCount</td>
    <td ></td>
   </tr>
   <tr >
    <td >失信人信息</td>
    <td >pastDishonest</td>
    <td ></td>
   </tr>
   <tr >
    <td >被执行人</td>
    <td >pastZhixing</td>
    <td ></td>
   </tr>
   <tr  >
    <td >行政处罚</td>
    <td >pastPunishmentIC,
    pastPunishmentCreditCN</td>
    <td ></td>
   </tr>
   <tr >
    <td >股权出质</td>
    <td >pastEquitycount</td>
    <td ></td>
   </tr>
   <tr >
    <td >动产抵押</td>
    <td ></td>
    <td ></td>
   </tr>
   <tr  >
    <td >行政许可</td>
    <td >getPastLicenseCN</td>
    <td ></td>
   </tr>
</table>


## 运行依赖 Dependencies
1. [Chrome浏览器](https://www.google.com/chrome/)
2. Chrome-webdriver：将`chromedriver.exe`(Windows)或`chromedriver.dmg`(Mac)移动到本地Python安装目录下。
    1. [百度网盘下载](https://pan.baidu.com/s/1zMSlbRtL6RHhJdp0NL0bcg)
    2. [官方下载](https://sites.google.com/a/chromium.org/chromedriver/downloads)(需要代理访问)
3. `Requirements.txt`

## 捐助 Donation
捐助是一种美德。 :heart::yellow_heart::blue_heart:
1. 资金
<img src="https://user-images.githubusercontent.com/10396208/49501270-6dcd4580-f8ad-11e8-89c9-ff30922df917.jpg" width="300" height="300" />
<!--- Alipay
<img src="https://user-images.githubusercontent.com/10396208/49501461-e03e2580-f8ad-11e8-8c21-3cb9b71cb18a.jpg" width="300" />
-->
2. 点赞
请为知乎相关问题的[回答](像天眼查这种网站怎么进行全爬虫？ - 张乔的回答 - 知乎
https://www.zhihu.com/question/277100386/answer/569032807)点赞，帮助更多人受惠于本项目。

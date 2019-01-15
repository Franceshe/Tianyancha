# Tianyancha
输入目标企业的模糊名称/简称，一行代码将目标企业的工商信息分类保存为Excel/JSON文件。

* **模拟登录**：基于PyAutoGUI的GUI自动化方式来定位登录框并传入个人账户信息。绕开了官方对Selenium定位元素和Cookies仅能首次成功登陆的限制。GUI自动化方式同比稍慢，一次登录大概25秒。
* **关键字的模糊识别**：利用天眼查搜索框的已有模糊检索能力，方便用户仅能提供部分关键字的情况。
* **元素定位**：特殊表格（比如'baseInfo'）使用了Selenium提供的API，具体请参考[Locating Elements](https://selenium-python.readthedocs.io/locating-elements.html)。一般表格使用pandas的[read_html](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_html.html)方法。

## 使用方法 Instruction
**输入更换为自己的天眼查账户、密码和查询关键字。** 生成的结果文件请参考`北京鸿智慧通实业有限公司.xlsx`和`北京鸿智慧通实业有限公司.json`。

运行下面的示例代码将执行：“用户User输入密码Password登录后，爬取关键字为Keyword的企业的工商信息(baseInfo)，结果保存为JSON文件。”
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

### 表格名称对照表 Table Parameters Mapping Chart

| 名称  | 参数  | 说明  |
|---|---|---|
| **所有表格**   | all  | 所有表格信息，非官方字段。  |
| **工商信息** | baseInfo | 企业基础工商信息，包含统一社会信用代码/注册资本/注册日期/法定代表人/经营范围等信息  |
| 主要人员  | staff  |   |
| 上市公告 | announcement |  |
| 招聘 | recruit  |   |
| 知识产权  | tminfo  |  |
| 参股控股  | holdingCompany  |   |
| 分红情况  | bonus  |   |
| 对外投资  | invest  |   |
| 企业业务  | firmProduct  |   |
| 竞品信息  | jingpin  |   |
| 招投标  | bid  |   |
| 税务评级  | taxcredit  |   |
| 资质证书  | certificate  |   |
| 专利信息  | patent  |   |
| 软件著作权  | copyright  |   |
| 最终受益人  | humanholding  |   |
| 实际控制权  | companyholding  |   |
| 变更记录  | changeinfo  |   |
| 分支机构  | branch  |   |
| 进出口信用  | importAndExport |   |
| 名称  | product  |   |
| 作品著作权  | copyrightWorks  |   |
| 微信公众号  | wechat  |   |
| 网站备案  | icp  |   |
| 开庭公告  | announcementcourt  |   |
| 法律诉讼  | lawsuit  |   |
| 法院公告  | court  |   |
| 投资事件  | touzi  |   |
| 司法拍卖  | judicialSale  |   |
| 债券信息  | bond  |   |
| 核心团队  | teamMember  |   |
| 抽查检查  | check  |   ||


### 表格名称中英对照表   Table Parameters Mapping Chart


<table><tbody>

  <table width="713" border="0" cellpadding="0" cellspacing="0" style='width:427.80pt;border-collapse:collapse;table-layout:fixed;'>
    <td></td>
    <th >名称</th>
    <th >参数</th>
    <th >说明</th>
   </tr>
   <tr>
    <th rowspan="11">上市信息 Listed information</th>
    <td>股票行情</td>
    <td>volatilityNum</td>
    <td ></td>
   </tr>
   <tr>
    <td>企业简介</td>
    <td >brief introduction</td>
    <td ></td>
   </tr>
   <tr  >
    <td >高管信息</td>
    <td >Executive information</td>
    <td ></td>
   </tr>
   <tr  >
    <td >参股控股</td>
    <td >quity participation</td>
    <td ></td>
   </tr>
   <tr  >
    <td >上市公告</td>
    <td >announcement</td>
    <td ></td>
   </tr>
   <tr>
    <td >十大股东</td>
    <td >Ten major stockholders</td>
    <td ></td>
   </tr>
   <tr>
    <td >十大流通</td>
    <td >Ten majior tradable shareholders</td>
    <td ></td>
   </tr>
   <tr>
    <td >发行相关</td>
    <td >Issuance related</td>
    <td ></td>
   </tr>
   <tr  >
    <td >股本结构</td>
    <td >Capital stock structure</td>
    <td ></td>
   </tr>
   <tr  >
    <td >股本变动</td>
    <td >Capital stock changes</td>
    <td ></td>
   </tr>
   <tr >
    <td >分红情况</td>
    <td >Dividends</td>
    <td ></td>
   </tr>
   <tr>
    <th rowspan="14">公司背景 Company background</th>
    <td >工商信息</td>
    <td >baseInfo</td>
    <td >企业基础工商信息，包含统一社会信用代码/注册资本/注册日期/法定代表人/经营范围等信息</td>
   </tr>
   <tr >
    <td >天眼风险</td>
    <td >Risks</td>
    <td ></td>
   </tr>
   <tr>
    <td >股权穿透图</td>
    <td ></td>
    <td ></td>
   </tr>
   <tr>
    <td >主要人员</td>
    <td >staff</td>
    <td ></td>
   </tr>
   <tr>
    <td >股东信息 </td>
    <td >Shareholders information</td>
    <td ></td>
   </tr>
   <tr >
    <td >对外投资</td>
    <td >Investment</td>
    <td ></td>
   </tr>
   <tr >
    <td >最终受益人</td>
    <td >humanholding</td>
    <td ></td>
   </tr>
   <tr >
    <td >实际控制权</td>
    <td > Owenership</td>
    <td ></td>
   </tr>
   <tr >
    <td >财务简析</td>
    <td >Brief commercial analise</td>
    <td ></td>
   </tr>
   <tr >
    <td >企业关系</td>
    <td >Related company</td>
    <td ></td>
   </tr>
   <tr >
    <td >变更记录</td>
    <td >Reform record</td>
    <td ></td>
   </tr>
   <tr >
    <td >历史沿革</td>
    <td >Historical evolution</td>
    <td ></td>
   </tr>
   <tr  >
    <td >公司年报</td>
    <td >Company annual report</td>
    <td ></td>
   </tr>
   <tr >
    <td >分支机构</td>
    <td >Affiliates</td>
    <td ></td>
   </tr>
   <tr >
   </tr>
   <tr>
    <th rowspan="6">司法风险 Judicial risk</th>
    <td >开庭公告</td>
    <td >announcement of court session </td>
    <td ></td>
   </tr>
   <tr >
    <td >法律诉讼</td>
    <td >lawsuit</td>
    <td ></td>
   </tr>
   <tr >
    <td >法院公告</td>
    <td >Court bulletin</td>
    <td ></td>
   </tr>
   <tr >
    <td >失信人信息</td>
    <td >dishonest person</td>
    <td ></td>
   </tr>
   <tr >
    <td >被执行人</td>
    <td >person subjected to execution</td>
    <td ></td>
   </tr>
   <tr  >
    <td >司法协助</td>
    <td >Judicial assistance</td>
    <td ></td>
   </tr>
   <tr >
   </tr >
   <tr>
    <th rowspan="10" ing>经营风险 Operational risks</th>
    <td >经营异常</td>
    <td >Abnormal operation</td>
    <td ></td>
   </tr>
   <tr  >
    <td >行政处罚</td>
    <td >administrative penalty</td>
    <td ></td>
   </tr>
   <tr >
    <td >严重违法</td>
    <td >Serious illegal</td>
    <td ></td>
   </tr>
   <tr >
    <td >股权出质</td>
    <td >Equity pledge</td>
    <td ></td>
   </tr>
   <tr >
    <td >动产抵押</td>
    <td >Chattel mortgage</td>
    <td ></td>
   </tr>
   <tr  >
    <td >欠税公告</td>
    <td >overdue bulletin </td>
    <td ></td>
   </tr>
   <tr >
    <td >司法拍卖</td>
    <td >judicial sale</td>
    <td ></td>
   </tr>
   <tr >
    <td >清算信息</td>
    <td >Accounting information</td>
    <td ></td>
   </tr>
   <tr >
    <td >知识产权出质</td>
    <td >Intellectual property pledge</td>
    <td ></td>
   </tr>
   <tr >
    <td >公示催告</td>
    <td >Public notice</td>
    <td ></td>
   </tr>
   <tr >
   </tr >
   <tr >
    <th   rowspan="5" >公司发展 Company development</th>
    <td >融资历史</td>
    <td >Financing history</td>
    <td ></td>
   </tr>
   <tr  >
    <td >核心团队</td>
    <td >core teammember</td>
    <td ></td>
   </tr>
   <tr >
    <td >企业业务</td>
    <td >firmProduct</td>
    <td ></td>
   </tr>
   <tr >
    <td >投资事件</td>
    <td >investment issue</td>
    <td ></td>
   </tr>
   <tr >
    <td >竞品信息</td>
    <td >competing product</td>
    <td ></td>
   </tr>
   <tr  >
    <th  rowspan="12" >经营状况Operation status </th>
    <td >招聘信息</td>
    <td >recruitment</td>
    <td ></td>
   </tr>
   <tr  >
    <td >行政许可</td>
    <td >administrative licensing</td>
    <td ></td>
   </tr>
   <tr >
    <td >税务评级</td>
    <td >tax credit</td>
    <td ></td>
   </tr>
   <tr >
    <td >抽查检查</td>
    <td >spot check</td>
    <td ></td>
   </tr>
   <tr >
    <td >资质证书</td>
    <td >qualification certificate</td>
    <td ></td>
   </tr>
   <tr >
    <td >招投标信息</td>
    <td >bidding </td>
    <td ></td>
   </tr>
   <tr  >
    <td >产品信息</td>
    <td >product information</td>
    <td ></td>
   </tr>
   <tr >
    <td >微信公众号</td>
    <td >wechat</td>
    <td ></td>
   </tr>
   <tr  >
    <td >进出口信用</td>
    <td >Import and export</td>
    <td ></td>
   </tr>
   <tr >
    <td >债券信息</td>
    <td >bond</td>
    <td ></td>
   </tr>
   <tr >
    <td >购地信息</td>
    <td >land purchase</td>
    <td ></td>
   </tr>
   <tr  >
    <td >电信许可</td>
    <td >telecommunications license</td>
    <td ></td>
   </tr>
   <tr >
   </tr >
   <tr >
    <th rowspan="4">知识产权 Intellectual property</td>
    <td >商标信息</td>
    <td >trademark</td>
    <td ></td>
   </tr>
   <tr >
    <td >专利信息</td>
    <td >patent</td>
    <td ></td>
   </tr>
   <tr >
    <td >软件著作权</td>
    <td >software copyright</td>
    <td ></td>
   </tr>
   <tr >
    <td >作品著作权</td>
    <td >copyright</td>
    <td ></td>
   </tr>
   <tr >
   </tr >
   <tr  >
    <th rowspan="13">历史信息 History</td>
    <td >网站备案</td>
    <td >websit registration</td>
    <td ></td>
   </tr>
   <tr >
    <td >工商信息</td>
    <td >baseInfo</td>
    <td ></td>
   </tr>
   <tr >
    <td >股东信息</td>
    <td >Shareholders information</td>
    <td ></td>
   </tr>
   <tr >
    <td >对外投资</td>
    <td >investment</td>
    <td ></td>
   </tr>
   <tr >
    <td >开庭公告</td>
    <td >announcement of court session </td>
    <td ></td>
   </tr>
   <tr >
    <td >法律诉讼</td>
    <td >lawsuit</td>
    <td ></td>
   </tr>
   <tr >
    <td >法院公告</td>
    <td >Court bulletin</td>
    <td ></td>
   </tr>
   <tr >
    <td >失信人信息</td>
    <td >dishonest person</td>
    <td ></td>
   </tr>
   <tr >
    <td >被执行人</td>
    <td >person subjected to execution</td>
    <td ></td>
   </tr>
   <tr  >
    <td >行政处罚</td>
    <td >administrative penalty</td>
    <td ></td>
   </tr>
   <tr >
    <td >股权出质</td>
    <td >Equity pledge</td>
    <td ></td>
   </tr>
   <tr >
    <td >动产抵押</td>
    <td >Chattel mortgage</td>
    <td ></td>
   </tr>
   <tr  >
    <td >行政许可</td>
    <td >administrative licensing</td>
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

<img src="https://user-images.githubusercontent.com/10396208/49501270-6dcd4580-f8ad-11e8-89c9-ff30922df917.jpg" width="300" height="300" />
<!--- Alipay
<img src="https://user-images.githubusercontent.com/10396208/49501461-e03e2580-f8ad-11e8-8c21-3cb9b71cb18a.jpg" width="300" />
-->

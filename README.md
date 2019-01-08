# Tianyancha
输入目标企业的模糊名称/简称，一行代码将目标企业的工商信息分类保存为Excel/JSON文件。

## 设计思想 Design
### 模拟登录

基于PyAutoGUI的GUI自动化方式来定位登录框并传入个人账户信息。绕开了官方对Selenium定位元素和Cookies仅能首次成功登陆的限制。GUI自动化方式同比稍慢，一次登录大概25秒。

### 数据爬取
1. 关键字的模糊识别：利用天眼查搜索框的已有模糊检索能力，方便用户仅能提供部分关键字的情况。
2. 元素定位：特殊表格（比如'baseInfo'）使用了Selenium提供的API，具体请参考[Locating Elements](https://selenium-python.readthedocs.io/locating-elements.html)。一般表格使用pandas的[read_html](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_html.html)方法。

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

### 表格名称对照表 Table Parameters Matching Chart

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
| 名称  | judicialSale  |   |
| 债券信息  | bond  |   |
| 核心团队  | teamMember  |   |
| 抽查检查  | check  |   |

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



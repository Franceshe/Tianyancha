# Tianyancha
输入目标企业的模糊名称/简称，一行代码将目标企业的工商信息分类保存为Excel/JSON文件。

## 使用方法 Instruction
**输入更换为自己的天眼查账户、密码和查询关键字。** 生成的结果文件请参考`北京鸿智慧通实业有限公司.xlsx`和`北京鸿智慧通实业有限公司.json`。
```python
from tianyancha import Tianyancha
table_dict = Tianyancha(username='User', password='Password').tianyancha_scraper(keyword='Keyword', table='baseInfo', export='json')
```

<!--- ![demo](https://user-images.githubusercontent.com/10396208/40413412-5875fa46-5ea8-11e8-975a-546290cb746c.gif) -->

### 表格名称对照表 Table Parameters Matching Chart
本列表可能不全，欢迎补充。

| 名称  | 参数  | 说明  |
|---|---|---|
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



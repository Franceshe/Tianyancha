# Tianyancha
输入目标企业的模糊名称/简称，一行代码将目标企业的工商信息分类保存为Excel/JSON文件。

## 使用方法 Instruction
**输入更换为自己的天眼查账户、密码和查询关键字。** 生成的结果文件请参考`北京鸿智慧通实业有限公司.xlsx`和`北京鸿智慧通实业有限公司.json`。
    
    from tianyancha import Tianyancha
    table_dict = Tianyancha(username='User', password='Password').tianyancha_scraper(keyword='Keyword', table='baseInfo', export='json')

<!--- ![demo](https://user-images.githubusercontent.com/10396208/40413412-5875fa46-5ea8-11e8-975a-546290cb746c.gif) -->

### 表格名称对照表 Table Parameters Matching Chart


## 运行依赖 Dependencies
1. [Chrome浏览器](https://www.google.com/chrome/)
2. Chrome-webdriver：将`chromedriver.exe`(Windows)或`chromedriver.dmg`(Mac)移动到本地Python安装目录下。
    1. [百度网盘下载](https://pan.baidu.com/s/1zMSlbRtL6RHhJdp0NL0bcg)
    2. [官方下载](https://sites.google.com/a/chromium.org/chromedriver/downloads)(需要代理访问)
3. `Requirements.txt`

## 捐助 Donation
捐助是一种美德。 :kissing_heart:

<img src="https://user-images.githubusercontent.com/10396208/49501270-6dcd4580-f8ad-11e8-89c9-ff30922df917.jpg" width="300" height="300" />
<!--- Alipay
<img src="https://user-images.githubusercontent.com/10396208/49501461-e03e2580-f8ad-11e8-8c21-3cb9b71cb18a.jpg" width="300" />
-->



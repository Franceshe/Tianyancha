# Tianyancha
天眼查企业工商信息下载工具，一行代码将目标企业的工商信息分门别类地保存为Excel文件。

## 运行依赖
1. [Chrome浏览器](https://www.google.com/chrome/)
2. Chrome-webdriver：将`chromedriver.exe`(Windows)或`chromedriver.dmg`(Mac)移动到本地Python安装目录下。
    1. [百度网盘下载](https://pan.baidu.com/s/1zMSlbRtL6RHhJdp0NL0bcg)
    2. [官方下载](https://sites.google.com/a/chromium.org/chromedriver/downloads)(需要代理访问)
3. Requirement.txt

## 使用方法
输入更换为自己的天眼查账户、密码和查询关键字。
    
    from Tianyancha import tianyancha
    table_dict = Tianyancha(username='User', password='Password').tianyancha_scraper(keyword='Keyword')

<!--- ![demo](https://user-images.githubusercontent.com/10396208/40413412-5875fa46-5ea8-11e8-975a-546290cb746c.gif) -->

## 捐助 Donation
<img src="https://user-images.githubusercontent.com/10396208/49501270-6dcd4580-f8ad-11e8-89c9-ff30922df917.jpg" width="300" height="300" />
<!--- Alipay
<img src="https://user-images.githubusercontent.com/10396208/49501461-e03e2580-f8ad-11e8-8c21-3cb9b71cb18a.jpg" width="300" />
-->



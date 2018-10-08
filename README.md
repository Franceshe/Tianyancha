# Tianyancha
天眼查企业工商信息下载工具，一行代码将目标企业的工商信息分门别类地保存为Excel文件。欢迎根据[改进方向](https://github.com/qzcool/Tianyancha#%E6%94%B9%E8%BF%9B%E6%96%B9%E5%90%91)Pull-a-request。

## 运行依赖
1. [Chrome浏览器](https://www.google.com/chrome/)
2. Chrome-webdriver。将`chromedriver.exe`(Windows)或`chromedriver.dmg`(Mac)移动到本地Python安装目录下。
    1. [百度网盘下载](https://pan.baidu.com/s/1zMSlbRtL6RHhJdp0NL0bcg)
    2. [官方下载](https://sites.google.com/a/chromium.org/chromedriver/downloads)(需要代理访问)

## 使用方法
**下载仓库到本地后**，运行.py文件：

![demo](https://user-images.githubusercontent.com/10396208/40413412-5875fa46-5ea8-11e8-975a-546290cb746c.gif)

1. 使用命令行工具执行`/Tianyancha.py`
3. 程序开始运行，对分类信息开始依次爬取，输出结果范例为`000810 创维数字.xlsx`

## 改进方向
1. 性能提升
  1. 非阻塞方法：代理池，引用，Headers的设置
2. API化：类似`get_company_info(keyword)`
3. Browser-driver: 使用PhantomJS代替Chrome-webdriver
4. 数字和中文字符反爬虫编码字体攻克

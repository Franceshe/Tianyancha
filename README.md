# Tianyancha
天眼查企业工商信息下载工具，一行代码将目标企业的工商信息分门别类地保存为Excel文件。欢迎根据`改进方向`Pull-a-request。

## 运行依赖
1. [Chrome浏览器](https://www.google.com/chrome/)
2. Chrome-webdriver。将`chromedriver.exe`(Windows)或`chromedriver.dmg`(Mac)移动到本地Python安装目录下。
    1. [百度网盘下载](https://pan.baidu.com/s/1zMSlbRtL6RHhJdp0NL0bcg)
    2. [官方下载](https://sites.google.com/a/chromium.org/chromedriver/downloads)(需要代理访问)

## 使用方法
**下载仓库到本地后**，根据个人情况选择：

### 1. Jupyter Notebook
1. [Jupyter Notebook](http://jupyter.org/)，建议使用[Anaconda](https://www.anaconda.com/download/)下载安装运行环境。
1. 打开`/JupyterNotebook/Tianyancha.ipynb`
3. 输入查询公司的名称并运行所有代码块
5. 程序开始运行，对分类信息开始依次爬取，输出结果范例为`中信.xlsx`

### 2. 运行.py文件
1. 使用命令行工具执行`/Tianyancha.py`
3. 程序开始运行，对分类信息开始依次爬取，输出结果范例为`中信.xlsx`

~~~~
### 3. 图形界面(GUI)
打包为本地程序，支持[Mac](https://py2app.readthedocs.io/en/latest/)/[Windows](http://www.py2exe.org/)。

进行中，用户名/密码未正确设置。

### 4. Web App
服务化。优点是自主性高，缺点是并发IP请求大。
部署：Heroku/青云

未开始。
~~~~

## 改进方向
1. 性能提升
  1. 非阻塞方法：代理池，引用，Headers的设置
2. API化：类似`get_company_info(keyword)`
3. Browser-driver: 使用PhantomJS代替Chrome-webdriver

from selenium import webdriver
import time,re,os
from bs4 import BeautifulSoup
import pandas as pd

path = os.getcwd().replace('\\','/')+'/'


def open_browser(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver


def log_in(driver):
    # 模拟登陆
    driver.find_element_by_xpath(
        ".//*[@id='web-content']/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/input"). \
        send_keys(username)
    driver.find_element_by_xpath(
        ".//*[@id='web-content']/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[3]/input"). \
        send_keys(password)
    driver.find_element_by_xpath(
        ".//*[@id='web-content']/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[5]").click()
    time.sleep(3)
    return driver


def search_company(driver, url1):
    driver.get(url1)
    content = driver.page_source.encode('utf-8')
    soup1 = BeautifulSoup(content, 'lxml')
    time.sleep(3)
    # company_name = soup1.find('a', class_="query_name sv-search-company f18 in-block vertical-middle").get_text()

    url2 = soup1.find('a', class_="query_name sv-search-company f18 in-block vertical-middle").attrs['href']
    driver.get(url2)
    # content2 = driver.page_source.encode('utf-8')
    # soup2 = BeautifulSoup(content2, 'lxml')
    return driver


def get_base_info(driver):
    base_table = {}
    base_table['名称'] = driver.find_element_by_xpath("//div[@class='company_header_width ie9Style position-rel']/div").text.split('我要认证')[0]
    base_info = driver.find_element_by_xpath("//div[@class='company_header_interior pl10 pt10 pb10 position-rel company-claim-header-bc mt15']")
    base_table['电话'] = base_info.text.split('电话：')[1].split('邮箱：')[0]
    base_table['邮箱'] = base_info.text.split('邮箱：')[1].split('\n')[0]
    base_table['网址'] = base_info.text.split('网址：')[1].split('地址')[0]
    base_table['地址'] = base_info.text.split('地址：')[1].split('\n')[0]
    abstract = driver.find_element_by_xpath("//div[@class='sec-c2 over-hide']/script")
    base_table['简介'] = driver.execute_script("return arguments[0].textContent", abstract).strip()
    tabs = driver.find_elements_by_tag_name('table')

    rows1 = tabs[0].find_elements_by_tag_name('tr')
    base_table['法人代表'] = rows1[1].find_elements_by_tag_name('td')[0].text.split('\n')[0]
    base_table['注册资本'] = rows1[1].find_elements_by_tag_name('td')[1].text.split('\n')[1]
    base_table['注册时间'] = rows1[1].find_elements_by_tag_name('td')[1].text.split('\n')[3]
    base_table['公司状态'] = rows1[1].find_elements_by_tag_name('td')[1].text.split('\n')[5]

    rows2 = tabs[1].find_elements_by_tag_name('tr')
    base_table['工商注册号'] = rows2[0].find_elements_by_tag_name('td')[1].text
    base_table['统一信用代码'] = rows2[1].find_elements_by_tag_name('td')[1].text
    base_table['纳税人识别号'] = rows2[2].find_elements_by_tag_name('td')[1].text
    base_table['营业期限'] = rows2[3].find_elements_by_tag_name('td')[1].text
    base_table['登记机关'] = rows2[4].find_elements_by_tag_name('td')[1].text

    base_table['组织机构代码'] = rows2[0].find_elements_by_tag_name('td')[3].text
    base_table['公司类型'] = rows2[1].find_elements_by_tag_name('td')[3].text
    base_table['行业'] = rows2[2].find_elements_by_tag_name('td')[3].text
    base_table['核准日期'] = rows2[3].find_elements_by_tag_name('td')[3].text
    base_table['英文名称'] = rows2[4].find_elements_by_tag_name('td')[3].text

    base_table['注册地址'] = rows2[5].find_elements_by_tag_name('td')[1].text.split('附近公司')[0]
    base_table['经营范围'] = rows2[6].find_elements_by_tag_name('td')[1].text

    return pd.DataFrame([base_table])


def get_staff_info(driver):
    staff_list = []
    staff_info = driver.find_elements_by_xpath("//div[@class='in-block f14 new-c5 pt9 pl10 overflow-width vertival-middle new-border-right']")
    for i in range(len(staff_info)):
        position = driver.find_elements_by_xpath("//div[@class='in-block f14 new-c5 pt9 pl10 overflow-width vertival-middle new-border-right']")[i].text
        person = driver.find_elements_by_xpath("//a[@class='overflow-width in-block vertival-middle pl15 mb4']")[i].text
        staff_list.append({'职位': position, '人员名称': person})
    staff_table = pd.DataFrame(staff_list, columns=['职位', '人员名称'])
    return staff_table


def tryonclick(table):
    # 测试是否有翻页
    try:
        # 找到有翻页标记
        table.find_element_by_tag_name('ul')
        onclickflag = 1
    except Exception:
        print("没有翻页")
        onclickflag = 0
    return onclickflag


def change_page(table, df):
    PageCount = table.find_element_by_class_name('total').text
    PageCount = re.sub("\D", "", PageCount)  # 使用正则表达式取字符串中的数字 ；\D表示非数字的意思
    for i in range(int(PageCount) - 1):
        button = table.find_element_by_xpath(".//li[@class='pagination-next  ']/a")
        driver.execute_script("arguments[0].click();", button)
        time.sleep(3)
        df2 = get_table_info(table)
        df = df.append(df2)
    return df


def get_table_info(table):
    tab = table.find_element_by_tag_name('table')
    df = pd.read_html('<table>' + tab.get_attribute('innerHTML') + '</table>')
    if isinstance(df, list):
        df = df[0]
    if '操作' in df.columns:
        df = df.drop(columns='操作')
    return df


def scrapy(driver):
    tables = driver.find_elements_by_xpath("//div[contains(@id,'_container_')]")

    # 获取每个表格的名字
    c = '_container_'
    name = [0] * (len(tables) - 2)
    # 生成一个独一无二的十六位参数作为公司标记，一个公司对应一个，需要插入多个数据表
    id = keyword
    table_dict = {}
    for x in range(len(tables)-2):
        name[x] = tables[x].get_attribute('id')
        name[x] = name[x].replace(c, '')  # 可以用这个名称去匹配数据库
        # 判断是表格还是表单
        num = tables[x].find_elements_by_tag_name('table')

        # 基本信息表table有两个
        if len(num) > 1:
            table_dict[name[x]] = get_base_info(driver)

        elif name[x] in ['recruit', 'tmInfo']:
            pass

        #  单纯的表格
        elif len(num) == 1:
            df = get_table_info(tables[x])

            onclickflag = tryonclick(tables[x])
            # 判断此表格是否有翻页功能
            if onclickflag == 1:
                df = change_page(tables[x], df)

            table_dict[name[x]] = df

        # 表单样式
        elif name[x] == 'staff':
           table_dict[name[x]] = get_staff_info(driver)

        else:
            table_dict[name[x]] = pd.DataFrame()

    table_dict['websiteRecords'] = get_table_info(tables[len(tables)-2])

    return table_dict


def gen_excel(table_dict, keyword):
    with pd.ExcelWriter(path+keyword+'.xlsx') as writer:
        for sheet_name in table_dict:
            table_dict[sheet_name].to_excel(writer, sheet_name=sheet_name, index=None)

def get_company_info(keyword):
    url = 'https://www.tianyancha.com/login'
    url1 = 'http://www.tianyancha.com/search?key=%s&checkFrom=searchBox' % keyword
    username = '13488895246'
    password = 'abcd1234'

    driver = open_browser(url)
    driver = log_in(driver)
    driver = search_company(driver, url1)
    table_dict = scrapy(driver)
    gen_excel(table_dict, keyword)

# GUI启动
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.L1 = tk.Label(self, text="用户名")
        self.L1.pack#( side = 'left')
        self.E1 = tk.Entry(self, bd =5)
        self.E1.pack#(side = 'right')

        self.L2 = tk.Label(self, text="密码")
        self.L2.pack()#side = 'left')
        self.E2 = tk.Entry(self, bd =5)
        self.E2.pack()#side = 'right')

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "开始"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="left")

        self.QUIT = tk.Button(self, text="退出", fg="red", command=root.destroy)
        self.QUIT.pack(side="right")

    def say_hi(self):
        username = '13488895246'
        password = 'abcd1234'
        get_company_info(keyword)

root = tk.Tk()
app = Application(master=root)

app.master.title("天眼查数据下载器")
app.master.maxsize(300, 200)

app.mainloop()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Tianyancha: tools to help scrap Tianyancha information'

__author__ = 'Qiao Zhang'

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests, time, re, math, openpyxl, datetime, os, shutil, psutil, platform, pyautogui, subprocess, webbrowser
from tqdm import *
import xlwings as xw
from selenium import webdriver

class Tianyancha():

    # 常量定义
    url = 'https://www.tianyancha.com/login'

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = self.log_in()

    # 登录天眼查
    def log_in(self):
        # 打开浏览器
        driver = webdriver.Chrome()
        driver.get(self.url)

        # 模拟登陆
        driver.find_element_by_xpath(
            ".//*[@id='web-content']/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/input"). \
            send_keys(self.username)
        driver.find_element_by_xpath(
            ".//*[@id='web-content']/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[3]/input"). \
            send_keys(self.password)
        driver.find_element_by_xpath(
            ".//*[@id='web-content']/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[5]").click()
        time.sleep(1)
        return driver

    def tianyancha_scraper(self, keyword,change_page_interval=2):
        # 定义天眼查爬虫

        ## 顺带的名称检查功能，利用天眼查的模糊搜索功能
        def search_company(driver, url1):
            driver.get(url1)
            time.sleep(1)
            content = driver.page_source.encode('utf-8')
            soup1 = BeautifulSoup(content, 'lxml')
            url2 = soup1.find('div',class_='header').find('a', class_="name ").attrs['href']
        #     ## 如果搜索有误，手工定义URL2地址
        #     url2 = 'https://www.tianyancha.com/company/28472888'
            driver.get(url2)
            return driver

        ## Base_info稳健性
        def get_base_info(driver):
            base_table = {}
            base_table['名称'] = driver.find_element_by_xpath("//div[@id='company_web_top']/div[2]/div[2]/div/h1").text
            base_info = driver.find_element_by_class_name('detail')

            ## 爬取数据不完整,要支持展开和多项合并
            base_table['电话'] = base_info.text.split('电话：')[1].split('邮箱：')[0].split('查看')[0]
            base_table['邮箱'] = base_info.text.split('邮箱：')[1].split('\n')[0].split('查看')[0]
            base_table['网址'] = base_info.text.split('网址：')[1].split('地址')[0]
            base_table['地址'] = base_info.text.split('地址：')[1].split('\n')[0]

            try:
                abstract = driver.find_element_by_xpath("//div[@class='summary']/script") # @class='sec-c2 over-hide'
                base_table['简介'] = driver.execute_script("return arguments[0].textContent", abstract).strip()
            except:
                abstract = driver.find_element_by_xpath("//div[@class='summary']")
                base_table['简介'] = driver.execute_script("return arguments[0].textContent", abstract).strip()[3:]

            tabs = driver.find_elements_by_tag_name('table')
            rows1 = tabs[0].find_elements_by_tag_name('tr')

            if len(rows1[1].find_elements_by_tag_name('td')[0].text.split('\n')[0]) < 2:
                base_table['法人代表'] = rows1[1].find_elements_by_tag_name('td')[0].text.split('\n')[1]
            else:
                base_table['法人代表'] = rows1[1].find_elements_by_tag_name('td')[0].text.split('\n')[0]

            ## 注册资本显示不对，需要使用转码函数：可以参考GitHub另一个人的解法
            base_table['注册资本'] = rows1[1].find_elements_by_tag_name('td')[1].text.split('\n')[1]
            ## 公司状态尚未爬取
            base_table['公司状态'] = ''#rows1[1].find_elements_by_tag_name('td')[1].text.split('\n')[5]

            rows2 = tabs[1].find_elements_by_tag_name('tr')

            # 使用循环批量爬取base_table_2
            base_table_2 = pd.DataFrame(columns=['Row_Index','Row_Content'])

            for rows2_row in range(len(rows2)):
                for element_unit in rows2[rows2_row].find_elements_by_tag_name('td'):
                    if element_unit.text != '':
                        base_table_2 = base_table_2.append({'Row_Index':rows2_row,'Row_Content':element_unit.text},ignore_index=True)

            if len(base_table_2) % 2 == 0:
                for i in range(int(len(base_table_2)/2)):
                    base_table[base_table_2.iloc[2*i,1]] = base_table_2.iloc[2*i+1,1] # 将base_table_2的数据装回base_table
            else:
                print ('base_table_2（公司基本信表2）行数不为偶数，请检查代码！')

            # 利用营业期限未加密编码修正注册时间和核准日期
            base_table['注册时间'] = base_table['营业期限'].split('至')[0]#rows1[1].find_elements_by_tag_name('td')[1].text.split('\n')[3] ##直接截取营业期限的起始日
            base_table['核准日期'] = base_table['营业期限'].split('至')[0]

            return pd.DataFrame([base_table])


        # 特殊处理：主要人员
        ## staff_info定位不准？
        def get_staff_info(driver):
            staff_list = []
            staff_info = driver.find_elements_by_xpath("//div[@class='in-block f14 new-c5 pt9 pl10 overflow-width vertival-middle new-border-right']")
            for i in range(len(staff_info)):
                position = driver.find_elements_by_xpath("//div[@class='in-block f14 new-c5 pt9 pl10 overflow-width vertival-middle new-border-right']")[i].text
                person = driver.find_elements_by_xpath("//a[@class='overflow-width in-block vertival-middle pl15 mb4']")[i].text
                staff_list.append({'职位': position, '人员名称': person})
            staff_table = pd.DataFrame(staff_list, columns=['职位', '人员名称'])
            return staff_table


        # 特殊处理:上市公告
        ## 加入类别搜索功能
        def get_announcement_info(driver):
            announcement_df = pd.DataFrame(columns=['序号','日期','上市公告','上市公告网页链接']) ## 子函数自动获取columns
            ### 函数化
            content = driver.page_source.encode('utf-8')
            ## 能不能只Encode局部的driver
            soup = BeautifulSoup(content, 'lxml')
            announcement_info = soup.find('div',id='_container_announcement').find('tbody').find_all('tr')
            for i in range(len(announcement_info)):
                index = announcement_info[i].find_all('td')[0].get_text()
                date = announcement_info[i].find_all('td')[1].get_text()
                announcement = announcement_info[i].find_all('td')[2].get_text()
                announcement_url = 'https://www.tianyancha.com' + announcement_info[i].find_all('td')[2].find('a')['href']
                announcement_df = announcement_df.append({'序号':index,'日期':date,'上市公告':announcement,'上市公告网页链接':announcement_url}, ignore_index=True)
            ###

            ### 判断此表格是否有翻页功能:重新封装change_page函数
            announcement_table = driver.find_element_by_xpath("//div[contains(@id,'_container_announcement')]")
            onclickflag = tryonclick(announcement_table)
            if onclickflag == 1:
                PageCount = announcement_table.find_element_by_class_name('company_pager').text
                PageCount = re.sub("\D", "", PageCount)  # 使用正则表达式取字符串中的数字 ；\D表示非数字的意思
                for i in range(int(PageCount) - 1):
                    button = table.find_element_by_xpath(".//a[@class='num -next']") #历史class_name（天眼查的反爬措施）：'pagination-next  ',''
                    driver.execute_script("arguments[0].click();", button)
                    ####################################################################################
                    time.sleep(change_page_interval)
                    ####################################################################################
            ###
                    ### 函数化
                    content = driver.page_source.encode('utf-8')
                    ## 能不能只Encode局部的driver
                    soup = BeautifulSoup(content, 'lxml')
                    announcement_info = soup.find('div',id='_container_announcement').find('tbody').find_all('tr')
                    for i in range(len(announcement_info)):
                        index = announcement_info[i].find_all('td')[0].get_text()
                        date = announcement_info[i].find_all('td')[1].get_text()
                        announcement = announcement_info[i].find_all('td')[2].get_text()
                        announcement_url = 'https://www.tianyancha.com' + announcement_info[i].find_all('td')[2].find('a')['href']
                        announcement_df = announcement_df.append({'序号':index,'日期':date,'上市公告':announcement,'上市公告网页链接':announcement_url}, ignore_index=True)
                    ###
            return announcement_df


        def tryonclick(table): # table实质上是selenium WebElement
            # 测试是否有翻页
            ## 把条件判断写进tryonclick中
            try:
                # 找到有翻页标记
                table.find_element_by_tag_name('ul')
                onclickflag = 1
            except Exception:
                print("没有翻页") ## 声明表格名称: name[x] +
                onclickflag = 0
            return onclickflag

        def tryontap(table):
            # 测试是否有翻页
            try:
                table.find_element_by_xpath("//div[contains(@class,'over-hide changeTabLine f14')]")
                ontapflag = 1
            except Exception:
                print("没有时间切换页") ## 声明表格名称: name[x] +
                ontapflag = 0
            return ontapflag

        def change_page(table, df):
            ##完善
            PageCount = table.find_element_by_class_name('company_pager').text #历史class_name（天眼查的反爬措施）：'total',
            PageCount = re.sub("\D", "", PageCount)  # 使用正则表达式取字符串中的数字 ；\D表示非数字的意思
            for i in range(int(PageCount) - 1):
                button = table.find_element_by_xpath(".//a[@class='num -next']") #历史class_name（天眼查的反爬措施）：'pagination-next  ',''
                driver.execute_script("arguments[0].click();", button)
                ####################################################################################
                time.sleep(change_page_interval) # 更新换页时间间隔,以应对反爬虫
                ####################################################################################
                df2 = get_table_info(table) ## 应该可以更换不同的get_XXXX_info
                df = df.append(df2)
            return df

        def change_tap(table, df):
            TapCount = len(table.find_elements_by_tag_name('div'))
            for i in range(int(TapCount) - 3):
                button = table.find_elements_by_tag_name('div')[i+3]
                driver.execute_script("arguments[0].click();", button)
                time.sleep(2)
                df2 = get_table_info(table) ## 应该可以更换不同的get_XXXX_info
         ##     df2['日期'] = table.find_elements_by_tag_name('div')[i+3].text
                df = df.append(df2, ignore_index=True)
         ## df = df.drop(columns=['序号'])
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
            # Waiting time for volatilityNum to load
            time.sleep(2)

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

                # 基本信息表：table有两个
                if len(num) > 1: ##需要更好地设置baseinfo的判定条件
                    table_dict[name[x]] = get_base_info(driver)

                #########
                # 排除列表：不同业务可以设置不同分类，实现信息的精准爬取
                #########
                elif name[x] in ['recruit', 'tmInfo', 'holdingCompany', 'bonus', 'invest', 'firmProduct', 'jingpin', \
                                 'bid', 'taxcredit', 'certificate', 'patent', 'copyright', 'product', 'importAndExport', \
                                 'copyrightWorks', 'wechat', 'websiteRecords', 'announcementcourt', 'lawsuit', 'court', \
                                 'branch', 'touzi', 'judicialSale', 'bond', 'teamMember', 'check','recruit']:
                    pass

    #             # 公司高管的特殊处理
    #             elif name[x] == 'staff':
    #                 table_dict[name[x]] = get_staff_info(driver)

                # 公告的特殊处理：加入URL
                elif name[x] == 'announcement':
                    table_dict[name[x]] = get_announcement_info(driver)

                #  单纯的表格进行信息爬取
                ## 含头像的行未对齐
                elif len(num) == 1:

                    print (name[x]) ##检查用

                    df = get_table_info(tables[x])
                    onclickflag = tryonclick(tables[x])
                    ontapflag = tryontap(tables[x])
                    # 判断此表格是否有翻页功能
                    if onclickflag == 1:
                        df = change_page(tables[x], df)
                ##  if ontapflag == 1:
                ##      df = change_tap(tables[x], df)
                    table_dict[name[x]] = df

                else:
                    table_dict[name[x]] = pd.DataFrame()
                    print (name[x]+'为奇怪表格，请检查程序！')

            #table_dict['websiteRecords'] = get_table_info(tables[len(tables)-2])
            return table_dict


        def gen_excel(table_dict, keyword):
            with pd.ExcelWriter(keyword+'.xlsx') as writer:
                for sheet_name in table_dict:
                    table_dict[sheet_name].to_excel(writer, sheet_name=sheet_name, index=None)

        # # 微信通知提醒进度：已进行到'131. XXXX; 35%',声明序号/名称/完成度;发送给自己
        # def notification_wechat():
        #     pass

        # 主程序
        url1 = 'http://www.tianyancha.com/search?key=%s&checkFrom=searchBox' % keyword ## 是否要移到最前面定义？

        self.driver = search_company(self.driver, url1)
        table_dict = scrapy(self.driver)
        gen_excel(table_dict, keyword)
        # notification_wechat()
        return table_dict
        # # 个性操作
        # os.makedirs(path+'/'+'clients'+'/'+ str(i+1) + '. ' + keyword + ' ' + keyword_list_name[i].replace(' ',''))
        # shutil.move(path+'/'+keyword+'.xlsx',path+'/'+'clients'+'/'+ str(i+1) + '. ' + keyword + ' ' + keyword_list_name[i].replace(' ','') +'/'+keyword + ' ' + keyword_list_name[i].replace(' ','') + '.xlsx')
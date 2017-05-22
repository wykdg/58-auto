#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common import action_chains, keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import select

import time
start_url='http://gz.58.com/chuzu/'
city_url='http://www.58.com/chuzu/changecity/'
target_city=u'广州'
user_name='15902084922'
password='58wyk123'
xiaoqu=u"天朗明居"
huxing=u"2"
huxingting=u"2"
huxingwei=u"1"
area=u"40"

floor=u"2"
total_floor=u"5"
minprice=u"1000"
goblianxiren=u'哈哈'
Phone='13288821992'
text=u'环境优雅,贷带宋亮辅导辅导'
check_states=[True,False,True,False,True,False,True,False,True,False,True,False,True]
toward=u'东北'
fittype=u'豪华装修'
object_type=u'公寓'
fukuan=u'押一付二'
localArea=u'天河'
localDiduan=u'东圃'
dizhi=u'三元里大道1220-1224号22'


options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values': {
        'images': 2
    },
    "profile.content_settings.exceptions.images":{
        "post.58.com/*":{"setting":0}
    }
}


options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(chrome_options=options)
# browser=webdriver.Chrome()
browser.set_page_load_timeout(10)
try:
    browser.get(start_url)
except TimeoutException:
    pass
try:
    browser.find_element_by_link_text(u'登录').click()
except TimeoutException:
    pass
try:
    browser.find_element_by_class_name('pwdlogin').click()
except TimeoutException:
    pass

time.sleep(1)
js_value="document.getElementById('passwordUser').style='display: inline-block;'"
browser.execute_script(js_value)
browser.find_element_by_id('usernameUser').send_keys(user_name)


browser.find_element_by_xpath('//input[@type="password"]').send_keys(password)
try:
    browser.find_element_by_class_name('submit').click()
except:
    pass
try:
    browser.get(city_url)
except TimeoutException:
    pass

try:
    browser.find_element_by_link_text(target_city).click()
except TimeoutException:
    pass


fabu_url=browser.find_element_by_link_text(u'免费发布').get_attribute('href')
try:
    browser.get(fabu_url)
except TimeoutException:
    pass


browser.find_element_by_id('xiaoqu').send_keys(xiaoqu)
browser.find_element_by_id('huxingshi').send_keys(huxing)
browser.find_element_by_id('huxingting').send_keys(huxingting)
browser.find_element_by_id('huxingwei').send_keys(huxingwei)
browser.find_element_by_id('area').send_keys(area)

browser.find_element_by_id('Floor').send_keys(floor)
browser.find_element_by_id('zonglouceng').send_keys(total_floor)
browser.find_element_by_id('MinPrice').send_keys(minprice)
# browser.find_element_by_id('miaoshuBtn').click()


img_paths=["C:\\Users\\wangyongkang\\Pictures\\59e2a7efce1b9d1666ab6ac9f3deb48f8d5464ca.jpg"]
for img_path in img_paths:
    browser.find_element_by_xpath('//div[@id="imgUpload"]/div/input').send_keys(img_path)
browser.switch_to.frame('baidu_editor_0')
browser.find_element_by_xpath('/html/body').send_keys(text)
browser.switch_to.parent_frame()
browser.find_element_by_id('goblianxiren').send_keys(goblianxiren)
browser.find_element_by_id('Phone').send_keys(Phone)

checkbox=[6,15, 14, 12 ,11, 9, 10, 8, 13, 17, 674989, 674990, 674991]
for x,check_state in zip(checkbox,check_states):
    check_box=browser.find_element_by_xpath('//div[@data-value="%d"]'%(x,))

    if 'focus' in check_box.get_attribute('class'):
        check=True
    else:
        check=False

    if check !=check_state:
        check_box.click()

time.sleep(1)

selects=['Toward','FitType','ObjectType','fukuanfangshi','localArea','localDiduan']
for selector,value in zip(selects,[toward,fittype,object_type,fukuan,localArea,localDiduan]):
    js_value='document.getElementsByName("%s")[0].children[0].children[0].textContent="%s"'%(selector,value)
    browser.execute_script(js_value)

browser.find_element_by_id('dizhi').send_keys(dizhi)


# browser.find_element_by_xpath('//div[@class="submit_wrap"]/span').click()
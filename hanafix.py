from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import time
import requests 
from seleniumbase import Driver
import pandas as pd 


pname_lis = []
pimg_lis = []
price_lis = []
pcat_lis = []
psku_lis = []
prelate_lis = []
purl_lis = []

pdesc_lis = []
pdesc_html_lis = []

pshort_desc_lis = []
pshort_desc_html_lis = []

spec_lis = []
spec_text_lis = []

pcat_url_lis = []
prelate_prod_url_lis = []

img_new_lis = [] #new




import requests
from bs4 import BeautifulSoup
import pandas as pd


start = 44
end = 64

count = start

driver = Driver(uc=True)


for page in range(start,end+1):

  print("------------------------------- Page {} -------------------------------------".format(page))
  main_url = "https://www.hannathailand.com/shop/page/{}/".format(page)

  driver.get(main_url)

  soup = BeautifulSoup(driver.page_source,'html.parser')
  # soup.prettify()


  link_lis = [ link['href'] for link in soup.find_all('a',attrs={'class':'woocommerce-LoopProduct-link'})]
  print(link_lis)


  print(len(link_lis))


  for url in link_lis:

    driver.get(url)
    soupx = BeautifulSoup(driver.page_source,'html.parser')

    # ลิงค์สินค้า
    print(f"--------------------ลิงค์สินค้า ตัวที่ {count}------------------------")
    print(url)
    purl_lis.append(url)


    # ชื่อสินค้า
    print("--------------------ชื่อสินค้า------------------------")
    try:
      title = soupx.find('h1',{'class':'product-title'}).text.strip()
      print(title)
      pname_lis.append(title)
    except:
      print("ไม่มี")
      pname_lis.append("ไม่มี")


    # หมวดหมู่
    print("--------------------หมวดหมู่------------------------")
    try:
      cat = " , ".join( [ c.text for c in soupx.find('div',{'class':'product_meta'}).find('span',{'class':'posted_in'}).find_all('a')] ).strip()
      print(cat)
      pcat_lis.append(cat)

    except:
      print("ไม่มี")
      pcat_lis.append("ไม่มี")

    # หมวดหมู่
    print("--------------------Link หมวดหมู่------------------------")
    try:
      cat_url = [ c for c in soupx.find('div',{'class':'product_meta'}).find('span',{'class':'posted_in'}).find_all('a')][-1]['href']
      print(cat_url)
      pcat_url_lis.append(cat_url) 
    except: 
      print("ไม่มี")
      pcat_url_lis.append("ไม่มี")


    #sku รหัสสินค้า
    print("--------------------รหัสสินค้า------------------------")
    try:
      sku = " , ".join( [ s.text for s in soupx.find('span',{'class':'sku_wrapper'}).find('span',{'class':'sku'})] ).strip()
      print(sku)
      psku_lis.append(sku)
    except:
      print("ไม่มี")
      psku_lis.append("ไม่มี")

    #ราคา
    print("--------------------ราคา------------------------")
    try:
      price = soupx.find('span',{'class':'woocommerce-Price-amount'}).text.replace('฿',"").strip()
      print(price)
      price_lis.append(price)
    except:
      print("ไม่มี")
      price_lis.append("ไม่มี")

    #รายละเอียดสินค้า
    print("--------------------รายละเอียดสินค้า------------------------")
    try:
      desc = soupx.find('div',{'class':'woocommerce-Tabs-panel--description'}).text.strip()
      print(desc[:100])
      print(soupx.find('div',{'class':'woocommerce-Tabs-panel--description'}))
      pdesc_lis.append(desc)
      pdesc_html_lis.append(soupx.find('div',{'class':'woocommerce-Tabs-panel--description'}))

    except:
      print("ไม่มี")
      pdesc_lis.append("ไม่มี")
      pdesc_html_lis.append('ไม่มี')

    

    #รูปภาพสินค้า
    print("--------------------รูปภาพสินค้า------------------------")
    try:
      img = soupx.find('div',{'class':'woocommerce-product-gallery__image slide first'}).find('a')['href']
      print(img)
      pimg_lis.append(img)
    except:
      print("ไม่มี")
      pimg_lis.append("ไม่มร")



    #รูปภาพสินค้า
    print("--------------------รูปภาพสินค้า thumbnail------------------------")
    try:
      imgx = " , ".join([x['src'] for x in soupx.find_all('img',{'class':'attachment-woocommerce_thumbnail'})])
      print(imgx)
      img_new_lis.append(imgx)
    except:
      print("ไม่มี")
      img_new_lis.append('ไม่มี')

  

    

    #-------------------------------- short description -----------------------------
    try:
      print('--------------------Short Description------------------------')
      short_desc = soupx.find('div',{'class':'product-short-description'})
      print(short_desc)

      # text
      pshort_desc_lis.append(short_desc.text.strip())

      # html
      pshort_desc_html_lis.append(short_desc)
    except:
      print("ไม่มี")
      pshort_desc_lis.append("ไม่มี")
      pshort_desc_html_lis.append("ไม่มี")

    #สินค้าที่เกี่ยวข้อง
    print("--------------------สินค้าที่เกี่ยวข้อง------------------------")
    try:
      relate_prod =" , ".join([ rp.find('a').text.replace("หยิบใส่ตะกร้า","").replace("อ่านเพิ่มเติม","").strip() for rp in soupx.find('div',{'class':'related-products-wrapper'}).find_all('div',{'class':'box-text-products'})])
      print(relate_prod)
      prelate_lis.append(relate_prod)
    except:
      print("ไม่มี")
      prelate_lis.append("ไม่มี")

    #สินค้าที่เกี่ยวข้อง
    print("--------------------Link สินค้าที่เกี่ยวข้อง------------------------")
 
    relate_prod2 =" , ".join([ str(rp.find('a')) for rp in soupx.find('div',{'class':'related-products-wrapper'}).find_all('div',{'class':'box-text-products'})])
    print(relate_prod2)
    prelate_prod_url_lis.append(relate_prod2)
    # except:
    #    print("ไม่มี")
    #    prelate_prod_url_lis.append("ไม่มี")

    print("------------------- Specification HTML -----------------------------------------")
    try:
      spec = soupx.find('div',{'class':'woocommerce-Tabs-panel--additional_information'})
      print(spec)
      # html
      spec_lis.append(spec)
      # text
      spec_text_lis.append(spec.text.strip())
    except:
      print("ไม่มี")
      spec_lis.append("ไม่มี")
      spec_text_lis.append("ไม่มี")


    print()
    print()
    count = count + 1




  #A.append([pdname,pdbrand,pddetail,pdprice,pdimage])
#print(A)

df = pd.DataFrame()
df['ชื่อสินค้า'] = pname_lis
df["หมวดหมู่"] = pcat_lis
df['ลิงค์หมวดหมู่'] = pcat_url_lis
df['ลิงค์สินค้า'] = purl_lis
df['รหัสสินค้า'] = psku_lis
df['ราคา'] = price_lis
df['SPECIFICATION'] = spec_text_lis 
df['SPECIFICATION HTML'] = spec_lis 
df['รายละเอียด'] = pdesc_lis
df['รายละเอียด HTML'] = pdesc_html_lis 
df['รายละเอียด short'] = pshort_desc_lis
df['รายละเอียด short HTML'] = pshort_desc_html_lis 
df['ภาพสินค้า'] = pimg_lis
df['สินค้าที่เกียวข้อง'] = prelate_lis
df['สินค้าที่เกี่ยวข้องพร้อมชื่อและลิงค์'] = prelate_prod_url_lis
df['รูปครบๆ New'] = img_new_lis
df.head()

filename = "newbookPage42To64"
df.to_excel(filename+".xlsx")
print("Save Successful")
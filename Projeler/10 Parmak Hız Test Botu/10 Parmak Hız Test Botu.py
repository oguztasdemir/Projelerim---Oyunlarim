from selenium import webdriver
import time

browser = webdriver.Chrome("/Users/yarentasdemir/Desktop/chromedriver")

url = "https://www.m5bilisim.com/tr/on-parmak/hiz-testi/"
browser.get(url)
time.sleep(3)

browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/div/a").click()
time.sleep(1)
browser.find_element_by_xpath("//*[@id='mcac']/a[2]").click()
time.sleep(1)

i = 1

word_screen = browser.find_element_by_xpath("//*[@id='yaziyaz']")

while i < 1000:
    word = browser.find_element_by_xpath("//*[@id='satir']/span["+str(i)+"]")
    i += 1
    word_screen.send_keys(word.text + " ")
    time.sleep(0.01)





from multiprocessing import freeze_support
freeze_support()
from tkinter import N
from selenium import webdriver
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
import itertools
import threading
import time
import sys

done = False
#here is the animation
def loading():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rSearching for page and position ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r'+result)

def get_pos():
    user=input('What is your chaturbate username?:')
    user=user.lower()
    cam_list=input('Search for your user name in\n1)Featured\n2)Women\n3)Men\n4)Couples\n5)Trans\n')
    if cam_list =='1':
        url='https://chaturbate.com/'
    elif cam_list=='2':
        url='https://chaturbate.com/female-cams/'
    elif cam_list=='3':
        url='https://chaturbate.com/male-cams/'
    elif cam_list=='4':
        url='https://chaturbate.com/couple-cams/'
    elif cam_list=='5':
        url='https://chaturbate.com/trans-cams/'
    options = uc.ChromeOptions()
    options.add_argument("--headless")
    bot = uc.Chrome(options=options)
    t2 = threading.Thread(target=loading)
    t2.start()
    bot.get(url)
    time.sleep(1)
    bot.find_element(By.ID,'close_entrance_terms').click()
    time.sleep(0)
    room_count=0
    found=False
    page_count=1
    last_page=bot.find_element(By.XPATH,'//*[@id="roomlist_pagination"]/ul/li[6]/a').text
    last_page=int(last_page)
    while last_page != page_count+1:
        titles=bot.find_elements(By.CLASS_NAME,'icon_not_following' )
        for t in titles:
            room_name= t.get_attribute('data-slug')
            if room_name == user:
                global done
                done=True
                global result
                result='\nYou are on page '+str(page_count)+' of '+str(last_page)+' room position is '+str(room_count)
                found = True
                time.sleep(5)
                end_prog()
                
            else:
                room_count+=1
        bot.find_element(By.CLASS_NAME,'next').click()
        page_count+=1
        time.sleep(1)
def end_prog():
    input("\nPress any key to quit")
    exit()
if __name__=='__main__':
    get_pos()    
        
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
import wrap
import configparser



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
    online=True
    while online:
        Config = configparser.ConfigParser()
        Config.read("conf.ini")
        user=Config.get('settings', 'user')  
        url=Config.get('settings','url')
        wait_time=Config.get('settings','wait')
        wait_time=int(wait_time)
        options = uc.ChromeOptions()
        options.add_argument("--headless")
        bot = uc.Chrome(options=options)
        t2 = threading.Thread(target=loading)
        t2.start()
        t2.is_alive = True
        bot.get(url)
        time.sleep(1)
        bot.find_element(By.ID,'close_entrance_terms').click()
        time.sleep(0)
        room_count=0
        found=False
        page_count=0
        last_page=bot.find_element(By.XPATH,'//*[@id="roomlist_pagination"]/ul/li[6]/a').text
        last_page=int(last_page)
        while last_page != page_count:
            
            titles=bot.find_elements(By.CLASS_NAME,'icon_not_following' )
            for t in titles:
                room_name= t.get_attribute('data-slug')
                if room_name == user:
                    bot.get('https://chaturbate.com/'+user)
                    time.sleep(2)
                    viewers=bot.find_element(By.XPATH,'//*[@id="users-tab-default"]/span/span').text
                    viewers=viewers.replace('(','')
                    viewers=viewers.replace(')','')
                    viewers=viewers.replace('USERS','')
                    viewers=int(viewers)-1
                    viewers=str(viewers)+' Viewers'
                    bot.close()
                    global done
                    done=True
                    global result
                    result='\nYou are on page '+str(page_count+1)+' of '+str(last_page)+' room position is '+str(room_count)+' you have '+str(viewers)
                    found = True
                    t2.is_alive = False
                    time.sleep(wait_time)
                    wrap.run()
                    exit()
                
                else:
                    room_count+=1
            page_count+=1
            bot.find_element(By.CLASS_NAME,'next').click()
            time.sleep(1)
            #print('on page ',page_count, ' of ',last_page)
        if page_count>=last_page:
            bot.close()
            done=True
            result='You were not found'
            t2.is_alive = False
            timer=30
            while timer >0:
                mins, secs = divmod(timer, 60)
                time_left = '{:02}:{:02}'.format(mins, secs)
                time_left=str(time_left)
                time_left.replace('d','')
                sys.stdout.write('\rRetrying in '+time_left)
                timer-=1
                time.sleep(1)
            wrap.run()
            exit()
            
def main():
    get_pos()
if __name__=='__main__':
    main()    
        
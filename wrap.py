import const_check
import configparser
def run():
    const_check.main()
def settings():
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
    wait_time=input('How often do you want to update your ranking stats? (time input in seconds)')
    config = configparser.ConfigParser()
    config['settings'] = {'user': user,
                    'url': url,
                    'wait':wait_time}
    with open('conf.ini', 'w') as configfile:
        config.write(configfile)
if __name__=='__main__':
    settings()
    run()
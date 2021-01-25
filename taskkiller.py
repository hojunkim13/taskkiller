import psutil
import keyboard

def config_filter(line):
    if '#' in line or line=='':
        return False
    else:
        return True
config = open('config.txt', 'r', encoding='utf-8')
target_list = config.read().replace(' ','').split('\n')
target_list = list(filter(config_filter, target_list))
    
keyboard.read_event()

for proc in psutil.process_iter():
    if proc.name() in target_list:
        proc.kill()
from tkinter import *
import sys
import json
import urllib.request 
import time
import threading

master = Tk()
master.configure(bg="black")

master.title("LIVE listeners on de Zwarte Plak")

master.attributes('-topmost', True)
master.update()


w = Label(master, text="00", font=("Helvetica", 200),fg="white",bg="black")

MAX_RETRY = 1000

def get_html(html_url, timeout=10, decode='utf-8'):
    for tries in range(MAX_RETRY):
        try:
            with urllib.request.urlopen(html_url, timeout=timeout) as response:
                return response.read().decode(decode)
        except Exception as e:
            #logging.warning(str(e) + ',html_url:{0}'.format(html_url))
            if tries < (MAX_RETRY - 1):
                continue
            else:
                print('Has tried {0} times to access url {1}, all failed!'.format(MAX_RETRY, html_url))
                return None
            



def Refresher():
    mystr = get_html('http://173.249.43.24:5000/api/v1/visitors/total')
    
    
    
    if mystr is None :
        w['text'] = "*"
    else:
        data = json.loads(mystr[1:-1])
        print(data)
        w['text'] = data['visitors']
    w.pack()
    
    threading.Timer(5, Refresher).start()


Refresher()
mainloop()

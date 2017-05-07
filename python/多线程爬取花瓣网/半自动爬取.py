import requests
import sys
import json
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import threading
Default_Header = {
    'Accept':'application/json',
    'Cookie': 'UM_distinctid=15b4a443a6118e-036d6b278a21a1-36465d60-100200-15b4a443a624d5; CNZZDATA1256914954=533334989-1483782331-http%253A%252F%252Fwww.poluoluo.com%252F%7C1491595587; referer=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DTgohxC_ctaU6bDKuZQd2D1aOf773OCjmg1NiBWPl5Oa%26wd%3D%26eqid%3D83f31b460004cec900000005590f2707; _f=iVBORw0KGgoAAAANSUhEUgAAADIAAAAUCAYAAADPym6aAAABSklEQVRYR%2B1XOxLCQAiFC9lZ2Xgjr5LcyMbKzoPkCjis2RVx2W%2FiOJqMhSQQeLx9MEEgIpgvQgR8muBs4F%2FbRQDUEy%2BzDtMQ6oxVg38FhDvLXfDdtWzpw%2F%2B9n%2B%2BgZEc%2Bi71X56hmRNMmk%2BhC2NbHR9rWs1yMbhrnqQZiaSSVXHc%2FBz5ocmY6Vrj0%2BRgQi4Vc52OArZjVGSkt1rPWehyLgfCoDaIkcqNXi1SL1x%2BJ0vuW2OPj9DH2%2FbvHaUjugJfxG%2FVEgahtnSwSVcyImc0AQudrWFB43KO2U9XX%2BAbRi3zj7vL2%2Bi5GuCAGIZNJOwamNUYWf7odQIPZgGgWdKeto%2FWVjLipMh%2BvDYjSmaWrVTXyU4xIMCULI6URP5b15OP7FiM8wR6LWXxYtS7EUn3EdoIe364oMdJze2RRICVM9Pqsttl7C6uNzwG5A0REryCcRnCcAAAAAElFTkSuQmCC%2CWin32.1366.768.24; md_href=http%3A%2F%2Fhuaban.com%2Fboards%2F17623739%2F%3Fmd%3D404in; md=404in; _ga=GA1.2.674309131.1483787236; _cnzz_CV1256903590=is-logon%7Clogged-out%7C1494165566805%26md%7C404in%7C1494165567805; __asc=9d73966b15be3307dfdeec94559; __auc=9d73966b15be3307dfdeec94559; crtg_rta=; sid=4dIKOOWyPm8HeyqK029pqiWN9qt.msJ75LsC4jH%2BnvqEouh8j0Cx4zIl54%2F%2FEqIGL5eieuo; CNZZDATA1256903590=1159241347-1494163766-null%7C1494163766',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'X-Request':'JSON',
    'Referer':'http://huaban.com/pins/873774526/',
    'X-Requested-With':'XMLHttpRequest',
    'Accept':'application/json'
}
_session=requests.session()
_session.headers.update(Default_Header)
#http://huaban.com/pins/873774526/?j2erhmc2
#beautiful 必须是一个xml文档或者html文档
#//img.hb.aicdn.com/1c1959991b9ec6b07a25fe8fcdb7d5e3750bc60b181a1-xThGaz_fw658

#多线程下载
class myThread(threading.Thread):
    def __init__(self,imgUrl,fname):
        threading.Thread.__init__(self)
        self.imgUrl=imgUrl
        self.fname=fname
    def run(self):
        print("downloading",self.imgUrl)
        download(self.imgUrl,self.fname)



def download(fileid,type):
    img_url="http://img.hb.aicdn.com/"+fileid
    imgresp=requests.get(img_url)
    byte_img = imgresp.content
    try:
        out = open(type, 'wb')
        out.write(byte_img)
        out.flush()
        out.close()
    except Exception as e:
        print(e)
if __name__ == "__main__":
    #sys.exit(0)
    soup =_session.get('http://huaban.com/pins/873774526/?j2erhmc2')
    url=json.loads(soup.text)
    urlList=url['pin']['board']['pins']
    for i in urlList:
        key=i['file']['key']
        print(key)
        #download(key,key+'.jpg')
        myThread(key,key+'.jpg').start()



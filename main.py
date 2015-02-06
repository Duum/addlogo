# -*- coding: gbk -*-
import Image
import codecs
import os,sys
import Tkinter,tkFileDialog
import ConfigParser
reload(sys)
sys.setdefaultencoding('gbk')
cf=ConfigParser.ConfigParser()
cf.read("dirc.conf")
picdir=(cf.get("sec_a","thedir")).decode('gbk')
t=[]
def GetDesktopPath():
    return os.path.join(os.path.expanduser("~"), 'Desktop')
global imglist
def getdirpath():
    global picdir
    picdir=tkFileDialog.askdirectory(parent=top,initialdir=desk,title=('选择路径'.decode('gbk')))
    if picdir:
        cf.set("sec_a","thedir",picdir)
        cf.write(open("dirc.conf","w"))
        entry.delete('0', 'end')
        entry.insert(0,picdir)
def getdir(picdir=os.getcwd()):
    global imglist
    imglist=os.listdir(picdir)
def start():
    getdir(picdir)
    for tex in imglist:
        if tex.endswith('.jpg') or tex.endswith('.jpeg') or tex.endswith('.png')or tex.endswith('.JPG') or tex.endswith('JPEG') or tex.endswith('PNG'):
            dir=picdir
            fname = dir+"\\"+tex
            im2 = Image.open(fname)
            tex = tex.replace('.jpg', '')
            tex = tex.replace('.jpeg', '')
            tex = tex.replace('.png', '')
            tex = tex.replace('.JPG', '')
            tex = tex.replace('.JPEG', '')
            tex = tex.replace('.PNG', '')
            tex = tex.split('-')
            media = tex[0]
            title = tex[1]
            global t
            if title in t:
                continue
            im1=imdic.get(media)
            im3 = im2.resize((592, 296))
            if im1==None:
                b="\n"+title+" 出现了问题\n"
                text.insert(Tkinter.END,b.decode('gbk'))
                continue
            layer = Image.new('RGBA', im1.size, (0, 0, 0, 0))
            layer.paste(im3, (0, 204))
            im4 = Image.composite(layer, im1, layer)
            if not os.path.exists(desk+r'\带logo的图片'):
               os.makedirs(desk+r'\带logo的图片')
            out=desk+r'\带logo的图片'
            im4.save(os.path.join(out,title+".jpg"),quality=100)
            t.extend([title])
            a=title+" 处理成功 "
            text.insert(Tkinter.END,a.decode('gbk'))
imdic={
            "华盛顿邮报".decode('gbk'):Image.open("source\华盛顿邮报.jpg"),
            "纽约时报".decode('gbk'):Image.open("source\纽约时报.jpg"),
            "9to5google":Image.open("source\9to5google.jpg"),
            "9to5mac":Image.open("source\9to5mac.jpg"),
            "anadtech":Image.open(r"source\anadtech.jpg"),
            "androidpolice":Image.open(r"source\andriodpolice.jpg"),
            "arstechnica":Image.open(r"source\arstechnica.jpg"),
             "appleinsider":Image.open(r"source\appleinsider.jpg"),
            "bbc":Image.open(r"source\BBC.jpg"),
            "businessinsider":Image.open(r"source\businessinsider.jpg"),
            "buzzfeed":Image.open(r"source\buzzfeed.jpg"),
            "cnet":Image.open(r"source\Cnet.jpg"),
            "coindesk":Image.open(r"source\coindesk.jpg"),
            "computerworld":Image.open(r"source\computerworld.jpg"),
            "efytimes":Image.open(r"source\efytimes.jpg"),
            "gadgets":Image.open(r"source\gadgets.jpg"),
            "geekwire":Image.open(r"source\geekwire.jpg"),
            "gigaom":Image.open(r"source\gigaom.jpg"),
            "macrumors":Image.open(r"source\macrumors.jpg"),
            "pcmag":Image.open(r"source\pcmag.jpg"),
            "pcworld":Image.open(r"source\Pcworld.jpg"),
            "mashable":Image.open(r"source\Mashable.jpg"),
            "recoder":Image.open(r"source\recoder.jpg"),
            "searchengineland":Image.open(r"source\searchengineland.jpg"),
            "techcruch":Image.open(r"source\techcruch.jpg"),
            "techdirt":Image.open(r"source\techdirt.jpg"),
            "thenextweb":Image.open(r"source\thenextweb.jpg"),
            "theverge":Image.open(r"source\theverge.jpg"),
            "venturebeat":Image.open(r"source\venturebeat.jpg"),
            "zdnet":Image.open(r"source\zdnet.jpg"),
            "福布斯".decode('gbk'):Image.open(r"source\福布斯.jpg"),
            "赫芬顿邮报".decode('gbk'):Image.open(r"source\赫芬顿邮报.jpg"),
            "华尔街日报".decode('gbk'):Image.open(r"source\华尔街日报.jpg"),
            "今日美国".decode('gbk'):Image.open(r"source\今日美国.jpg"),
            "今日印度".decode('gbk'):Image.open(r"source\今日印度.jpg"),
            "连线".decode('gbk'):Image.open(r"source\连线.jpg"),
            "路透社".decode('gbk'):Image.open(r"source\路透社.jpg"),
            "彭博社".decode('gbk'):Image.open(r"source\彭博社.jpg"),
            "卫报".decode('gbk'):Image.open(r"source\卫报.jpg"),
            "瘾科技".decode('gbk'):Image.open(r"source\瘾科技.jpg"),
            "印度时报".decode('gbk'):Image.open(r"source\印度时报.jpg"),
        }
desk=GetDesktopPath()
top = Tkinter.Tk()
top.title("科技大事件图片处理".decode('gbk'))
frame = Tkinter.Frame(top)
frame.grid()
text =Tkinter.Text(frame)
entry =Tkinter.Entry(frame, width=60)
entry.grid(row=0)
entry.insert(0,picdir)
text.grid(row=2)
A= Tkinter.Button(frame, text ="选取目录".decode('gbk'), command = getdirpath)
A.place(x= 30, y=40, height=40, width=100,)
B = Tkinter.Button(frame, text ="开始处理".decode('gbk'), command = start)
B.place(x= 400, y=40, height=40, width=100,)
top.mainloop()
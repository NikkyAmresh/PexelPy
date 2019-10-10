import requests,json,math,csv,os,random, argparse
from urllib.request import urlopen
from urllib.request import Request
from auth import apikey
parser = argparse.ArgumentParser()
parser.add_argument("category", help="Enter the category of images", nargs='?', const='null', type=str, default='null')
parser.add_argument("f_nm", help="Enter number of images", nargs='?', const=50, type=int, default=50)
parser.add_argument("quality", help="choose image quality", nargs='?', const='null', type=str, default='null')
args=parser.parse_args()
keyword=args.category
def download_file(url,path):
    local_filename = url.split('/')[-1].split('?')[0]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(path+"/"+local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                if chunk: 
                    f.write(chunk)
    return local_filename
def dn(i,lis,keyword,f_num,tmp):
    while i<f_num:
        try:
            url=lis[i]
            download_file(url,keyword+"_pics")
            print(str(i)+" downloaded")
            ff=open('g.py','w')
            ff.write("a='"+keyword+"'\ng="+str(i))
            ff.write("\nt="+str(f_num)+"\ntm='"+tmp+"'")
            ff.close()
            i=int(i)+1
        except Exception as e:
            print(e)
            dn(int(i)+1,lis,keyword,f_num,tmp)
    os.remove("test.py")
    os.remove("g.py")
    import shutil
    shutil.rmtree('__pycache__/')
    exit("Total number of "+str(f_num)+" pics saved to folder '"+keyword+"_pics/'\n Thanks for using this program :) ") 
qltq=args.quality
qlty = {
        "XLQ":"tiny", 
        "LQ":"small", 
        "M":"medium", 
        "HD":"large",
        "FHD":"large2x",
        "N":"original", 
        "P":"portrait", 
        "L":"landscape"
    }
if(keyword=='null'):
    exit("Please enter image categories \n[python app.py category quantity quality]\n\n\or to continue last download  \n[python app.py last]")
else:
    if(keyword=='last' and qltq!="null" and args.f_nm!=50):
        try:
            from g import g
            from g import a
            from g import t
            from test import lis
            import sys
        except Exception as e:
            exit("error encountered while continuing last download...files are missing") 
        dn(int(g)-1,lis,a,t,a)       
    else:
        if(qltq=='null'):   
            print("Please choose image quality ")
            print("\n[*] 'XLQ' for extra low quality")
            print("[*] 'LQ' for low quality")
            print("[*] 'M' for medium quality")
            print("[*] 'HD' for HD quality")
            print("[*] 'FHD' for FHD quality")
            print("[*] 'N' for original quality")
            print("[*] 'P' for portrait")
            print("[*] 'L' for landscape")
            qw=input("Image quality : ").upper()
            qlt=qlty.get(qw,'tt')
            if(qlt=='tt'):
                exit("invalid quality! ")
        else:
            qlt=qlty.get(qltq.upper(),'tt')
            if(qlt=='tt'):
                exit("invalid quality")
        rn=random.randint(1000,9999)
        tmp='temp'+str(rn)
        dirr=keyword+'_pics'
        if(os.path.isdir(tmp)):
            tmp=tmp+str(rn)
        if(os.path.isdir(dirr)):
            dirr=dirr+str(rn)
        os.mkdir(tmp)
        os.mkdir(dirr)    
head={
    "Authorization":apikey
    }
def resp(head,url):
    return requests.get(url,headers=head)
def wr(data,i):
    jsn=data.json()
    page=str(jsn['page'])
    with open(tmp+"/"+str(int(page)-1)+'.json', 'w') as outfile:
        json.dump(jsn, outfile)
    print("fetching links : "+str(math.ceil((100/int(i))*int(page)))+"% ")
i=0
url="https://api.pexels.com/v1/search?query="+keyword+"&per_page=500"
temp=resp(head,url).json()
t_page=temp['total_results']/temp['per_page']
f_num=args.f_nm
if f_num>temp['total_results']:
    print('sorry only ' +str(temp['total_results'])+' images available') 
    ctn=input('Do you wanna download' +str(temp['total_results'])+' images (Y/N): ')
    if (ctn=='y' or ctn=='Y'):
        t_page=temp['total_results']/temp['per_page']
        f_num=temp['total_results']        
    else:
        exit('Thanks for using this programme')
else:
    t_page=math.ceil(f_num/temp['per_page'])
while i<math.ceil(t_page):
    res=resp(head,url)
    wr(res,math.ceil(t_page))
    try:
        url=res.json()['next_page']
        i=i+1
    except:
        break
print("100% completed")
i=0
arr=[]
def json2arr(jsn):
    i=0
    while i<len(jsn['photos']):
        pus(jsn['photos'][i]['src'][qlt])
        i=i+1
def pus(data):
    arr.append(data)
def wt(data):
    with open(tmp+"/test.py", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(data)
while i<math.ceil(t_page):
    with open(tmp+"/"+str(i)+".json") as f:
        data=json.load(f)
    print("preparing links : "+str(math.ceil((100/int(t_page))*int(i)))+"% ")
    json2arr(data)
    i=i+1
print("100% completed") 
wt(arr)
with open(tmp+"/test.py", 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(arr)
src=open(tmp+"/test.py","r")
fline="lis=["    
oline=src.readlines()
oline.insert(0,fline)
src.close()
src=open("test.py","w")
src.writelines(oline)
src.close()
with open("test.py", "a") as myfile:
    myfile.write("]")
from test import lis
f1=open('g.py',"w")
f1.write("a=''\ng=0\n")
f1.write("t=''\ntm=''")
f1.close()
from g import g
import shutil
shutil.rmtree(tmp+'/')
print(str(f_num)+" images ready to download ")      
dn(0,lis,keyword,f_num,tmp)

        

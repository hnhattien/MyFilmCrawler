import os
import idm
import urllib
import m3u8
import requests
import base64
import moviepy.editor as moviepy
import tempfile
import binascii
def m3u8downloadByFFmpeg(m3u8url,namefile,currenturl) :
    try : 
        f = open("./247filmvideo/{}".format(namefile+".mp4"),"wb")
        f.close()

        strCommand = "ffmpeg -headers 'Referer: {header}' -i -loglevel debug '{url}' -c copy {path}{name}".format(url=m3u8url,name="output.ts",path="",header=currenturl)
        print(strCommand)
        if(os.path.isfile("./247filmvideo/{}".format(namefile+".mp4"))) : 
            os.system(strCommand)
        else : 
            print("No File")
        
    except : 
        print("Error Download : "+str(namefile))
def m3u8Download(m3u8url,namefile,currenturl) : 
    temp_path = tempfile.gettempdir()
    request = requests.Session()
    request.trust_env = False
    m3u8Res = request.get(m3u8url)
    m3u8Object = m3u8.loads(m3u8Res.text)
    baseurl = os.path.dirname(m3u8url)
    playlist = m3u8Object.data['segments']
    with open("temp/m3u8_data.m3u8","w") as f :
        f.write(m3u8Res.text)
        f.close()
    
    for i in range(0,len(playlist)) : 
        print(playlist[i]['uri'])
        print(baseurl+playlist[0]['uri'])
        res = request.get("{base}/{file_name}".format(base=baseurl,file_name=playlist[i]['uri']),headers={"Referer" : "https://247phim.com/", "User-Agent" : "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"},stream=True,allow_redirects=True,cookies=None)
        with open(os.path.join(os.getcwd(),"segment_video","segment_{}.ts".format(str(i))),"wb") as f : 
            f.write(res.content)
            f.close()
        with open("exported_video/hello.mp4","ab") as fb :
            with open(os.path.join(os.getcwd(),"segment_video","segment_{}.ts".format(str(i))),"rb") as ts :
                stringDecode = bin(int(binascii.hexlify(ts.read()),16))
                fb.write(stringDecode)    
                ts.close()
            fb.close()
    clip = moviepy.VideoFileClip("hello.mp4")
    clip.write_videofile("he.mp4")
    

        
def m3u8DownloadIDM(m3u8url,namefile,currenturl) : 

    idmDownloader = idm.IDMan()
    idmDownloader.usage()
    idmDownloader.download(link="https://xemtv24h.com/statics/fmp4/films10/00dmbkle/00dmbkle.m3u8",clip=True,referrer="https://247phim.com/",path_to_save="./",postData="https://xemtv24h.com/statics/fmp4/films10/00dmbkle/00dmbkle.m3u8", output="hi.mp4",confirm=True)
    m3u8DownloadIDM("https://xemtv24h.com/statics/fmp4/films10/00dmbkle/00dmbkle.m3u8","","")


# coding=utf-8
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from utils.ueditor.config import *
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from utils.sae_storage import *
# import Image
import os
import time
import urllib2
import uuid
import base64

def __myuploadfile(fileObj, source_pictitle, source_filename, fileorpic='pic'):
    """ 一个公用的上传文件的处理 """
    myresponse = ""
    if fileObj:
        filename = fileObj.name.decode('utf-8', 'ignore')
        fileExt = filename.split('.')[1]
        file_name = str(uuid.uuid1())
        subfolder = time.strftime("%Y%m")
        MEDIA_ROOT = settings.MEDIA_ROOT[0] if isinstance(settings.MEDIA_ROOT , list) else settings.MEDIA_ROOT
        if not os.path.exists(MEDIA_ROOT + subfolder):
            os.makedirs(MEDIA_ROOT + subfolder)
        path = str(subfolder + '/' + file_name + '.' + fileExt)

        if fileExt.lower() in ('jpg', 'jpeg', 'bmp', 'gif', 'png', "rar" , "doc" , "docx", "zip", "pdf", "txt", "swf", "wmv"):

            phisypath = MEDIA_ROOT + path
            destination = open(phisypath, 'wb+')
            for chunk in fileObj.chunks():
                destination.write(chunk)
            destination.close()

            if fileorpic == 'pic':
                if fileExt.lower() in ('jpg', 'jpeg', 'bmp', 'gif', 'png'):
                    im = Image.open(phisypath)
                    im.thumbnail((720, 720))
                    im.save(phisypath)

            real_url = '/upload/' + subfolder + '/' + file_name + '.' + fileExt
            myresponse = "{'original':'%s','url':'%s','title':'%s','state':'%s'}" % (source_filename, real_url, source_pictitle, 'SUCCESS')
    return myresponse


@csrf_exempt
def ueditor_ImgUp(request):
    """ 上传图片 """
    fileObj = request.FILES.get('upfile', None)
    source_pictitle = request.POST.get('pictitle', '')
    source_filename = request.POST.get('fileName', '')
    response = HttpResponse()
    myresponse = __myuploadfile(fileObj, source_pictitle, source_filename, 'pic')
    response.write(myresponse)
    return response


@csrf_exempt
def ueditor_FileUp(request):
    """ 上传文件 """
    fileObj = request.FILES.get('upfile', None)
    source_pictitle = request.POST.get('pictitle', '')
    source_filename = request.POST.get('fileName', '')
    response = HttpResponse()
    myresponse = __myuploadfile(fileObj, source_pictitle, source_filename, 'file')
    response.write(myresponse)
    return response

@csrf_exempt
def ueditor_ScrawUp(request):
    """ 涂鸦文件,处理 """
    print request
    param = request.POST.get("action", '')
    fileType = [".gif" , ".png" , ".jpg" , ".jpeg" , ".bmp"]

    if  param == 'tmpImg':
        fileObj = request.FILES.get('upfile', None)
        source_pictitle = request.POST.get('pictitle', '')
        source_filename = request.POST.get('fileName', '')
        response = HttpResponse()
        myresponse = __myuploadfile(fileObj, source_pictitle, source_filename, 'pic')
        myresponsedict = dict(myresponse)
        url = myresponsedict.get('url', '')
        response.write("<script>parent.ue_callback('%s','%s')</script>" % (url, 'SUCCESS'))
        return response
    else:
        #========================base64上传的文件=======================
        base64Data = request.POST.get('content', '')
        subfolder = time.strftime("%Y%m")
        MEDIA_ROOT = settings.MEDIA_ROOT[0] if isinstance(settings.MEDIA_ROOT , list) else settings.MEDIA_ROOT
        if not os.path.exists(MEDIA_ROOT + subfolder):
            os.makedirs(MEDIA_ROOT + subfolder)
        file_name = str(uuid.uuid1())
        path = str(subfolder + '/' + file_name + '.' + 'png')
        phisypath = MEDIA_ROOT + path
        f = open(phisypath, 'wb+')
        f.write(base64.decodestring(base64Data))
        f.close()
        response = HttpResponse()
        response.write("{'url':'%s',state:'%s'}" % ('/upload/' + subfolder + '/' + file_name + '.' + 'png', 'SUCCESS'))
        return response

def listdir(path, filelist):
    """ 递归 得到所有图片文件信息 """
    phisypath = settings.MEDIA_ROOT[0] if isinstance(settings.MEDIA_ROOT , list) else settings.MEDIA_ROOT
    if os.path.isfile(path):
        return '[]'
    allFiles = os.listdir(path)
    retlist = []
    for cfile in allFiles:
        fileinfo = {}
        filepath = (path + os.path.sep + cfile).replace("\\", "/").replace('//', '/')

        if os.path.isdir(filepath):
            listdir(filepath, filelist)
        else:
            if cfile.endswith('.gif') or cfile.endswith('.png') or cfile.endswith('.jpg') or cfile.endswith('.bmp'):
                filelist.append(filepath.replace(phisypath, '/upload/').replace("//", "/"))


@csrf_exempt
def ueditor_imageManager(request):
    """ 图片在线管理  """
    filelist = []
    phisypath = settings.MEDIA_ROOT[0] if isinstance(settings.MEDIA_ROOT , list) else settings.MEDIA_ROOT
    listdir(phisypath, filelist)
    imgStr = "ue_separate_ue".join(filelist)
    response = HttpResponse()
    response.write(imgStr)
    return response


@csrf_exempt
def ueditor_getMovie(request):
    """ 获取视频数据的地址 """
    content = ""
    searchkey = request.POST.get("searchKey")
    videotype = request.POST.get("videoType")
    try:
        url = "http://api.tudou.com/v3/gw?method=item.search&appKey=myKey&format=json&kw=" + searchkey + "&pageNo=1&pageSize=20&channelId=" + videotype + "&inDays=7&media=v&sort=s"
        content = urllib2.urlopen(url).read()
    except Exception, e:
        pass
    response = HttpResponse()
    response.write(content)
    return response


@csrf_exempt
def ueditor_getRemoteImage(request):
    print request
    """ 把远程的图抓到本地,爬图 """
    file_name = str(uuid.uuid1())
    subfolder = time.strftime("%Y%m")
    MEDIA_ROOT = settings.MEDIA_ROOT[0] if isinstance(settings.MEDIA_ROOT , list) else settings.MEDIA_ROOT
    if not os.path.exists(MEDIA_ROOT + subfolder):
        os.makedirs(MEDIA_ROOT + subfolder)
    #====get request params=================================
    urls = str(request.POST.get("upfile"))
    urllist = urls.split("ue_separate_ue")
    outlist = []
    #====request params end=================================
    fileType = [".gif" , ".png" , ".jpg" , ".jpeg" , ".bmp"]
    for url in urllist:
        fileExt = ""
        for suffix in fileType:
            if url.endswith(suffix):
                fileExt = suffix
                break
        if fileExt == '':
            continue
        else:
            path = str(subfolder + '/' + file_name + '.' + fileExt)
            phisypath = MEDIA_ROOT + path
            piccontent = urllib2.urlopen(url).read()
            picfile = open(phisypath, 'wb')
            picfile.write(piccontent)
            picfile.close()
            outlist.append('/upload/' + subfolder + '/' + file_name + '.' + fileExt)
    outlist = "ue_separate_ue".join(outlist)

    response = HttpResponse()
    myresponse = "{'url':'%s','tip':'%s','srcUrl':'%s'}" % (outlist, '成功', urls)
    response.write(myresponse)
    return response

def main(request):
    action = request.GET.get('action', None);
    result = '';
    return listDirOfSAEStorage('video');
    if action == 'config':
        return str(listDirOfSAEStorage());
        # return setToSAEStorage('config.txt',request.REQUEST,'txt');
        # result = getUeditorConfig1();
        # return HttpResponseRedirect('http://weixinofneo.sinaapp.com/err/');
    elif action == 'uploadimage':
        setToSAEStorage('imageupload.txt', request.REQUEST, 'txt');
        return HttpResponse(request.REQUEST);
    elif action == 'uploadscrawl':
        setToSAEStorage('cralupload.txt', request.REQUEST, 'txt');
        return HttpResponse(request.REQUEST);
    elif action == 'uploadvideo':
        return HttpResponse(request.REQUEST);
    elif action == 'uploadfile':
        setToSAEStorage('fileupload.txt', request.REQUEST, 'txt');
        return HttpResponse(request.REQUEST);
    elif action == 'listimage':
        return HttpResponse(request.REQUEST);
    elif action == 'catchimage':
        return HttpResponse(request.REQUEST);
    
    cb = request.GET.get('callback', None)
    if  cb != None:
        result = cb + '(' + result + ')';
    
    return HttpResponse(result, content_type="application/json"); 
	# return HttpResponse(result);

def LoadUeditor(request):
    # t = get_template('ueditor/deamon.html')
    # html = t.render()
    # return HttpResponse(t)
    return render_to_response('index.html')

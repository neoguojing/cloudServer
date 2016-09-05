import os
import shutil
from django.conf import settings

class NeoStorage(object):
    
    def __init__(self, rootdir=settings.MEDIA_ROOT):
        self.rootdir = rootdir
        self.fullpath = None
        self.url = settings.MEDIA_URL
        
    def _mkdir(self, filepath):
        self.fullpath = self.rootdir + filepath
        
    def _getfilename(self):
        index = self.fullpath.rfind('/')
        if index != -1:
            return self.fullpath[index+1:]
        else:
            return ''
    
    def _getfilepath(self):
        index = self.fullpath.rfind('/')
        if index != -1:
            return self.fullpath[0:index]
        else:
            return ''
        
    def saveB(self, filepath, data):
        self._mkdir(filepath)
        if not os.path.exists(self._getfilepath()):
            os.mkdir(self.fullpath)
        f = open (self.fullpath, 'wb' )
        f.write (data)
        f.close() 
        return self.url + filepath
    
    def save(self, filepath, data):
        self._mkdir(filepath)
        if not os.path.exists(self._getfilepath()):
            os.mkdir(self.fullpath)
        f = open (self.fullpath, 'w' )
        f.write (data)
        f.close() 
        return self.url + filepath
    
    def rmall(self, path):
        try:
            for file in os.listdir(path):
                    if os.path.isdir(file):
                        shutil.rmtree(file) 
                    else:
                        os.remove(file)
        except Exception as e:
            pass
            
                    
    
    def delete(self,filepath):
        self._mkdir(filepath)
        if os.path.isdir(self.fullpath):
            self.rmall(self.fullpath)
        else:
            os.remove(self.fullpath)
    
    def saveUploadFile(self, app,filename, fileobject):
        try:
            path = self.rootdir+"/" + app+"/"
            if not os.path.exists(path):
                os.makedirs(path)
            file_name = path + filename
            destination = open(file_name, 'wb+')
            for chunk in fileobject.chunks():
                destination.write(chunk)
            destination.close() 
        except Exception, e:
            print e
    
        return file_name
    
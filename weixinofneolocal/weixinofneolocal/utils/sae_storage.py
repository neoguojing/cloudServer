# -*- coding: utf-8 -*-
# coding=utf-8
import os
from django.conf import settings
if settings.ENV == 'SAE':
    from sae.ext.storage import monkey
    from sae.storage import Bucket
    
    def __method_get_filename(fullname):
        filename = os.path.basename(fullname);
        return filename;
    
    def __method_get_namelist(fullname):
        if fullname != '':
            filename = __method_get_filename(fullname);
            m_list = filename.split('.');
            if len(m_list) <= 1:
                return None;
            return m_list;
        return None
    
    def getFromSAEStorage(filename):
        monkey.patch_all();
        bucket = Bucket('media');
        bucket.put();
        bucket.post(acl='.r:.sinaapp.com,.r:sae.sina.com.cn,.r:.vipsinaapp.com,.r:.qq.com,.r:.wx.qq.com', metadata={'expires': '7d'});
        
        filetype = __method_get_namelist(filename)[1];
        if filetype.lower() in ('jpg', 'jpeg', 'bmp', 'gif', 'png'):
            filepath = 'image/' + filename;
        elif filetype.lower() in ("swf", "wmv"):
            filepath = 'video/' + filename;
        elif filetype.lower() in ("wma", "mp3"):
            filepath = 'music/' + filename;
        else:
            filepath = filename;
        return bucket.generate_url(filepath);
        
    
    
    def setToSAEStorage(filename, data):
        monkey.patch_all();
        bucket = Bucket('media');
        bucket.put();
        bucket.post(acl='.r:.sinaapp.com,.r:sae.sina.com.cn,.r:.vipsinaapp.com,.r:.qq.com,.r:.wx.qq.com', metadata={'expires': '7d'});
        tmp = __method_get_namelist(filename)
        if tmp == None:
            return None;
        filetype = tmp[1];
        
        if filetype.lower() in ('jpg', 'jpeg', 'bmp', 'gif', 'png'):
            filepath = 'image/' + filename;
        elif filetype.lower() in ("swf", "wmv"):
            filepath = 'video/' + filename;
        elif filetype.lower() in ("wma", "mp3"):
            filepath = 'music/' + filename;
        else:
            filepath = filename;
        bucket.put_object(filepath, data);
        return bucket.generate_url(filepath);
    
    def delThenSetToSAEStorage(filename, data):
        monkey.patch_all();
        bucket = Bucket('media');
        bucket.put();
        bucket.post(acl='.r:.sinaapp.com,.r:sae.sina.com.cn,.r:.vipsinaapp.com,.r:.qq.com,.r:.wx.qq.com', metadata={'expires': '7d'});
        tmp = __method_get_namelist(filename)
        if tmp == None:
            return None;
        filetype = tmp[1];
        
        if filetype.lower() in ('jpg', 'jpeg', 'bmp', 'gif', 'png'):
            filepath = 'image/' + filename;
        elif filetype.lower() in ("swf", "wmv"):
            filepath = 'video/' + filename;
        elif filetype.lower() in ("wma", "mp3"):
            filepath = 'music/' + filename;
        else:
            filepath = filename;
            
        try:
        	bucket.delete_object(filepath);
        except Exception:
            pass
            
        bucket.put_object(filepath, data);
        return bucket.generate_url(filepath);
    
    def delObjectInSaeStorage(filename):
        monkey.patch_all();
        bucket = Bucket('media');
        bucket.put();
        bucket.post(acl='.r:.sinaapp.com,.r:sae.sina.com.cn,.r:.vipsinaapp.com,.r:.qq.com,.r:.wx.qq.com', metadata={'expires': '7d'});
        tmp = __method_get_namelist(filename)
        if tmp == None:
            return None;
        filetype = tmp[1];
        
        if filetype.lower() in ('jpg', 'jpeg', 'bmp', 'gif', 'png'):
            filepath = 'image/' + filename;
        elif filetype.lower() in ("swf", "wmv"):
            filepath = 'video/' + filename;
        elif filetype.lower() in ("wma", "mp3"):
            filepath = 'music/' + filename;
        else:
            filepath = filename;
            
        bucket.delete_object(filepath);
        return;
    
    # 返回所有文件的所有属性
    def listDirOfSAEStorage(path=''):
        monkey.patch_all();
        bucket = Bucket('media');
        bucket.put();
        bucket.post(acl='.r:.sinaapp.com,.r:sae.sina.com.cn,.r:.vipsinaapp.com,.r:.qq.com,.r:.wx.qq.com', metadata={'expires': '7d'});
        
        if not path.endswith('/'):
            if path == '':
                pass;
            else:
                path = path + '/';
                
        return [i for i in bucket.list(path)];
    

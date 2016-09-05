# coding=utf-8

def getUeditorConfig(image_path='http://weixinofneo-media.stor.sinaapp.com/image/', video_path='http://weixinofneo-media.stor.sinaapp.com/video/', file_path='http://weixinofneo-media.stor.sinaapp.com/'):
    ued_config = {
        "imageActionName": "uploadimage",
        "imageFieldName": "upfile",
        "imageMaxSize": 2048000,
        "imageAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
        "imageCompressEnable": True,
        "imageCompressBorder": 1600,
        "imageInsertAlign": "none",
        "imageUrlPrefix": image_path,
        "imagePathFormat": image_path + "{yyyy}{mm}{dd}/{time}_{filename}",
        "scrawlActionName": "uploadscrawl",
        "scrawlFieldName": "upfile",
        "scrawlPathFormat": "{yyyy}{mm}{dd}/{time}{rand:6}",
        "scrawlMaxSize": 2048000,
        "scrawlUrlPrefix": image_path,
        "scrawlInsertAlign": "none",
        "snapscreenActionName": "uploadimage",
        "snapscreenPathFormat": "{yyyy}{mm}{dd}/{time}{rand:6}",
        "snapscreenUrlPrefix": image_path,
        "snapscreenInsertAlign": "none",
        "catcherLocalDomain": ["127.0.0.1", "localhost", "img.baidu.com"],
        "catcherActionName": "catchimage",
        "catcherFieldName": "source",
        "catcherPathFormat": "{yyyy}{mm}{dd}/{time}{rand:6}",
        "catcherUrlPrefix": image_path,
        "catcherMaxSize": 2048000,
        "catcherAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
        "videoActionName": "uploadvideo",
        "videoFieldName": "upfile",
        "videoPathFormat": "{yyyy}{mm}{dd}/{time}{rand:6}",
        "videoUrlPrefix": video_path,
        "videoMaxSize": 102400000,
        "videoAllowFiles": [
            ".flv", ".swf", ".mkv", ".avi", ".rm", ".rmvb", ".mpeg", ".mpg",
            ".ogg", ".ogv", ".mov", ".wmv", ".mp4", ".webm", ".mp3", ".wav", ".mid"],
        "fileActionName": "uploadfile",
        "fileFieldName": "upfile",
        "filePathFormat": "{yyyy}{mm}{dd}/{time}{rand:6}",
        "fileUrlPrefix": file_path,
        "fileMaxSize": 51200000,
        "fileAllowFiles": [
            ".png", ".jpg", ".jpeg", ".gif", ".bmp",
            ".flv", ".swf", ".mkv", ".avi", ".rm", ".rmvb", ".mpeg", ".mpg",
            ".ogg", ".ogv", ".mov", ".wmv", ".mp4", ".webm", ".mp3", ".wav", ".mid",
            ".rar", ".zip", ".tar", ".gz", ".7z", ".bz2", ".cab", ".iso",
            ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".txt", ".md", ".xml"
        ],
        "imageManagerActionName": "listimage",
        "imageManagerListPath": "image/",
        "imageManagerListSize": 20,
        "imageManagerUrlPrefix":image_path,
        "imageManagerInsertAlign": "none",
        "imageManagerAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
        "fileManagerActionName": "listfile",
        "fileManagerListPath": "",
        "fileManagerUrlPrefix": file_path,
        "fileManagerListSize": 20,
        "fileManagerAllowFiles": [
            ".png", ".jpg", ".jpeg", ".gif", ".bmp",
            ".flv", ".swf", ".mkv", ".avi", ".rm", ".rmvb", ".mpeg", ".mpg",
            ".ogg", ".ogv", ".mov", ".wmv", ".mp4", ".webm", ".mp3", ".wav", ".mid",
            ".rar", ".zip", ".tar", ".gz", ".7z", ".bz2", ".cab", ".iso",
            ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".txt", ".md", ".xml"
        ] 
    }
    
    return ued_config;

def getUeditorConfig1(image_path='http://weixinofneo-media.stor.sinaapp.com/image/', video_path='http://weixinofneo-media.stor.sinaapp.com/video/', file_path='http://weixinofneo-media.stor.sinaapp.com/'):
    ued_config = u'''{
        "imageActionName": "uploadimage",
        "imageFieldName": "upfile",
        "imageMaxSize": 2048000,
        "imageAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
        "imageCompressEnable": True,
        "imageCompressBorder": 1600,
        "imageInsertAlign": "none",
        "imageUrlPrefix": "%s",
        "imagePathFormat": "%s"+"{yyyy}{mm}{dd}/{time}_{filename}",
        "scrawlActionName": "uploadscrawl",
        "scrawlFieldName": "upfile",
        "scrawlPathFormat": "{yyyy}{mm}{dd}/{time}{rand:6}",
        "scrawlMaxSize": 2048000,
        "scrawlUrlPrefix": "%s",
        "scrawlInsertAlign": "none",
        "snapscreenActionName": "uploadimage",
        "snapscreenPathFormat": "{yyyy}{mm}{dd}/{time}{rand:6}",
        "snapscreenUrlPrefix": "%s",
        "snapscreenInsertAlign": "none",
        "catcherLocalDomain": ["127.0.0.1", "localhost", "img.baidu.com"],
        "catcherActionName": "catchimage",
        "catcherFieldName": "source",
        "catcherPathFormat": "{yyyy}{mm}{dd}/{time}{rand:6}",
        "catcherUrlPrefix": "%s",
        "catcherMaxSize": 2048000,
        "catcherAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
        "videoActionName": "uploadvideo",
        "videoFieldName": "upfile",
        "videoPathFormat": "{yyyy}{mm}{dd}/{time}{rand:6}",
        "videoUrlPrefix": "%s",
        "videoMaxSize": 102400000,
        "videoAllowFiles": [
            ".flv", ".swf", ".mkv", ".avi", ".rm", ".rmvb", ".mpeg", ".mpg",
            ".ogg", ".ogv", ".mov", ".wmv", ".mp4", ".webm", ".mp3", ".wav", ".mid"],
        "fileActionName": "uploadfile",
        "fileFieldName": "upfile",
        "filePathFormat": "{yyyy}{mm}{dd}/{time}{rand:6}",
        "fileUrlPrefix": "%s",
        "fileMaxSize": 51200000,
        "fileAllowFiles": [
            ".png", ".jpg", ".jpeg", ".gif", ".bmp",
            ".flv", ".swf", ".mkv", ".avi", ".rm", ".rmvb", ".mpeg", ".mpg",
            ".ogg", ".ogv", ".mov", ".wmv", ".mp4", ".webm", ".mp3", ".wav", ".mid",
            ".rar", ".zip", ".tar", ".gz", ".7z", ".bz2", ".cab", ".iso",
            ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".txt", ".md", ".xml"
        ],
        "imageManagerActionName": "listimage",
        "imageManagerListPath": "image/",
        "imageManagerListSize": 20,
        "imageManagerUrlPrefix":"%s",
        "imageManagerInsertAlign": "none",
        "imageManagerAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
        "fileManagerActionName": "listfile",
        "fileManagerListPath": "",
        "fileManagerUrlPrefix": "%s",
        "fileManagerListSize": 20,
        "fileManagerAllowFiles": [
            ".png", ".jpg", ".jpeg", ".gif", ".bmp",
            ".flv", ".swf", ".mkv", ".avi", ".rm", ".rmvb", ".mpeg", ".mpg",
            ".ogg", ".ogv", ".mov", ".wmv", ".mp4", ".webm", ".mp3", ".wav", ".mid",
            ".rar", ".zip", ".tar", ".gz", ".7z", ".bz2", ".cab", ".iso",
            ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".txt", ".md", ".xml"
        ] 
    }''' % (image_path, image_path, image_path, image_path, image_path, video_path, file_path, image_path, file_path)
    
    return ued_config;
'''
{
        ##/* 上传图片配置项 */
        "imageActionName": "uploadimage", ##/* 执行上传图片的action名称 */
        "imageFieldName": "upfile", ##/* 提交的图片表单名称 */
        "imageMaxSize": 2048000, ##/* 上传大小限制，单位B */
        "imageAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"], ##/* 上传图片格式显示 */
        "imageCompressEnable": True, ##/* 是否压缩图片,默认是true */
        "imageCompressBorder": 1600, ##/* 图片压缩最长边限制 */
        "imageInsertAlign": "none", ##/* 插入的图片浮动方式 */
        "imageUrlPrefix": image_path, ##/* 图片访问路径前缀 */
        "imagePathFormat": "{filename}{yyyy}{mm}{dd}/{time}{rand:6}", ##/* 上传保存路径,可以自定义保存路径和文件名格式 */
                                    ##/* {filename} 会替换成原文件名,配置这项需要注意中文乱码问题 */
                                    #/* {rand:6} 会替换成随机数,后面的数字是随机数的位数 */
                                    #/* {time} 会替换成时间戳 */
                                    #/* {yyyy} 会替换成四位年份 */
                                    #/* {yy} 会替换成两位年份 */
                                    #/* {mm} 会替换成两位月份 */
                                    #/* {dd} 会替换成两位日期 */
                                    #/* {hh} 会替换成两位小时 */
                                    #/* {ii} 会替换成两位分钟 */
                                    #/* {ss} 会替换成两位秒 */
                                    #/* 非法字符 \ : * ? " < > | */
                                    #/* 具请体看线上文档: fex.baidu.com/ueditor/#use-format_upload_filename */
    
        #/* 涂鸦图片上传配置项 */
        "scrawlActionName": "uploadscrawl", #/* 执行上传涂鸦的action名称 */
        "scrawlFieldName": "upfile", #/* 提交的图片表单名称 */
        "scrawlPathFormat": "{yyyy}{mm}{dd}/{time}{rand:6}", #/* 上传保存路径,可以自定义保存路径和文件名格式 */
        "scrawlMaxSize": 2048000, #/* 上传大小限制，单位B */
        "scrawlUrlPrefix": image_path, #/* 图片访问路径前缀 */
        "scrawlInsertAlign": "none",
    
        #/* 截图工具上传 */
        "snapscreenActionName": "uploadimage", #/* 执行上传截图的action名称 */
        "snapscreenPathFormat": "{yyyy}{mm}{dd}/{time}{rand:6}", #/* 上传保存路径,可以自定义保存路径和文件名格式 */
        "snapscreenUrlPrefix": image_path, #/* 图片访问路径前缀 */
        "snapscreenInsertAlign": "none", #/* 插入的图片浮动方式 */
    
        #/* 抓取远程图片配置 */
        "catcherLocalDomain": ["127.0.0.1", "localhost", "img.baidu.com"],
        "catcherActionName": "catchimage", #/* 执行抓取远程图片的action名称 */
        "catcherFieldName": "source", #/* 提交的图片列表表单名称 */
        "catcherPathFormat": "{yyyy}{mm}{dd}/{time}{rand:6}", #/* 上传保存路径,可以自定义保存路径和文件名格式 */
        "catcherUrlPrefix": image_path, #/* 图片访问路径前缀 */
        "catcherMaxSize": 2048000, #/* 上传大小限制，单位B */
        "catcherAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"], #/* 抓取图片格式显示 */
    
        #/* 上传视频配置 */
        "videoActionName": "uploadvideo", #/* 执行上传视频的action名称 */
        "videoFieldName": "upfile", #/* 提交的视频表单名称 */
        "videoPathFormat": "{yyyy}{mm}{dd}/{time}{rand:6}", #/* 上传保存路径,可以自定义保存路径和文件名格式 */
        "videoUrlPrefix": video_path, #/* 视频访问路径前缀 */
        "videoMaxSize": 102400000, #/* 上传大小限制，单位B，默认100MB */
        "videoAllowFiles": [
            ".flv", ".swf", ".mkv", ".avi", ".rm", ".rmvb", ".mpeg", ".mpg",
            ".ogg", ".ogv", ".mov", ".wmv", ".mp4", ".webm", ".mp3", ".wav", ".mid"], #/* 上传视频格式显示 */
    
        #/* 上传文件配置 */
        "fileActionName": "uploadfile", #/* controller里,执行上传视频的action名称 */
        "fileFieldName": "upfile", #/* 提交的文件表单名称 */
        "filePathFormat": "{yyyy}{mm}{dd}/{time}{rand:6}", #/* 上传保存路径,可以自定义保存路径和文件名格式 */
        "fileUrlPrefix": file_path, #/* 文件访问路径前缀 */
        "fileMaxSize": 51200000, #/* 上传大小限制，单位B，默认50MB */
        "fileAllowFiles": [
            ".png", ".jpg", ".jpeg", ".gif", ".bmp",
            ".flv", ".swf", ".mkv", ".avi", ".rm", ".rmvb", ".mpeg", ".mpg",
            ".ogg", ".ogv", ".mov", ".wmv", ".mp4", ".webm", ".mp3", ".wav", ".mid",
            ".rar", ".zip", ".tar", ".gz", ".7z", ".bz2", ".cab", ".iso",
            ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".txt", ".md", ".xml"
        ], #/* 上传文件格式显示 */
    
        #/* 列出指定目录下的图片 */
        "imageManagerActionName": "listimage", #/* 执行图片管理的action名称 */
        "imageManagerListPath": "image/", #/* 指定要列出图片的目录 */
        "imageManagerListSize": 20, #/* 每次列出文件数量 */
        "imageManagerUrlPrefix":image_path, #/* 图片访问路径前缀 */
        "imageManagerInsertAlign": "none", #/* 插入的图片浮动方式 */
        "imageManagerAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"], #/* 列出的文件类型 */
    
        #/* 列出指定目录下的文件 */
        "fileManagerActionName": "listfile", #/* 执行文件管理的action名称 */
        "fileManagerListPath": "", #/* 指定要列出文件的目录 */
        "fileManagerUrlPrefix": file_path, #/* 文件访问路径前缀 */
        "fileManagerListSize": 20, #/* 每次列出文件数量 */
        "fileManagerAllowFiles": [
            ".png", ".jpg", ".jpeg", ".gif", ".bmp",
            ".flv", ".swf", ".mkv", ".avi", ".rm", ".rmvb", ".mpeg", ".mpg",
            ".ogg", ".ogv", ".mov", ".wmv", ".mp4", ".webm", ".mp3", ".wav", ".mid",
            ".rar", ".zip", ".tar", ".gz", ".7z", ".bz2", ".cab", ".iso",
            ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".txt", ".md", ".xml"
        ] #/* 列出的文件类型 */
    
    }
'''

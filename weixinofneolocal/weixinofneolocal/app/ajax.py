from djangocaptcha.fields import ReCaptchaField 
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def calcuteVertifyCode(request):
    rcf = ReCaptchaField(request);
    code = rcf.display();
    origcode = rcf.getCode();
    data = u'''{"pic":"%s","code":"%s"}''' % (code, origcode);
    # code = rcf.displayAsPic();
    response = HttpResponse(); 
    response['Content-Type'] = "application/json"  
    response.write(data)  
    return response

@csrf_exempt
def calcuteVertifyCode1(request):
    rcf = ReCaptchaField(request);
    return rcf.displayAsPic();

@csrf_exempt
def multiply1(request):
    response = HttpResponse()  
    response['Content-Type'] = "text/javascript"  
    a = request.POST.get("a", '')  
    b = request.POST.get("b", '')  
    ret = int(a) * int(b)
    response.write(ret)  
    return response

class VertifyCode:
    def __init__(self, request):
        self.rcf = ReCaptchaField(request);
    
    def getVertiCode(self):
        return self.rcf.getCode();
    
    def getHttpPic(self):
        return self.rcf.displayAsPic();
    
    
    

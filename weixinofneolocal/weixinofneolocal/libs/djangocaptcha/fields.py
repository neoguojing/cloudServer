# -*- coding: utf-8 -*-
# coding=utf-8
from django.conf import settings
from django import forms
from django.utils.encoding import smart_unicode
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from .verticode import Captcha
import random
    
class ReCaptcha(forms.widgets.Widget):
    # recaptcha_challenge_name = 'recaptcha_challenge_field'
    recaptcha_response_name = 'recaptcha_response_field'
    ca = None
    
    def __init__(self, capobj, attrs=None):
        self.ca = capobj
        super(ReCaptcha, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        return mark_safe(u'%s' % self.displayhtml(self.ca.save()))

    def value_from_datadict(self, data, files, name):
        return [data.get(self.recaptcha_response_name, None)] 
    
    def displayhtml (self, capurl):

        return u"""<img src="%s" width="145" height="30" alt="CAPTCHA" border="1" onclick= this.src="%s" style="cursor: pointer;" title="看不清？点击更换另一个验证码" />
        <input type='text' name='recaptcha_response_field' value='manual_challenge' />""" % (capurl, capurl)
        
    def __displayhtml (self, capurl):

        return u"""<iframe src="%s" height="300" width="500" frameborder="0"></iframe><br />
        <input type='hidden' name='recaptcha_response_field' value='manual_challenge' />""" % capurl
        
class ReCaptchaField(forms.CharField):
    default_error_messages = {
        'captcha_invalid': _(u'Invalid captcha')
    }	
    figures = [2, 3, 4, 5, 6, 7, 8, 9]
    ca = None

    def __init__(self, request, *args, **kwargs):
        self.ca = Captcha(request)
        self.ca.words = [''.join([str(random.sample(self.figures, 1)[0]) for i in range(0, 4)])]
        self.ca.type = 'word'
        self.ca.img_width = 100
        self.ca.img_height = 30
        # self.ca.save()
        self.widget = ReCaptcha(self.ca)
        self.required = True
        self.__request = request
        super(ReCaptchaField, self).__init__(*args, **kwargs)
	
    def display(self):
        return self.ca.save()
    
    def displayAsPic(self):
        return self.ca.display()
        
    def check(self):
        code = self.__request.POST.get('recaptcha', '')
        if not code:
            return False
        
        if self.ca.check(code):
            return True
        else:
            return False
        
    def checkCode(self, code):
        if not code:
            return False
        
        if self.ca.check(code):
            return True
        else:
            return False
    
    def getCode(self):
        return self.ca.getCode();
 
        

    def clean(self, values):
        super(ReCaptchaField, self).clean(values[0])
        recaptcha_response_value = smart_unicode(values[0])

        if not self.ca.check(recaptcha_response_value):
            raise forms.util.ValidationError(self.error_messages['captcha_invalid'])
        return values[0] 




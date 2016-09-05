# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import app 
admin.autodiscover() 

urlpatterns = patterns('',
    # Examples:

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	
    # admin
    url(r'^admin/', include(admin.site.urls)),
    # Uncomment the next line to enable the admin:
    # test urls
    url(r'^weixin/$', 'interface.views.weixin_main'),
    url(r'^code/', 'app.views.weixin_main'),
    url(r'^test/', 'app.views.test'),
    # url(r'^editor/', 'utils.ueditor.views.main'),
    # url(r'^loadeditor/', 'utils.ueditor.views.LoadUeditor'),
    # common tools
	
    # weixin urls
    url(r'^app/', include('app.urls')),
    url(r'^myweixin/', 'app.views.weixin_main'),
    
    url(r'^editor13/', include('utils.ueditor13.urls')),
    url(r'^loadeditor13/', 'utils.ueditor13.views.LoadUeditor'),

    url(r'^err/', 'utils.debug.views.displayErr'),
    # blog
    # url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^xmlrpc/$', 'utils.xmlrpc.views.handle_xmlrpc'),
    url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include('django_comments.urls')),
    # satchmo
    # url(r'^store/', include('satchmo.urls')),
    # forum
    url(r'^neoforum/', include('forumapp.urls')),
    # renovation
    # url(r'^renovation/', include('renovation.urls')),
    #android
    url(r'^android/', include('android.urls')),
    
)

# blog
'''
from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap

sitemaps = {'tags': TagSitemap,
            'blog': EntrySitemap,
            'authors': AuthorSitemap,
            'categories': CategorySitemap,}

urlpatterns += patterns(
    'django.contrib.sitemaps.views',
    url(r'^sitemap.xml$', 'index',
        {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap',
        {'sitemaps': sitemaps}),)
'''
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT) 

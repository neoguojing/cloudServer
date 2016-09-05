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
    url(r'^site1/admin/', include(admin.site.urls)),
    # Uncomment the next line to enable the admin:
    # test urls
    url(r'^site1/weixin/$', 'interface.views.weixin_main'),
    url(r'^site1/code/', 'app.views.weixin_main'),
    url(r'^site1/test/', 'app.views.test'),
    # url(r'^editor/', 'utils.ueditor.views.main'),
    # url(r'^loadeditor/', 'utils.ueditor.views.LoadUeditor'),
    # common tools
    
    # weixin urls
    url(r'^site1/app/', include('app.urls')),
    url(r'^site1/myweixin/', 'app.views.weixin_main'),
    
    url(r'^site1/editor13/', include('utils.ueditor13.urls')),
    url(r'^site1/loadeditor13/', 'utils.ueditor13.views.LoadUeditor'),

    url(r'^site1/err/', 'utils.debug.views.displayErr'),
    # blog
    # url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^site1/xmlrpc/$', 'utils.xmlrpc.views.handle_xmlrpc'),
    url(r'^site1/weblog/', include('zinnia.urls')),
    url(r'^site1/comments/', include('django_comments.urls')),
    # satchmo
    # url(r'^store/', include('satchmo.urls')),
    # forum
    url(r'^site1/neoforum/', include('forumapp.urls')),
    # renovation
    # url(r'^renovation/', include('renovation.urls')),
    
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

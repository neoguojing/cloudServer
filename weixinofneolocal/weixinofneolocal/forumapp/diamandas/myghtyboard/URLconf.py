import django
if django.VERSION < (1, 6):
    from django.conf.urls.defaults import *
else:
    from django.conf.urls import *
    
# Myghtyboard URLs
urlpatterns = patterns('forumapp.diamandas.myghtyboard.views',
    url(r'^$', 'category_list'),
    url(r'^forum/(?P<forum_id>[0-9]+)/$', 'topic_list'),
    url(r'^forum/(?P<forum_id>[0-9]+)/(?P<pagination_id>[0-9]+)/$', 'topic_list'),
    url(r'^topic/(?P<pagination_id>[0-9]+)/(?P<topic_id>[0-9]+)/$', 'post_list'),
    url(r'^mytopics/(?P<show_user>.*)/$', 'my_topic_list'),
    url(r'^mytopics/$', 'my_topic_list'),
    url(r'^lasttopics/$', 'last_topic_list'),
    url(r'^myptopics/(?P<show_user>.*)/$', 'my_posttopic_list'),
    url(r'^myptopics/$', 'my_posttopic_list'),
)

urlpatterns += patterns('forumapp.diamandas.myghtyboard.views_add_edit',
    url(r'^add_topic/(?P<forum_id>[0-9]+)/$', 'add_topic'),
    url(r'^add_post/(?P<topic_id>[0-9]+)/(?P<post_id>[0-9]+)/$', 'add_post'),  # add post with quote
    url(r'^add_post/(?P<topic_id>[0-9]+)/$', 'add_post'),
    url(r'^edit_post/(?P<post_id>[0-9]+)/$', 'edit_post'),
)

urlpatterns += patterns('forumapp.diamandas.myghtyboard.views_actions',
    url(r'^delete_post/(?P<post_id>[0-9]+)/(?P<topic_id>[0-9]+)/$', 'delete_post'),
    url(r'^move_topic/(?P<topic_id>[0-9]+)/(?P<forum_id>[0-9]+)/$', 'move_topic'),
    url(r'^delete_topic/(?P<topic_id>[0-9]+)/(?P<forum_id>[0-9]+)/$', 'delete_topic'),
    url(r'^close_topic/(?P<topic_id>[0-9]+)/(?P<forum_id>[0-9]+)/$', 'close_topic'),
    url(r'^open_topic/(?P<topic_id>[0-9]+)/(?P<forum_id>[0-9]+)/$', 'open_topic'),
    url(r'^topic/solve/(?P<topic_id>[0-9]+)/(?P<forum_id>[0-9]+)/$', 'solve_topic'),
    url(r'^topic/unsolve/(?P<topic_id>[0-9]+)/(?P<forum_id>[0-9]+)/$', 'unsolve_topic'),
)

#!/usr/bin/python
# Diamanda Application Set
# myghtyboard forum
# coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.utils.translation import ugettext as _
# from django.views.generic.list_detail import object_list
from django.views.generic.list import ListView
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage

from forumapp.diamandas.myghtyboard.models import *
from forumapp.diamandas.myghtyboard.context import forum as forumContext
from forumapp.diamandas.myghtyboard.forms import *

# neo
from djangocaptcha.fields import ReCaptchaField 

def category_list(request):
	"""
	show all categories and their topics
	"""
	categories = Category.objects.all().order_by('order')
	for c in categories:
		# {% if forum.mods %}<u>{% trans "Moderators" %}</u>:
		#        {% for i in forum.mods %}
		#               {{ i.username }}{% if not forloop.last %},{% endif %} 
		#        {% endfor %}
		# {% endif %}
		# forum = c.forum_set.all().order_by('order')
		# forums = []
		# for f in forum:
		# 	f.mods = f.moderators.all()
		# 	forums.append(f)
		c.forums = c.forum_set.all().order_by('order')
	return render_to_response(
		'myghtyboard/category_list.html',
		{'categories': categories},
		context_instance=RequestContext(request, processors=[forumContext]))


def topic_list(request, forum_id, pagination_id=1):
    # neo
    reCaptchaFieldOfTopic = ReCaptchaField(request);
    
    prefixes = False
    prefixes_list = False
    if request.POST:
        prefixes = request.POST.copy()
        prefixes = prefixes.getlist("prefix[]")
        prefixes = Prefix.objects.filter(id__in=prefixes)
    
    try:
        if prefixes and len(prefixes) > 0:
            tops = TopicPrefix.objects.all().values('topic').distinct()
            for i in prefixes:
                tops = tops.filter(prefix=i)
            topics_ids = []
            for tid in tops:
                topics_ids.append(tid['topic'])
            topics = Topic.objects.order_by('-is_global', '-is_sticky', '-modification_date').filter(Q(forum=forum_id) | Q(is_global='1'))
            topics = topics.filter(id__in=topics_ids)
        else:
            topics = Topic.objects.order_by('-is_global', '-is_sticky', '-modification_date').filter(Q(forum=forum_id) | Q(is_global='1'))
        count = topics.count()
        count = count / 10
        cnt = [1]
        i = 1
        while i <= count:
            i = i + 1
            cnt.append(i)
        forum = Forum.objects.get(id=forum_id)
        name = forum.name
    except:
        return redirect_by_template(request, reverse('forumapp.diamandas.myghtyboard.views.category_list', kwargs={}), _('There is no such forum. Please go back to the forum list.'))
    
    if request.user.is_authenticated():
        chck = Post.objects.filter(author_system=request.user).count()
    else:
        chck = 0
    
    if chck < 5:
        form = AddTopicWithCaptchaForm()
    else:
        form = AddTopicForm()
    
    pr = False
    if forum.use_prefixes:
        p = Prefix.objects.filter(forums=forum)
        if len(p) > 0:
            pr = []
            for i in p:
                pr.append(i)
    request.forum_id = forum_id
    # deal pagenator
    paginator = Paginator(topics, 10)
    try:
        topicspage = paginator.page(pagination_id)
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        topicspage = paginator.page(paginator.num_pages)
    
    previous = int(pagination_id) - 1;
    if previous < 1:
        previous = 1;
    nextpage = topicspage.next_page_number;
    if nextpage > paginator.num_pages:
        nextpage = paginator.num_pages;
    
    return render_to_response(
		'myghtyboard/topics_list.html',
		{'object_list': topicspage,
             'forum': forum,
             'form': form,
             'current_user': unicode(request.user),
             'pr': pr, 'prefixes': prefixes,
             'cnt': cnt, 'pages':len(cnt),
             'page':pagination_id,
             'prew':previous,
             'next':nextpage,
             'captcha': reCaptchaFieldOfTopic.display(),
             'verticode':reCaptchaFieldOfTopic.getCode(),
             },
		context_instance=RequestContext(request, processors=[forumContext]))

@login_required
def my_topic_list(request, show_user=False):
	"""
	list my topics
	
	* show_user - if not set will show current user topics
	"""
	if not show_user:
		show_user = unicode(request.user)
	topics = Topic.objects.order_by('-modification_date').filter(author=show_user)[:50]
	name = _('User Topics')
	return render_to_response(
		'myghtyboard/mytopics_list.html',
		{'topics': topics, 'name': name},
		context_instance=RequestContext(request, processors=[forumContext]))

@login_required
def last_topic_list(request):
	"""
	 list last active topics
	"""
	topics = Topic.objects.order_by('-modification_date')[:50]
	for i in topics:
		pmax = i.post_set.all().count() / 10
		pmaxten = i.post_set.all().count() % 10
		if pmaxten != 0:
			i.pagination_max = pmax + 1
		else:
			i.pagination_max = pmax
	name = _('Last Active Topics')
	return render_to_response(
		'myghtyboard/mytopics_list.html',
		{'topics': topics, 'name': name},
		context_instance=RequestContext(request, processors=[forumContext]))

@login_required
def my_posttopic_list(request, show_user=False):
	"""
	list topics with my posts
	
	* show_user - if not set will show current user topics
	"""
	if not show_user:
		show_user = unicode(request.user)
	try:
		topics = Post.objects.order_by('-date').filter(author=show_user).values('topic').distinct()[:50]
		posts = []
		for i in topics:
			posts.append(int(i['topic']))
		topics = Topic.objects.order_by('-modification_date').filter(id__in=posts)
		for i in topics:
			pmax = i.post_set.all().count() / 10
			pmaxten = i.post_set.all().count() % 10
			if pmaxten != 0:
				i.pagination_max = pmax + 1
			else:
				i.pagination_max = pmax
		name = _('User Posts in Latest Topics')
	except:
		return render_to_response('myghtyboard/mytopics_list.html', {}, context_instance=RequestContext(request, forumContext(request)))
	return render_to_response(
		'myghtyboard/mytopics_list.html',
		{'topics': topics, 'name': name},
		context_instance=RequestContext(request, processors=[forumContext]))


def post_list(request, topic_id, pagination_id):
    # neo
    reCaptchaFieldOfPost = ReCaptchaField(request)
    
    itemperpage = 10;
    try:
        topic = Topic.objects.get(id=topic_id)
    except Topic.DoesNotExist:
        return HttpResponseRedirect(reverse('forumapp.diamandas.myghtyboard.views.category_list', kwargs={}))
    if  topic.is_locked:
        opened = False
    else:
        opened = True
	
    if topic.author_anonymous == False:
        try:
            topic.author_system
        except:
            topic.author_anonymous = True
            topic.author_system = None
            topic.save()
            
    if topic.author_anonymous == False and request.user == topic.author_system:
        is_author = True
    else:
        is_author = False
    forum = topic.forum
    request.forum_id = forum.id
    # form = AddPostForm()
    form = AddPostWithCaptchaForm()
    allposts = topic.post_set.all().order_by('date')
    
    count = allposts.count()
    count = count / itemperpage
    cnt = [1]
    i = 1
    while i <= count:
        i = i + 1
        cnt.append(i)
        
    # deal pagenator
 	    
    paginator = Paginator(allposts, itemperpage)
    try:
        posts = paginator.page(pagination_id)
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        posts = paginator.page(paginator.num_pages)
    
    previous = int(pagination_id) - 1;
    if previous < 1:
        previous = 1;
    nextpage = posts.next_page_number;
    if nextpage > paginator.num_pages:
        nextpage = paginator.num_pages;
    
        
    return render_to_response(
		'myghtyboard/post_list.html',
		{
            'object_list': posts,
			'opened': opened,
			'is_author': is_author,
			'topic': topic,
			'cnt': cnt,
			'forum_id': forum.id,
			'form': form,
			'forum_name': forum,
			'current_user': unicode(request.user),
            'page':pagination_id,
            'pages':len(cnt),
            'prew':previous,
            'next':nextpage,
            'captcha': reCaptchaFieldOfPost.display(),
            # 'captcha': reCaptchaFieldOfPost.displayAsPic(),
            'verticode':reCaptchaFieldOfPost.getCode(),
            },
		context_instance=RequestContext(request, processors=[forumContext]))


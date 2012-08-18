# Create your views here.
from django.shortcuts import render_to_response
from slbilling.billing.models import *
from django.http import HttpResponseRedirect

def list(request, archive=1):
	#http://billing.silverlining.com/ and http://billing.silverlining.com/archives/number/
	if archive < "1":
		return HttpResponseRedirect("/")
	archiveNo = (int(archive))
	page = (archiveNo*7)
	if Post.objects.all().count() > (page + 7)
		posts=Post.objects.order_by('-published')[page-7:page]
	else
		posts=Post.objects.order_by('-published')[]page-7:]
	#next and previous archive
	if Posts.objects.all().count()>page
		next = archiveNo + 1
	else
		next =0 
    previous = archiveNo - 1		
	return render_to_response('base.html',{'posts':posts,
										   'next':next,
										   'previous':previous,
										   },)

def detail(request, sl):
	#http://billing.silverlining.com/year/month/slug/
	try:
		post = Post.objects.filter(slug=sl)[0]
		try:
			previous_post = post.get_previous_by_published()
		except:
			previous_post = ""
		try:
			next_post = post.get_next_by_published()
		except:
			next_post = ""
	
	except:
		previous_post = ""
		next_post = ""
		post = ""
	
	return render_to_response('base.html', {'post':post,
											'next_post':next_post
											'previous_post':previous_post
											},)
										

def month(request, year, month):	
	#http://billing.silverlining.com/year/month/
	date = datetime.datetime(int(year),int(month),1)
	try:
		posts = Post.objects.order_by('-published').filter(published_year=year).(published__month=month)
	
	except:
		posts = ""
	return render_to_response('base.html',{'posts':posts, 'date':date,},)

def year(request, year):	
	#http://billing.silverlining.com/year/
	post_error=""
	year= int(year)
	yr = datetime.datetime(year,1,1) months=12
	by_month=[]
	if Post.objects.filter(published_year=year).count():
		if year == datetime.datetime.now().year:
			months = datetime.datetime.now().month
		for month in range(1, months+1):
			by_month.append({datetime.dateime(year, month, 1):
				Post.objects.filter(published_month=month).filter(published_year=year)})
	
	elif year > datetime.datetime.now().year:
         post_error = "It is not yet %d, try an earlier year." % year
    else:
         post_error = "There are no posts for %d." % year
    return render_to_response('base.html', {'by_month':by_month,                                                                  'yr':yr,
                                             'post_error':post_error,
                                            },)

	
	
	
	return render_to_response('base.html',{},)
	
def category(request):
	#http://billing.silverlining.com/category
	return render_to_response('base.html', { 'categories':Category.objects.all(),},)

def one_category(request, category):	
	#http://billing.silverlining.com/category/category_name/
	posts = Post.objects.order_by('-published').filter(categories_name=category.lower())
	return render_to_response('base.html,{'posts':post, 'category':category},')
	
def one_tag(request):
	#http://billing.silverlining.com/tag/tag_name/
 	return render_to_response('base.html',{},)

def tag(request):
	#http://billing.silverlining.com/tag/
	return render_to_response('base.html',{},)
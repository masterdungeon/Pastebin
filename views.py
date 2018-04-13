from django.shortcuts import render

from django import http
from django.template import Context, loader
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django import template
from django.views.decorators.csrf import csrf_protect, csrf_exempt, ensure_csrf_cookie
from django.template import RequestContext
from django.shortcuts import render_to_response

from pastebin.models import Paste
import hashlib

from django.views.decorators.cache import cache_page

# def main(request):
#     previous = request.POST.get('paste', '')

#     if previous:
#         id = hashlib.md5(previous).hexdigest()

#         try:
#             Paste.objects.get(url=id)
#         except:
#             p = Paste(content=previous, url=id)
#             p.save()

#         previous = 'http://%s/%s' % (request.get_host(), id)

#     t = loader.get_template('pastebin/index.html')
#     c = Context({
#         'previous': previous
#     })

#     return http.HttpResponse(t.render(c))

@cache_page(60 * 15)
@csrf_exempt
@ensure_csrf_cookie
def main(request):
	if request.method == "POST":
		previous = request.POST["content"]

		new_hash = previous.strip() 
		id = hashlib.md5(new_hash.encode()).hexdigest()

		try:
			Paste.object.get(url = id)
		except:
			p = Paste(content = previous, url = id)
			p.save()

		new_url = 'http://%s' % (id)
		return render(request, 'pastebin/index.html', {'new_url': new_url})
		# return HttpResponse(t.render(c))
		# return render_to_response('pastebin/index.html', t,context_instance = RequestContext(request))
	else:
		return render(request, 'pastebin/index.html')


def fetch_paste(request):
    url = request.META.get('PATH_INFO', '')[1:]
    content = ""

    try:
        p = Paste.objects.get(url=url)
    except:
        t = loader.get_template('pastebin/index.html')
        c = Context({
            'error': "Paste '%s' does not exist." % url
        })
        return http.HttpResponse(t.render(c))

    return http.HttpResponse(p.content)


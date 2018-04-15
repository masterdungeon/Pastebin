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

		new_url = 'http://%s%s' % ('127.0.0.1:8000/pastebin/fetch_paste/',id)
		return render(request, 'pastebin/index.html', {'new_url': new_url})
	else:
		return render(request, 'pastebin/index.html')


def fetch_paste(request):
    url = request.META.get('PATH_INFO', '')[22:]
    url = url[:len(url)-1]
    # content = ""

    p = Paste.objects.get(url=url)

    return render(request, 'pastebin/show.html', {'content': p.content})

    # try:
    #     p = Paste.objects.get(url=url)
    # except:
    #     t = loader.get_template('pastebin/index.html')
    #     c = Context({
    #         'error': "Paste '%s' does not exist." % url
    #     })
    #     return http.HttpResponse(t.render(c))

    


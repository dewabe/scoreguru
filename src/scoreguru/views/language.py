from django.shortcuts import redirect
from django.utils.translation import activate
from django.conf import settings
from django.http import HttpResponse

def set_language(request):
    lang = request.GET.get('lang')
    if lang:
        activate(lang) 
        response = redirect(request.META.get('HTTP_REFERER', '/')) 
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
        return response

    return redirect(request.META.get('HTTP_REFERER', '/'))
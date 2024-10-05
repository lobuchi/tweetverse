from django.http import HttpResponseRedirect

def home(request):
    # Redirect to the /tweets page
    return HttpResponseRedirect('/tweet/')

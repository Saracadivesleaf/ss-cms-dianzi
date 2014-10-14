from django.shortcuts import render_to_response

# Create your views here.
def science(request):
	return render_to_response('sciences.html')
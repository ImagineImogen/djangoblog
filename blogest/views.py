from django.shortcuts import render

def post_list(request):
    return render(request, 'blogest/post_list.html', {})


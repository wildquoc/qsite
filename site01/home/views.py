from django.shortcuts import render

def index(request):
    context = {
        'loi_chao': 'Trang chủ Django đã hoạt động.'
    }
    return render(request, 'home/home.html', context)

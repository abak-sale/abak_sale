from django.http import HttpResponse

def beranda(request):
    return HttpResponse("Halo ini kita pakai fungsion")

def tentang(request):
    return HttpResponse("Ini halaman tentang masih pakai Function")
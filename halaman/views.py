from django.http import HttpResponse

def beranda(request):
    return HttpResponse("Halo ini kita pakai fungsion")
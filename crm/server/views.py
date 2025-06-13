from django.shortcuts import HttpResponse


def main_view(request):
    return HttpResponse('Hey world!')


from django.urls import resolve


def app_name(request):
    current_app = resolve(request.path_info).namespace
    return {'current_app': current_app}

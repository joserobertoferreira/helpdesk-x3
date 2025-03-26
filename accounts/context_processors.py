from django.urls import resolve


def app_name(request):
    resolver = resolve(request.path_info)
    return {'current_app': resolver.namespace, 'current_url': resolver.url_name}

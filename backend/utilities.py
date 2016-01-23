from django.http import JsonResponse

# inspired from https://passingcuriosity.com/2009/writing-view-decorators-for-django/
def staff_check(function=None):
    def _dec(view_func):
        def _view(request, *args, **kwargs):
            if request.user.is_staff:
                response = {
                    'status' : 0,
                    'message' : ' You are logged in as staff. Only registered users have access to this section.'
                }
                return JsonResponse(response)
            else:
                return view_func(request, *args, **kwargs)
        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__
        return _view

    if function is None:
        return _dec
    else:
        return _dec(function)

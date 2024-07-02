from django.shortcuts import redirect

# In this middleware, we check if the user is authenticated and if last_login is None or must_change_password is True. 
# If any of these conditions are true, we redirect the user to the 'newPassword' page. 
# We also check if 'newPassword' is not in request.path to avoid redirect loops.

class ForcePasswordChangeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and (request.user.last_login is None or request.user.must_change_password) and 'newPassword' not in request.path and 'get_user_role' not in request.path:
            return redirect('newPassword')
        response = self.get_response(request)
        return response
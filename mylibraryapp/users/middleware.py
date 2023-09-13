from django.http import HttpResponse, HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse


class AuthenticationMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        user = request.user
        isLoginRoute = reverse('auth:login') == request.path
        isRegisterRoute= reverse('auth:signup') == request.path
        isCreateUserRoute= reverse('auth:create') == request.path
        if not user.is_authenticated and not (isLoginRoute or isRegisterRoute or isCreateUserRoute) :
            return HttpResponseRedirect(reverse('auth:login'))
        elif user.is_authenticated and (isLoginRoute or isRegisterRoute or isCreateUserRoute) :
            return HttpResponseRedirect(reverse('home'))  
        
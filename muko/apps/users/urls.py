from django.urls import path,re_path
from django.views.generic import TemplateView


from users.views import LoginView,RegisterView,LogoutView,ActiveUserView,ForgetPwdView,ResetView,ModifyPwdView

app_name = 'users'

urlpatterns = [

    path('', TemplateView.as_view(template_name='index.html'),name='index'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('register/',RegisterView.as_view(),name='register'),
    re_path(r'^active/(?P<active_code>.*)/$',ActiveUserView.as_view(),name = 'user_active'),

    path('forget/',ForgetPwdView.as_view(),name='forgetpwd'),
    re_path(r'^reset/(?P<active_code>.*)/$',ResetView.as_view(),name = 'resetpwd'),
    path('modifypwd/',ModifyPwdView.as_view(),name='modifypwd'),
]

from django.urls import path, include
from rest_framework.authtoken import views as rest_framework_views

# from helpecBackend.account import views as aviews 

from .views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home-view'),
    path('token/', rest_framework_views.obtain_auth_token, name='get_auth_token'),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
    # path('accounts/', aviews.HP_UserListAPIView.as_view(), name='account-list'),
]

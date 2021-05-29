from django.urls import path

from . import views

urlpatterns = [
    path('',views.index_view),
    path('addpast',views.addpast_view),
    path('reflash',views.reflash_view),
    path('addfuture',views.addfuture_view),
    path('reflashf',views.reflashf_view)
]
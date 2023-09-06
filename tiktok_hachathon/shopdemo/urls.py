from django.urls import include, path
from . import views
from .views import ShopView, CommocityDetailView

urlpatterns = [

]

urlpatterns += [
    # home page
    path('', views.ShopView.as_view(), name='shop_view'),
    # login/logout page
    path('accounts/', include('django.contrib.auth.urls')),

    path('shopdemo/', ShopView.as_view(), name='commodity_list'),
    path('shopdemo/(?P<pk>[0-9a-f-]+)/$', CommocityDetailView.as_view(), name='commodity_detail'),
]


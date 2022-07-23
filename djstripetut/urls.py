from django.contrib import admin
from django.urls import path
from products.views import (
    CreateCheckoutSessionView, 
    ProductLandingView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductLandingView.as_view(), name='landing-page'),
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
]

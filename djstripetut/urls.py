from django.contrib import admin
from django.urls import path
from products.views import CreateCheckoutSessionView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
]

import re
import stripe
from django.conf import settings
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views import View

from djstripetut.settings import STRIPE_PUBLIC_KEY

stripe.api_key = settings.STRIPE_SECRET_KEY



class ProductLandingView(TemplateView):
    template_name = "landing.html"

    def get_context_data(self, **kwargs: Any):
      context = super(ProductLandingView, self).get_context_data(**kwargs)
      context.update({
        "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
      })
      return context

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN = "http://127.0.0.1::8000"
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': '{{PRICE_ID}}',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success',
            cancel_url=YOUR_DOMAIN + '/cancel',
        )
        return JsonResponse({
          'id': checkout_session.id
        })# this may be the old way. New way follows:
        #return redirect(checkout_session.url, code=303)

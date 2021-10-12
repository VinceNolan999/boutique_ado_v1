from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JjikvFmWTEbwtxzDWZCRK1xBMVFA745dxAf3iwxhyknhpdJOZoKwr6MUOo1Yk1OO64HOLdel30yV2CuMrlZ2V7v00XDVgIPHl',
        'client_secret': 'sk_test_51JjikvFmWTEbwtxzu330TgMsSlfVjsfybwb22YH7Q6FN7YL6AfflpDCR9ITW7lTCzZ2bgTK1ZPcMalPWAhyCBDKZ00ED0CjZr4',
    }

    return render(request, template, context)

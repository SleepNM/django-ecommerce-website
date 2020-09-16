from .models import Order


def total_items(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order= Order.objects.get(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        cartItems = 404 #Placeholder for not logged in user
    return {'cartItems':cartItems}
from .models import OrderItem

def total_items(request):
    cart_quantity = 10
    return {'cart_quantity':cart_quantity}
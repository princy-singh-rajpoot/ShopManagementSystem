# context_processors.py

from .models import Cart
def message_processor(request):
    if request.user.is_authenticated:
        item_already_in_cartt = Cart.objects.filter(user=request.user).count()
    else:
        item_already_in_cartt = 0
    return {
        'item_already_in_cartt' :  item_already_in_cartt
    }
    
from .models import Cart
def message_processor(request):
    if request.user.is_authenticated:
        item_already_in_cartt = Cart.objects.filter(user=request.user).count()
    else:
        item_already_in_cartt = 0
    return {
        'item_already_in_cartt' :  item_already_in_cartt
    }
    
# Overall, this function is used to provide information about the number of items in the user's cart to the templates of a Django web application. 
# If the user is logged in, it counts the items in the cart associated with that user; otherwise, it defaults to 0.
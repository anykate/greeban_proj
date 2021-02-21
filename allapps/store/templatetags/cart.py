from django import template

register = template.Library()


@register.filter(name='cart_qty')
def cart_qty(product, cart):
    if cart:
        for id in cart.keys():
            if int(id) == product.id:
                return cart.get(id)
    return 0

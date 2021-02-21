from django.shortcuts import get_object_or_404, render, redirect
from .models import Category, Product
from django.http import JsonResponse


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def all_products(request):
    if request.user.id:
        products = Product.products.all().filter(created_by=request.user)
    else:
        products = Product.products.all()

    cart = request.session.get('cart')
    if not cart:
        request.session.cart = {}

    if request.is_ajax():
        product_id = request.POST.get('product_id', None)
        remove = request.POST.get('remove', None)
        cart = request.session.get('cart')

        if cart:
            quantity = cart.get(product_id)
            if quantity:
                if remove:
                    if quantity <= 0:
                        cart.pop(product_id)
                        # request.session.get('cart').clear()
                    else:
                        cart[product_id] = quantity-1
                else:
                    cart[product_id] = quantity+1

            elif not remove:
                cart[product_id] = 1

        elif not remove:
            cart = {}
            cart[product_id] = 1

        request.session['cart'] = cart
        return JsonResponse({
            'cart': cart,
            'product_id': product_id
        })

    return render(request, 'store/home.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product': product})

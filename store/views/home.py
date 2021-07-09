from django.shortcuts import render,redirect
from store.models.product import Product, Category
from django.views import View
#from store.models.info import info

# Create your views here.
class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1

                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart

        print(cart)
        return redirect('homepage')



    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        products = Product.get_all_products()

        categories = Category.get_all_categories()

        categoryID = request.GET.get('category')
        print(request.GET)
        if categoryID:
            products = Product.get_all_products_by_category_id(categoryID)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories
        #print('you r ', request.session.get('email'))
        return render(request, 'index.html', data)


    '''def infom(request):
        information = info.info_get_all()
        return render(request, "info.html", {'information': information})'''




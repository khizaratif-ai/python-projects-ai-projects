from django.shortcuts import render, redirect

from .models import Dish, Order, OrderItem

from .forms import OrderForm



def menu(request):

    dishes = Dish.objects.filter(
        available=True
    )

    return render(
        request,
        'menu.html',
        {
            'dishes': dishes
        }
    )



def add_to_cart(request, id):

    cart = request.session.get(
        'cart',
        []
    )

    cart.append(id)

    request.session['cart'] = cart

    return redirect('menu')



def cart(request):

    cart_ids = request.session.get(
        'cart',
        []
    )

    dishes = Dish.objects.filter(
        id__in=cart_ids
    )

    return render(
        request,
        'cart.html',
        {
            'dishes': dishes
        }
    )



def checkout(request):

    cart_ids = request.session.get(
        'cart',
        []
    )

    dishes = Dish.objects.filter(
        id__in=cart_ids
    )


    if request.method == "POST":

        form = OrderForm(
            request.POST
        )


        if form.is_valid():

            order = form.save()


            for dish in dishes:

                OrderItem.objects.create(

                    order=order,

                    dish=dish,

                    quantity=1

                )


            request.session['cart'] = []


            return render(
                request,
                'order_success.html'
            )


    else:

        form = OrderForm()



    return render(
        request,
        'checkout.html',
        {
            'form': form,
            'dishes': dishes
        }
    )
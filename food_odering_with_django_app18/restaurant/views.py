from decimal import Decimal

from django.shortcuts import render, redirect

from .models import Dish, Order, OrderItem
from .forms import OrderForm


def menu(request):

    dishes = Dish.objects.filter(
        available=True
    )

    return render(
        request,
        "menu.html",
        {
            "dishes": dishes
        }
    )


def add_to_cart(request, id):

    cart = request.session.get("cart", {})

    # Convert old list cart to dictionary cart
    if isinstance(cart, list):

        new_cart = {}

        for item in cart:

            item = str(item)

            if item in new_cart:
                new_cart[item] += 1
            else:
                new_cart[item] = 1

        cart = new_cart

    id = str(id)

    if id in cart:
        cart[id] += 1
    else:
        cart[id] = 1

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("menu")


def increase_quantity(request, id):

    cart = request.session.get("cart", {})

    id = str(id)

    if id in cart:
        cart[id] += 1

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")


def decrease_quantity(request, id):

    cart = request.session.get("cart", {})

    id = str(id)

    if id in cart:

        if cart[id] > 1:
            cart[id] -= 1
        else:
            del cart[id]

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")


def remove_from_cart(request, id):

    cart = request.session.get("cart", {})

    id = str(id)

    if id in cart:
        del cart[id]

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")


def cart(request):

    cart_data = request.session.get("cart", {})

    items = []

    subtotal = Decimal("0.00")

    for dish_id, quantity in cart_data.items():

        dish = Dish.objects.get(id=int(dish_id))

        total = dish.price * quantity

        subtotal += total

        items.append({

            "dish": dish,

            "quantity": quantity,

            "total": total

        })

    delivery = Decimal("4.99")

    tax = subtotal * Decimal("0.05")

    grand_total = subtotal + delivery + tax

    return render(

        request,

        "cart.html",

        {

            "items": items,

            "subtotal": subtotal,

            "delivery": delivery,

            "tax": tax,

            "grand_total": grand_total

        }

    )


def checkout(request):

    cart_data = request.session.get("cart", {})

    items = []

    subtotal = Decimal("0.00")

    for dish_id, quantity in cart_data.items():

        dish = Dish.objects.get(id=int(dish_id))

        total = dish.price * quantity

        subtotal += total

        items.append({

            "dish": dish,

            "quantity": quantity,

            "total": total

        })

    delivery = Decimal("4.99")

    tax = subtotal * Decimal("0.05")

    grand_total = subtotal + delivery + tax

    if request.method == "POST":

        form = OrderForm(request.POST)

        if form.is_valid():

            order = form.save()

            for item in items:

                OrderItem.objects.create(

                    order=order,

                    dish=item["dish"],

                    quantity=item["quantity"]

                )

            request.session["cart"] = {}
            request.session.modified = True

            return render(

                request,

                "order_success.html"

            )

    else:

        form = OrderForm()

    return render(

        request,

        "checkout.html",

        {

            "form": form,

            "items": items,

            "subtotal": subtotal,

            "delivery": delivery,

            "tax": tax,

            "grand_total": grand_total

        }

    )
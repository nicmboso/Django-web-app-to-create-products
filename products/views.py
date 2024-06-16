from django.shortcuts import render, redirect
from .models import Products

"""
for the models you created in the previous assignment, you are going to use those models
to create and list data on your own html templates powered by their own individual views like we did 

1 model allowed per view
"""

# Create your views here.

#search product via Title
#url ref: https://www.makeuseof.com/add-search-functionality-to-django-apps/

#url ref: https://www.youtube.com/watch?v=AGtae4L5BbI


def show_output(request):
    # Check if the request is a post request.
    if request.method == 'POST':
        # Retrieve the search query entered by the user
        search_query = request.POST['search_query']
        # Filter your model by the search query
        all_products = Products.objects.filter(Title__contains=search_query)
        return render(request, 'show-output.html', {"search_query":search_query, "all_products":all_products})
    else:
        return render(request, 'show-output.html',{})

#delete product via product_id
def delete_product(request, product_id):
    product = Products.objects.get(id=product_id)
    product.delete()
    return redirect('all_products') # this is the name of the url, it makes it easy so we don't have to type the entire url

#retrieve product_id
def product_detail(request, product_id):
    single_product = Products.objects.get(id=product_id)

    return render(request, "product-detail.html", context={
        "product": single_product
    })

#capture user data from webpage and post to db
def products_view(request):
    if request.method == "POST":
        Products.objects.create(
            Title=request.POST['Title'],
            Category=request.POST['Category'],
            Price=request.POST['Price'],
            Quantity=request.POST['Quantity'],
            In_stock=request.POST['In_stock']
            
        )

    """
    you have to render a context which is a dictionary
    that has the data you want to show to the user on the front end page (html)
    """
    products = Products.objects.all()
    return render(request, "products.html", context={
        "products": products
    })


from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import moviereview


# Create your views here.
def bs2(request):
    return JsonResponse({"data":"hello iam from basci2"})


products = [
    {"id": 1, "name": "iPhone 14", "category": "Electronics", "price": 69999, "stock": 15, "rating": 4.6
    },

    {"id": 2, "name": "Samsung Galaxy Buds", "category": "Accessories", "price": 7999, "stock": 40, "rating": 4.4
    },
    {"id": 3, "name": "Nike Running Shoes", "category": "Footwear", "price": 5499, "stock": 25, "rating": 4.5
    },
    {"id": 4, "name": "Boat Smart Watch", "category": "Wearables", "price": 2999, "stock": 60, "rating": 4.2
    },
    {"id": 5, "name": "Dell Laptop", "category": "Electronics", "price": 54999, "stock": 10, "rating": 4.7
    }
]

def productById(request,id):
    print(id)
    for product in products:
        if product["id"]==id:
            return JsonResponse(product)
    return JsonResponse({"error":"product not found"})



def productBycategory(request, ctg):
    result = []
    for product in products:
        if product["category"].lower() == ctg.lower():
            result.append(product)

    if result:
        return JsonResponse(result, safe=False)
    return JsonResponse({"error": "product not found"})




def movivebyid(request, id):
    movie = get_object_or_404(moviereview, id=id)
    movie_result={"id":movie.id,"name":movie.movie_name}
    print(movie.movie_name)
    return JsonResponse({"status": "success","data":movie_result})

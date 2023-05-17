from django.shortcuts import render
import requests
# Create your views here.


# The is Fake api json data 
def Json_data(request):
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    Json_data_response = response.json()
    return render (request, 'test/base.html', {"Info" : Json_data_response})


# The is custom data 
def product(request):
    list = [{
        "name" : "Mehedi",
        "Email" : "m@12gmail.com"      
    },{ 
        "name" : "Hasan",
        "Email" : "h@456gmail.com"    
    }]
    return render (request, 'test/product.html',{"data" : list})
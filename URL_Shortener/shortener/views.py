import os
print(os.listdir())



from django.shortcuts import render
from .models import Urls, AllUrls
from .utilities.short_code import (
    generate_body,
    build_short_url,
)

def home(request):
    if request.method == "POST":
        user_url = request.POST.get("url")
        body = generate_body(length=8)
        short_url = build_short_url(body)

        url, creation_status = Urls.objects.get_or_create(
            original_destination=user_url,
            generated_short_url=short_url,
        )
        unique_url, creation_status = AllUrls.objects.get_or_create(short_url=short_url)
        
        return render(request, "shortener/home.html", {"final_url": short_url})
    
    elif request.method == "GET":        
        return render(request, "shortener/home.html", {"final_url": None})

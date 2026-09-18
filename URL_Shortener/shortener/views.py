import logging
from django.shortcuts import render
from .models import Urls, AllUrls
from .utilities.short_code import (
    generate_body,
    build_short_url,
)
from .security_utilities.utilities import get_client_ip

logger = logging.getLogger(__name__)
logger.info(f"Logging started successfully from {__name__}")


def home(request):
    USER_IP = get_client_ip(request=request)

    if request.method == "POST":
        logger.info(f"Some user from {USER_IP} IP requested POST method.")

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
        logger.info(f"Some user from {USER_IP} IP visited home page.")
        return render(request, "shortener/home.html", {"final_url": None})

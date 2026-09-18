from django.db import models


class Urls(models.Model):
    user_ipv4 = models.GenericIPAddressField(default="1.2.3.4", max_length=15)
    user_url = models.URLField(max_length=200)
    short_url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    # NOTE: For now I have no idea of how can I implement it
    # total_clicks = models.IntegerField(default=0)

    def __str__(self):
        return_text = (
            f"URL {self.user_url} with the generated short URL {self.short_url} \
            was created at {self.created_at}."
        )
        return return_text

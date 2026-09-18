from django.db import models

class Urls(models.Model):
    original_destination = models.URLField(max_length=200)
    generated_short_url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    total_clicks = models.IntegerField(default=0)
    
    def __str__(self):
        return_text = (
            f"URL {self.original_destination} with the generated short URL {self.generated_short_url} \
            was created at {self.created_at} and has been clicked {self.total_clicks} times."
            )
        return return_text
    
class AllUrls(models.Model):
    short_url = models.URLField(max_length=200)

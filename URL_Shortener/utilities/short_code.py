from string import ascii_lowercase, ascii_uppercase
import random

def generate_body(length: int) -> str:
    """Function to generate the body (`length` number of letter) consisting
    of random number of both lowercase and uppercase letters.

    Args:
        length (int): length of the body. Must be greater or equal to 6.

    Returns:
        str: body of the short URL
    """
    
    # NOTE: Ensuring that lowercase count does not exceed the total length
    max_lowercase = min(6, length - 1) if length > 1 else 1
    
    no_of_lowercase = random.randint(1, length)
    no_of_uppercase = length - no_of_lowercase
    
    lowercase_chars = [random.choice(ascii_lowercase) for _ in range(no_of_lowercase)]
    uppercase_chars = [random.choice(ascii_uppercase) for _ in range(no_of_uppercase)]
    
    body = (lowercase_chars + uppercase_chars)
    random.shuffle(body)
    
    return "".join(body)


def build_short_url(body: str, domain: str, secure: bool) -> str:
    heading = "https://" if secure else "http://"
    return f"{heading}{domain}.me/go/{body}"
    
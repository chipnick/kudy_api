from base64 import urlsafe_b64encode, urlsafe_b64decode


def base64UrlEncode(data):
    return urlsafe_b64encode(data).rstrip(b'=')


def base64UrlDecode(base64Url):
    padding = b'=' * (4 - (len(base64Url) % 4))

    return urlsafe_b64decode(base64Url + padding)
class NoMoreTweetsException(Exception):
    def __init__(self):
        super().__init__("No More Tweets!")


class TokenExpiryException(Exception):
    def __init__(self):
        super().__init__("Token Expired")


class RefreshTokenException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

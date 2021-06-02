class Codec:
    def __init__(self):
        self.key = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        for i, phrase in enumerate(longUrl.split("/")):
            self.key[f'{i}'] = phrase
        
        tiny_url = "".join(self.key.keys())
        return tiny_url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        longUrl = []
        for char in shortUrl:
            longUrl.append(self.key[char])
        return "/".join(longUrl)
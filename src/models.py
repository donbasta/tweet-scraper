class Tweet:
    def __init__(self, uname, ts, text_content):
        self.uname = uname
        self.timestamp = ts
        self.text = text_content

    def __str__(self):
        return f'<{self.uname} ({self.timestamp})>: {self.text}\n'

class Browser:
    def __init__(self):
        pass

    def cleanup(self):
        pass

class Chrome:
    def __init__(self):
        pass

class Firefox:
    def __init__(self):
        pass

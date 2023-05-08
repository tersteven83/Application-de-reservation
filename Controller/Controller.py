import View


class Controller:
    def render(self, filename, method, data):
        View.filename.method(data)

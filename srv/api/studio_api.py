class BaseAPI:
    def __init__(self, model=None, **kwargs):
        self.model = model
        self.kwargs = kwargs


class StudioAPI(BaseAPI):
    def create(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

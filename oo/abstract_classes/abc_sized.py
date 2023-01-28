from collections.abc import Sized

class MyListing(Sized):
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description

    # Abstract Class Method
    def __len__(self):
        return super().__len__()


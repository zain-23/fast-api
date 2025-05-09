from fastapi import FastAPI

app = FastAPI()

class Cat():
    def __init__(self, name):
        self.name = name

fluffy = Cat(name="Mr Fluffy")
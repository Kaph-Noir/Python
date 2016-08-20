class Car(object):
    condition = "new"
    model = "DeLorean"
    color = "silver"
    mpg = 88

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.mpg = self.mpg


if __name__ == "__main__":
    my_car = Car("DeLorean", "silver", 90)
    print(my_car.condition)
    print(my_car.mpg)
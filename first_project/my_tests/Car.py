class Car:

    def __init__(self, model, price):
        self.model = model
        self.price = price
        self.started_engine = False

    def start_engine(self):
        self.started_engine = True
        print('Engine is running!')

    def stop_engine(self):
        if self.started_engine:
            self.started_engine = False
            print('Engine is stopped!')
        else:
            print('Engine is not running now!')

    def __str__(self):
        return f'{self.model} - {self.price}'


if __name__ == '__main__':
    car = Car('Tesla Model X', 5000)
    print(car)
    car.start_engine()
    car.stop_engine()
    car.stop_engine()

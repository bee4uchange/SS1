class Cars:
    def __init__(self):
        self.items = {}

    def add(self, brand, model, color):
        self.items = {
            "Brand": brand,
            "Model": model,
            "Color": color
        }

    def getBrand(self):
        return self.items["Brand"]

    def print(self):
        print(self.items)

if __name__ == '__main__':
    car = Cars()
    car.add('Toyota', 'ADDQW54', 'Black')
    print('Brand:', car.getBrand())
    car.print()

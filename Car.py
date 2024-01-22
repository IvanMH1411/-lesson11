class Car:
    def __init__(self):
        self.color = input("Input your car color:\n")
        self.car_type = input("Input your car type:\n")
        while True:
            year = input("Input your car year:\n")
            if year.isdigit():
                if 1975 < float(year) < 2025:
                    self.year = year
                    break
                else:
                    print("Invalid year")
            else:
                print("It is not year")
        self.is_engine_started = False

    def start_engine(self):
        if not self.is_engine_started:
            self.is_engine_started = True
            print("Engine started")

    def stop_engine(self):
        if self.is_engine_started:
            self.is_engine_started = False
            print("Engine stopped")

    def change_color(self, color):
        self.color = color
        print(f"Color is changed to {color}")

    def change_year(self, year):
        while True:
            year = input("Input your car year:\n")
            if year.isdigit():
                if 1975 < float(year) < 2025:
                    self.year = year
                    break
                else:
                    print("Invalid year")
            else:
                print("It is not year")
        print(f"Car year is changed to {year}")

    def change_car_type(self, car_type):
        self.car_type = car_type
        print(f"Color is changed to {car_type}")

# Programming Assignment: Классы и наследование 
# use print(Car.mro()) to method resolution order for super classes
# cars.csv file Example
# car_type;brand;passenger_seats_count;photo_file_name;body_whl;carrying;extra
# car;Nissan xTtrail;4;f1.jpeg;;2.5;
# truck;Man;;f2.png;8x3x2.5;20;
# truck;Man;;f2.png;;20;
# car;Mazda 6;4;f3.jpeg;;2.5;
# ;;;
# spec_machine;Hitachi;;f4;;1.2;Ð›ÐµÐ³ÐºÐ°Ñ Ñ‚ÐµÑ…Ð½Ð¸ÐºÐ° Ð´Ð»Ñ ÑƒÐ±Ð¾Ñ€ÐºÐ¸ ÑÐ½ÐµÐ³Ð°

import os
import csv


class BaseCar:
    def __init__(self, car_type="", brand="", photo_file_name="", carrying=0.0):
        self.car_type = car_type
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying

    @property
    def extention(self):
        """Return car's photo file extension"""
        try:
            path, filename = os.path.split(self.photo_file_name)
        except FileExistsError:
            return ""
        if "." in filename:
            f = filename.split('.')
            ext = f[-1]
            if ext is not None:
                return ext
        else:
            return ""


class Car(BaseCar):
    def __init__(self, car_type="", brand="", passenger_seat_count=0, photo_file_name="", carrying=0.0):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.passenger_seat_count = passenger_seat_count


class Truck(BaseCar):
    def __init__(self, car_type="", brand="", photo_file_name="",
                 length=0.0, height=0.0, width=0.0, carrying=0.0):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.body_length = length
        self.body_height = height
        self.body_width = width

    # https://www.python-course.eu/python3_properties.php
    @property
    def volume(self):
        return self.body_length * self.body_height * self.body_width

    def get_body_volume(self):
        return self.volume


class SpecMachine(BaseCar):
    def __init__(self, car_type="", brand="", photo_file_name="", carrying=0.0, extra=""):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.extra = extra


# car_type;brand;passenger_seats_count;photo_file_name;body_whl;carrying;extra
def read_from_file(filaname):
    cars = []
    vehicle = None
    try:
        with open(filaname) as csv_fd:
            reader = csv.reader(csv_fd, delimiter=';')
            next(reader)
            for row in reader:
                # skip the row with wrong number of fields
                if len(row) == 7:
                    try:
                        car_type = str(row[0])
                        brand = row[1]
                        passenger_seat_count = row[2]
                        photo_file_name = row[3]
                        body_whl = row[4]
                        carrying = row[5]
                        extra = row[6]

                        if car_type == 'car':
                            # print(Car.mro()) - Method Resolution Order for calling __init__() of super classes
                            vehicle = Car(car_type=car_type, brand=brand,
                                          passenger_seat_count=int(passenger_seat_count),
                                          photo_file_name=photo_file_name, carrying=float(carrying))
                        elif car_type == 'truck':
                            try:
                                [width, height, length] = body_whl.split('x')
                            except ValueError:
                                # We dont ignore missing volume parameters
                                [width, height, length] = 0, 0, 0

                            vehicle = Truck(car_type=car_type, brand=brand,
                                            photo_file_name=photo_file_name,
                                            length=float(length), height=float(height), width=float(width),
                                            carrying=float(carrying))
                        elif car_type == 'spec_machine':
                            vehicle = SpecMachine(car_type=car_type, brand=brand,
                                                  photo_file_name=photo_file_name, carrying=float(carrying),
                                                  extra=extra)

                    except ValueError as err:
                        print(f"Error bad row: {row},  {err} !!!")
                        continue
                    if isinstance(vehicle, BaseCar):
                        cars.append(vehicle)
                        print(row)
    except FileNotFoundError as err:
        print(f"Error {err.filename}: {err.strerror}")

    return cars


def get_car_list():
    return read_from_file('cars.csv')


def main():
    vehicles = get_car_list()
    for vehicle in vehicles:
        if isinstance(vehicle, Truck):
            print(f"{vehicle.get_body_volume()}, {vehicle.extention}")


if __name__ == "__main__":
    main()

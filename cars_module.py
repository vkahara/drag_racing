import car

def choose_car(chosen_car):
    ford_scorpio = car.Car("Ford", "Scorpio", 1, 20, "ford_scorpio.png")
    mitsubishi_evo = car.Car("Mitshubishi", "Lancer Evo VI", 3, 10, "mitsubishi_evo.png")
    toyota_supra = car.Car("Toyota", "Supra", 5, 10, "meitsi.jpg")

    cars_dict = {
        "ford_scorpio": ford_scorpio,
        "mitsubishi_evo": mitsubishi_evo,
        "toyota_supra": toyota_supra
    }
    return cars_dict[chosen_car]

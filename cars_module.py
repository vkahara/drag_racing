import car

ford_scorpio = car.Car(0, "Ford", "Scorpio", 1, 20, "ford_scorpio.png")
mitsubishi_evo = car.Car(1, "Mitshubishi", "Lancer Evo VI", 3, 10, "mitsubishi_evo.png")
toyota_supra = car.Car(2, "Toyota", "Supra", 5, 10, "meitsi.jpg")
volkswagen_golf = car.Car(3, "Volkswagen", "Golf", 2, 15, "volkswagen_golf.png")

cars_dict = {
    "ford_scorpio": ford_scorpio,
    "mitsubishi_evo": mitsubishi_evo,
    "toyota_supra": toyota_supra,
    "volkswagen_golf": volkswagen_golf
}


def choose_car(chosen_car):
    return cars_dict[chosen_car]

def cycle_names(ID):
    for key in cars_dict.values():
        if key.ID == ID:
            return key.make + " " + key.model
        
def cycle_images(ID):
    for key in cars_dict.values():
        if key.ID == ID:
            return key.image
        
#create list from dictionary keys and return dictionary key based on inputted ID
def get_car_key(ID):
    keys_list = list(cars_dict.keys())
    for key in cars_dict.values():
        if key.ID == ID:
            return keys_list[ID]
            
            

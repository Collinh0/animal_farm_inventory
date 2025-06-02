from datetime import date


class AnimalFeeder:
    def __init__(self):
        self.fed_today = {}

    def feed(self, animal_id, name):
        today = date.today()
        if animal_id not in self.fed_today:
            self.fed_today[animal_id] = {}
        self.fed_today[animal_id][name] = today
        print(f"Fed {name} (ID: {animal_id}) on {today}.")  #Feed the animal and record the feeding date.
   
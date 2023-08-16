
class Vehicle:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along...")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")

my_car = Vehicle('BMW',"GT")
my_car.get_make_model()

your_car = Vehicle('Cadillac', 'Escalade')
your_car.get_make_model()

class Airplane(Vehicle):

    def __init__(self, make, model, faa_id):
        super().__init__(make,model)
        self.faa_id = faa_id

    def moves(self):
        print('Flies Along...')


class  Truck(Vehicle):
    def moves(self):
        print("Rumbles along...")

class GolfCart(Vehicle):
    pass

cessna = Airplane("Cessna",'Skyhwak','N-123')
mack = Truck('Mack',"Pinnacle")
golfwagen = GolfCart("Yamaha", "GC100")


cessna.get_make_model()
cessna.moves()

mack.get_make_model()
mack.moves()

golfwagen.get_make_model()
golfwagen.moves()


print("""
.
.
.
.
.
.
.
""")


for v in (my_car,your_car,cessna,mack,golfwagen):
    v.get_make_model()
    v.moves()
import random

class River :
    rivers = ["Volta","Pra","Ancobra","Tano","Offin","Dansu","Brim"]

    @classmethod
    def set_river(cls,dam):
        return f"The {dam} should be in {random.choice(cls.rivers)}"

option = River.set_river("Akosombo dam")
print(option)

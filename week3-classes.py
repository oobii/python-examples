import json
import pprint

class Pet:
    def __init__(self,name=None):
        self.name = name

class Dog(Pet):
    def __init__(self,name,breed=None,):
        super(Dog, self).__init__(name)
        self.__breed = breed

    def say(self):
        return f"{self.name} says \'Waw!\'"

    def get_breed(self):
        return self.__breed

mydog = Dog("Rex","hound")
print(mydog.say())

print(issubclass(Dog,Pet))
print(isinstance(mydog,Pet))

class ExportJSON:
    def to_json(self):
        return json.dumps({"name": self.name, "breed": self.breed})

class ExDog(Dog, ExportJSON):
    pass

doggie = ExDog("Lessi", breed="Collie")
#print(doggie.to_json())
pprint.pprint(ExDog.__mro__)

class WoolenDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        super(Dog,self).__init__(name)
        self.breed = "woolen dog taxa"

    def __repr__(self):
        return f"{self.name} --- {self.breed}"

    def get_breed(self):
        return f" {self.name} breed is {self.__breed}"

taxa = WoolenDog("Suzi", "taxa")
print(taxa)

# This one has attribute from other class, not really recommended
class SomeDog(Dog, ExportJSON):
    def get_breed(self):
        return f"SomeDog of breed {self._Dog__breed}"

somedog = SomeDog("Tuzik","Nobreed")
print(somedog.get_breed())

#print(taxa.get_breed())
print(somedog.__dict__)

# Task: Implement export method for class using composition

class Mamal:
    def __init__(self,name):
        self.name = name


class Primate(Mamal):
    def __init__(self,name,exporter=None):
        #super(Primate,self).__init__(name)
        self.name = name
        self.__exporter = exporter

    def export(self):
        return self.__exporter.export(self)

class MamalExport:
    def export(self):
        raise NameError("Not Implemented")

class ExportMyJson(MamalExport):
    def export(self,specie):
        return json.dumps({'name': specie.name})

class ExportHTML(MamalExport):
    def export(self,specie):
        return f"""
<xml>
<mamal>
<name>
{specie.name}
</name>
</mamal>
</xml>        
"""

monkey = Primate("Baboon",ExportMyJson())
print(monkey.export())
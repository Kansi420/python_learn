class cat:

    classification = "mammals"

    def description(self):
        return f"{self.name} is {self.age} years old!"
    
    def speak(self, sound):
        return f"{self.name} says {sound}!"
    
class pussy_cat(cat):
    def speak(self, sound="woof"):
        return f"{self.name} says {sound}! {sound}!" 

class lion(cat):
    def speak(self, sound="woof"):
        return f"{self.name} says {sound}! {sound}!"

class tiger(cat):
    def speak(self, sound="Arf"):
        return super().speak(sound)
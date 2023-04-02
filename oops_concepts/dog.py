class dog:

    classification = "mammals"

    def __init__(self, name, age) -> None:
        self.name = name 
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old!"
    
    def speak(self, sound):
        return f"{self.name} says {sound}!"

class Labrador(dog):
    def speak(self, sound="woof"):
        return f"{self.name} says {sound}! {sound}!"

class Bulldog(dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

if __name__ == "__main__":
    joy = Labrador("joy", 4)
    jim = Bulldog("Jim", 5)

    print(joy.description())
    print(joy.speak())
    print(jim.speak())

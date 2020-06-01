#I've createda  a generalized class call Pet
class Pet:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} year old")

    def speak(self):
        print(f"My name is {self.name} and I don't Know what to say") 

#Then I created some specific classes for both Cat and dog which contains the methods that diferentiated one from the other.
class Cat(Pet):
#In the class Cat I want to have an additional attribute "color", but I don't want to redifine all name and age again.    
    def __init__(self, name, age, color):
#Therefore I will use the super(). method, which makes a reference to the upper class, in this case Pet and its attributes, so I call them from it.
        super().__init__(name, age)
        self.color = color

    def show(self):
        print(f"My name is {self.name} and my color is {self.color}")
    
    def speak(self):
        print("Meow")
    
class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

#Now we will use the PET class
p = Pet("Tim", 19)
p.show()
#now I will use the Cat class, and no show() method was defined on class 
# but since the Pet clase is inheritated to the other classes they are able to use the show().
c = Cat("Tom", 34, "Black")
c.show()
d = Dog("Jerry", 25)
d.show()
f = Fish("Bubbles",10)
f.show()

#I've defined a method call speak on the three classes. just to show that if a method with the same name is defined on the Generalist class and in the specific
#class, then it will use the specific instead of the generalist.
d.speak()
f.speak()
#As you can see in the case of dog it has a specific speak method so it will use it, but in the case of bubles, since it does not have a method it will use
#the general one.

class dog():
    def __init__(self,name,age) :
        self.name=name
        self.age=age
    def sit(self):
        print(self.name.title()+" is now sitting")
    def roll(self):
        print(self.name.title()+" rolled over!")

my_dog=dog("willie",6)
your_dog=dog("puppie",3)
my_dog.sit()
your_dog.roll()
class dog:
  def __init__(self,name,age,coat_color):
     self.name=name
     self.age=age
     self.coat_color=coat_color
  def description(self):
     return(self.name,self.age)
  def get_info(self):
     return(self.coat_color)
class JackRussellTerrier(dog):
  def __init__(self,name,age,coat_color):
    super().__init__(name,age,coat_color)
  def am_jack(self):
    return('Hello am JackRusselTerrrier')
class Bulldog(dog):
  def __init__(self,name,age,coat_color):
    super().__init__(name,age,coat_color)
  def am_bull(self):
    return('Hello am Bull dog')
dog_name=input('enter the name')
dog_age=int(input('enter the age'))
dog_coat_color=input('enter the color')
obj=dog(dog_name,dog_age,dog_coat_color)
print(obj.description())
obj2=JackRussellTerrier('neke',2,'brown')
print(obj2.am_jack())
obj3=Bulldog('pro',2,'black')
print(obj3.am_bull())
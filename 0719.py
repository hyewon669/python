##class Car:
##     model="BMW"
##     color="white"
##
##     def speedChange(self,v):
##          print("speedChange",v)
##          self.speed=v
##
##bmw=Car()
##bmw.speedChange(20)

##class Car:
##     model="BMW"
##     color="white"
##
##bmw=Car()
##benz=Car()
##benz.model="Benz"
##benz.color="black"
##print(bmw.model)
##print(bmw.color)
##
##print(benz.model)
##print(benz.color)

##class Car:
##     def __init__(self,model,color):
##          self.model = model
##          self.color=color
##     def info(self):
##          print("Model : ",self.model,",Color :",self.color)
##bmw=Car("BMW","white")
##bmw.info()
##benz=Car("Benz","black")
##benz.info()

##class Car:
##     def __init__(self,model,color):
##          self.model = model
##          self.color=color
##     def info(self):
##          print("Model : ",self.model,",Color :",self.color)
##
##class CarDrive(Car):
##     def speedChange(self,v):
##          self.speed = v
##          print("speedChange:",self.speed)
##
##bmw=CarDrive("BMW","white")
##bmw.info()
##bmw.speedChange(100)
##
##

##class Character:
##     def __init__(self,name,weapon) :
##          self.name=name
##          self.weapon=weapon
##
##     def intro(self):
##          print("Name :",self.name)
##          print("Weapon :",self.weapon)
##
##class Action(Character):
##     step=0
##
##     def move_forward(self,n):
##          self.step +=n
##          print("Current location is %d."%self.step)
##     def move_backyard(self,n):
##          self.step -=n
##          print("Current location is %d."%self.step)
##     def turn_right(self):
##          print("Turn right")
##     def turn_left(self):
##          print("Turn left")
##lugo = Action('lugo','gun')
##lugo.intro()
##lugo.move_forward(10)
##lugo.move_backyard(3)
##lugo.turn_right()
##lugo.turn_left()

class TV:
     def __init__(self,channel,volume):
          self.power= True
          self.channel=channel
          self.volume=volume

     def on_off(self):
          if self.power:
               self.power=False
               print("Turn off")
          else:
               self.power=True
               print("Turn on")
     def info(self):
          print("Power:",self.power)
          print("Channel:",self.channel)
          print("volume:",self.volume)

     def set_channel(self,channel):
          if self.power:
               self.channel=channel
          else:
               print("Power off")
     def set_volume(self,volume):
          if self.power:
               self.volume=volume
          else:
               print("Power off")
tv=TV(1,16)
tv.set_channel(111)
tv.set_volume(10)
tv.on_off()
tv.set_volume(13)            
tv.info()

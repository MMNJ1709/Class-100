class Car(object):
    def __init__(self,model,color,company,speedLimit):
        self.model=model
        self.color=color
        self.company=company
        self.speedLimit=speedLimit

    def start(self):
        print("started")
    def stop(self):
        print("stop")
    def acelerate(self):
        print("acelerate")
    
#define cars
Audi=Car("Q7","white","Audi",180)
BMW=Car("M4","blue","BMW",170)

print(Audi.color)
print(Audi.start())
print(BMW.acelerate())
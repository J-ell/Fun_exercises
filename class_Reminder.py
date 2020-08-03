import threading
import time
class Reminder:
    def __init__(self, reference_time = 12.00, breakfast_time = None, launch_time = None, dinner_time = None):
        self._reference_time = reference_time
        self.breakfast_time = breakfast_time
        self.launch_time = launch_time
        self.dinner_time = dinner_time

        interval1 = abs(self._reference_time - self.breakfast_time)
        interval2 = abs(self._reference_time - self.launch_time)
        interval3 = abs(self._reference_time - self.dinner_time)
        breakfast = threading.Timer(interval1, self.breakfast)
        launch = threading.Timer(interval2, self.launch)
        dinner = threading.Timer(interval3, self.dinner)

        breakfast.start()
        launch.start()
        dinner.start()

    def __str__(self):
        return f"object has a reference_time of {self._reference_time}"

    def breakfast(self):
        print(f"it's {self.breakfast_time} and it's time for breakfast")
        print("A good food suggestion is; pancakes with smashed eggs, sausage and baked beans \n")

    def launch(self):
        print(f"it's {self.launch_time} and it's time for launch")
        print("A good food suggestion is; pounded yam with vegetable soup \n")

    def dinner(self):
        print(f"it's {self.dinner_time} and it's time for dinner")
        print("A good food suggestion is; Hot akara with pap")

    def terminate(self, food_time):
        food_time.cancel()

    def get_reference_time(self):
        return self._reference_time

    def set_reference_time(self, new_time):
        if isinstance(new_time, int) and new_time >= 0:
            self._reference_time = new_time

    reference_time = property(get_reference_time, set_reference_time, doc= "A reference_time property")



ella = Reminder(6.0, 8.0, 26.0, 36.0 )

print(ella)
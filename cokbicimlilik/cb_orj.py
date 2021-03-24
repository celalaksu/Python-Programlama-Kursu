import time

class Vehicle():
    def change_direction(left, on):
        pass

    def turn(self,left):
        self.change_direction(left, True)
        time.sleep(0.25)
        change_direction(left, False)


class TrackedVehicle(Vehicle):
    def control_track(left, stop):
        pass

    def change_direction(left, on):
        control_track(left, on)


class WheeledVehicle(Vehicle):
    def turn_front_wheels(left, on):
        pass

    def change_direction(left, on):
        turn_front_wheels(left, on)
        
p_arac = TrackedVehicle()
p_arac.turn()

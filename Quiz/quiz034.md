# Quiz 034

## Code
```.py
class Flight:
    def __init__(self, flight_number: str, origin: str, destination: str, available_seat: int):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.available_seat = available_seat
        self.passenger_list = []

    def add_passenger(self, passenger_name: str) -> bool:
        if len(self.passenger_list) < self.available_seat:
            self.passenger_list.append(passenger_name)
            return True
        return False

    def remove_passenger(self, passenger_name: str) -> bool:
        if passenger_name in self.passenger_list:
            self.passenger_list.remove(passenger_name)
            return True
        return False

    def is_full(self):
        if len(self.passenger_list) >= self.available_seat:
            return "There are no more available seats"
        else: return f"There are still {self.available_seat - len(self.passenger_list)} seats on flight {self.flight_number}"
```
## Proof of work
![image](https://github.com/user-attachments/assets/0d8209c4-e1b9-4784-ae74-523fd91b8c1e)


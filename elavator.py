class Elevator:
    """
    Класс для расчета подъема груза на этаж
    """

    def __init__(self, capacity):
        self.capacity = capacity
        
    def manual_up(price = 300):
        pass

    def count_price(self, weight: float) -> int:
        if weight > self.capacity:
            return "Вес превышает грузоподъемность лифта!"
        if weight <= 0.25 * self.capacity:
            price = 300
        elif weight <= 0.5 * self.capacity:
            price = 500
        elif weight <= 0.75 * self.capacity:
            price = 800
        else:
            price = 1000
        return price

    def up(price = 300):
        pass
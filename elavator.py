class Elevator:
    """
    Класс для расчета подъема груза на этаж
    """

    def __init__(self, capacity):
        self.capacity = capacity

    def _count_price(self, weight: float) -> int:
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
    
    def manual_up(self, weight: float, floor: int) -> int:
        if weight <= 0:
            return "Вес должен быть положительным!"
        if floor <= 0:
            return "Этаж должен быть положительным!"

        base_price = self.count_price(weight)
        if isinstance(base_price, str): 
            return base_price
        
        additional_price = 300 * (floor - 1) * (weight // 100 + 1)

        total_price = base_price + additional_price
        return total_price

    def up(self, weight: float):
        return self._count_price(weight)

a = Elevator(100)
print(a.up(65))

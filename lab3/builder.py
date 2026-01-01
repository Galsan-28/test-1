class Pizza:
    def __init__(self):
        self.dough = ""
        self.sauce = ""
        self.topping = ""

    def set_dough(self, dough):
        self.dough = dough

    def set_sauce(self, sauce):
        self.sauce = sauce

    def set_topping(self, topping):
        self.topping = topping

    def __str__(self):
        return f"Pizza{{dough='{self.dough}', sauce='{self.sauce}', topping='{self.topping}'}}"


# Интерфейс строителя
class PizzaBuilder:
    def build_dough(self):
        raise NotImplementedError("Метод build_dough() должен быть реализован")

    def build_sauce(self):
        raise NotImplementedError("Метод build_sauce() должен быть реализован")

    def build_topping(self):
        raise NotImplementedError("Метод build_topping() должен быть реализован")

    def get_result(self):
        raise NotImplementedError("Метод get_result() должен быть реализован")


# Конкретный строитель для Гавайской пиццы
class HawaiianPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def build_dough(self):
        self.pizza.set_dough("cross")
        print("Добавлено тесто: cross")

    def build_sauce(self):
        self.pizza.set_sauce("mild")
        print("Добавлен соус: mild")

    def build_topping(self):
        self.pizza.set_topping("ham+pineapple")
        print("Добавлена начинка: ham+pineapple")

    def get_result(self):
        return self.pizza


# Конкретный строитель для Пепперони
class PepperoniPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def build_dough(self):
        self.pizza.set_dough("pan baked")
        print("Добавлено тесто: pan baked")

    def build_sauce(self):
        self.pizza.set_sauce("hot")
        print("Добавлен соус: hot")

    def build_topping(self):
        self.pizza.set_topping("pepperoni+salami")
        print("Добавлена начинка: pepperoni+salami")

    def get_result(self):
        return self.pizza


# Конкретный строитель для Вегетарианской пиццы
class VeggiePizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def build_dough(self):
        self.pizza.set_dough("thin")
        print("Добавлено тесто: thin")

    def build_sauce(self):
        self.pizza.set_sauce("tomato")
        print("Добавлен соус: tomato")

    def build_topping(self):
        self.pizza.set_topping("mushrooms+peppers+onions")
        print("Добавлена начинка: mushrooms+peppers+onions")

    def get_result(self):
        return self.pizza


# Директор
class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_pizza(self):
        print("Начинаем приготовление пиццы...")
        self.builder.build_dough()
        self.builder.build_sauce()
        self.builder.build_topping()
        print("Пицца готова!\n")

    def get_pizza(self):
        return self.builder.get_result()
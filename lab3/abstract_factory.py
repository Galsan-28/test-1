class Button:
    def paint(self):
        raise NotImplementedError("Метод paint() должен быть реализован")


# Конкретный продукт A1
class WindowsButton(Button):
    def paint(self):
        print("You have created a Windows button.")


# Конкретный продукт A2
class MacButton(Button):
    def paint(self):
        print("You have created a Mac button.")


# Конкретный продукт A3 (дополнительный пример)
class LinuxButton(Button):
    def paint(self):
        print("You have created a Linux button.")


# Интерфейс для продукта B
class Checkbox:
    def paint(self):
        raise NotImplementedError("Метод paint() должен быть реализован")


# Конкретный продукт B1
class WindowsCheckbox(Checkbox):
    def paint(self):
        print("You have created a Windows checkbox.")


# Конкретный продукт B2
class MacCheckbox(Checkbox):
    def paint(self):
        print("You have created a Mac checkbox.")


# Конкретный продукт B3 (дополнительный пример)
class LinuxCheckbox(Checkbox):
    def paint(self):
        print("You have created a Linux checkbox.")


# Интерфейс абстрактной фабрики
class GUIFactory:
    def create_button(self):
        raise NotImplementedError("Метод create_button() должен быть реализован")

    def create_checkbox(self):
        raise NotImplementedError("Метод create_checkbox() должен быть реализован")


# Конкретная фабрика 1
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


# Конкретная фабрика 2
class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


# Конкретная фабрика 3 (дополнительный пример)
class LinuxFactory(GUIFactory):
    def create_button(self):
        return LinuxButton()

    def create_checkbox(self):
        return LinuxCheckbox()


# Клиентский код
class Application:
    def __init__(self, factory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def paint(self):
        self.button.paint()
        self.checkbox.paint()
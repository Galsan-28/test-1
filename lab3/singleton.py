class Singleton:
    # Приватное статическое поле для хранения единственного экземпляра
    _instance = None

    # Приватный конструктор, чтобы предотвратить создание экземпляров извне
    def __init__(self):
        if Singleton._instance is not None:
            raise Exception("Этот класс является Singleton! Используйте getInstance()")
        # Инициализация, если необходимо
        Singleton._instance = self
        self.data = "Singleton Data"

    # Статический метод для получения единственного экземпляра
    @staticmethod
    def get_instance():
        if Singleton._instance is None:
            Singleton._instance = Singleton()
        return Singleton._instance

    # Другие методы класса
    def some_method(self):
        print("Вызван метод some_method() экземпляра Singleton")
        return self.data


# Пример потокобезопасной версии Singleton
class ThreadSafeSingleton:
    _instance = None
    _lock = None  # В реальности был бы threading.Lock()

    def __init__(self):
        if ThreadSafeSingleton._instance is not None:
            raise Exception("Этот класс является Singleton!")
        ThreadSafeSingleton._instance = self

    @staticmethod
    def get_instance():
        if ThreadSafeSingleton._instance is None:
            # В многопоточном приложении здесь была бы блокировка
            if ThreadSafeSingleton._instance is None:
                ThreadSafeSingleton._instance = ThreadSafeSingleton()
        return ThreadSafeSingleton._instance


# Еще один пример Singleton - конфигурация приложения
class Configuration:
    _instance = None
    _config_data = {}

    def __init__(self):
        if Configuration._instance is not None:
            raise Exception("Используйте get_instance() для получения Configuration")
        Configuration._instance = self

    @staticmethod
    def get_instance():
        if Configuration._instance is None:
            Configuration._instance = Configuration()
        return Configuration._instance

    def set_config(self, key, value):
        self._config_data[key] = value

    def get_config(self, key):
        return self._config_data.get(key)

    def show_all_configs(self):
        return self._config_data.copy()
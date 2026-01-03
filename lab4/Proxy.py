from abc import ABC, abstractmethod


# Интерфейс предмета
class Database(ABC):
    @abstractmethod
    def query(self, sql: str):
        pass

    @abstractmethod
    def connect(self):
        pass


# Реальный субъект
class RealDatabase(Database):
    def __init__(self, database_name: str):
        self._database_name = database_name

    def connect(self):
        print(f"Подключаюсь к базе данных: {self._database_name}")

    def query(self, sql: str):
        print(f"Выполняю запрос: {sql}")
        # Здесь была бы реальная логика выполнения запроса
        return f"Результат запроса: '{sql}'"


# Прокси
class DatabaseProxy(Database):
    def __init__(self, database_name: str, user_role: str):
        self._real_database = RealDatabase(database_name)
        self._user_role = user_role
        self._cache = {}
        self._is_connected = False

    def connect(self):
        if not self._is_connected:
            self._real_database.connect()
            self._is_connected = True
        else:
            print("Уже подключено к базе данных")

    def query(self, sql: str):
        # Проверка прав доступа
        if self._user_role not in ["admin", "editor"] and "DELETE" in sql.upper():
            print(f"Ошибка: пользователь с ролью '{self._user_role}' не может выполнять DELETE запросы")
            return None

        # Кеширование
        if sql in self._cache:
            print(f"Возвращаю результат из кеша для запроса: {sql}")
            return self._cache[sql]

        # Выполнение запроса
        print(f"Прокси: проверка прав доступа для роли '{self._user_role}'")
        self.connect()
        result = self._real_database.query(sql)

        # Сохранение в кеше
        self._cache[sql] = result
        return result


# Пример использования
def demonstrate_proxy():
    print("\n=== Proxy Pattern ===")

    # Создаем прокси для разных пользователей
    admin_proxy = DatabaseProxy("MyDatabase", "admin")
    editor_proxy = DatabaseProxy("MyDatabase", "editor")
    viewer_proxy = DatabaseProxy("MyDatabase", "viewer")

    print("\n1. Администратор выполняет запросы:")
    print(admin_proxy.query("SELECT * FROM users"))
    print(admin_proxy.query("DELETE FROM users WHERE id = 1"))

    print("\n2. Редактор выполняет запросы:")
    print(editor_proxy.query("SELECT * FROM products"))
    # Повторный запрос - должен вернуть из кеша
    print(editor_proxy.query("SELECT * FROM products"))

    print("\n3. Зритель пытается выполнить DELETE:")
    result = viewer_proxy.query("DELETE FROM users WHERE id = 1")
    if result is None:
        print("Запрос был отклонен прокси")
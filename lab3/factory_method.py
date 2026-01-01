class Logger:
    def log(self, message):
        raise NotImplementedError("Метод log() должен быть реализован")


# Конкретный продукт: Файловый логгер
class FileLogger(Logger):
    def log(self, message):
        print(f"Logging to file: {message}")


# Конкретный продукт: Консольный логгер
class ConsoleLogger(Logger):
    def log(self, message):
        print(f"Logging to console: {message}")


# Конкретный продукт: База данных логгер (дополнительный пример)
class DatabaseLogger(Logger):
    def log(self, message):
        print(f"Logging to database: {message}")


# Создатель (фабрика)
class LoggerFactory:
    # Фабричный метод (абстрактный)
    def create_logger(self):
        raise NotImplementedError("Фабричный метод должен быть реализован")

    # Метод, использующий фабричный метод
    def log_message(self, message):
        logger = self.create_logger()
        logger.log(message)


# Конкретный создатель: Фабрика для файлового логгера
class FileLoggerFactory(LoggerFactory):
    def create_logger(self):
        return FileLogger()


# Конкретный создатель: Фабрика для консольного логгера
class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self):
        return ConsoleLogger()


# Конкретный создатель: Фабрика для базы данных логгера
class DatabaseLoggerFactory(LoggerFactory):
    def create_logger(self):
        return DatabaseLogger()
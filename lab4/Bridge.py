from abc import ABC, abstractmethod


# Реализация (Implementor)
class Device(ABC):
    @abstractmethod
    def is_enabled(self) -> bool:
        pass

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass

    @abstractmethod
    def get_volume(self) -> int:
        pass

    @abstractmethod
    def set_volume(self, percent: int):
        pass

    @abstractmethod
    def get_channel(self) -> int:
        pass

    @abstractmethod
    def set_channel(self, channel: int):
        pass


# Конкретные реализации
class TV(Device):
    def __init__(self):
        self._enabled = False
        self._volume = 50
        self._channel = 1
        self._max_channel = 100

    def is_enabled(self) -> bool:
        return self._enabled

    def enable(self):
        self._enabled = True
        print("TV: включен")

    def disable(self):
        self._enabled = False
        print("TV: выключен")

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, percent: int):
        if 0 <= percent <= 100:
            self._volume = percent
            print(f"TV: громкость установлена на {percent}%")
        else:
            print("TV: неверное значение громкости")

    def get_channel(self) -> int:
        return self._channel

    def set_channel(self, channel: int):
        if 1 <= channel <= self._max_channel:
            self._channel = channel
            print(f"TV: канал установлен на {channel}")
        else:
            print(f"TV: канал должен быть от 1 до {self._max_channel}")


class Radio(Device):
    def __init__(self):
        self._enabled = False
        self._volume = 30
        self._channel = 88  # FM частота
        self._min_channel = 88
        self._max_channel = 108

    def is_enabled(self) -> bool:
        return self._enabled

    def enable(self):
        self._enabled = True
        print("Radio: включен")

    def disable(self):
        self._enabled = False
        print("Radio: выключен")

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, percent: int):
        if 0 <= percent <= 100:
            self._volume = percent
            print(f"Radio: громкость установлена на {percent}%")
        else:
            print("Radio: неверное значение громкости")

    def get_channel(self) -> int:
        return self._channel

    def set_channel(self, channel: int):
        if self._min_channel <= channel <= self._max_channel:
            self._channel = channel
            print(f"Radio: частота установлена на {channel} FM")
        else:
            print(f"Radio: частота должна быть от {self._min_channel} до {self._max_channel} FM")


# Абстракция
class RemoteControl(ABC):
    def __init__(self, device: Device):
        self._device = device

    def toggle_power(self):
        if self._device.is_enabled():
            self._device.disable()
        else:
            self._device.enable()

    def volume_down(self):
        self._device.set_volume(self._device.get_volume() - 10)

    def volume_up(self):
        self._device.set_volume(self._device.get_volume() + 10)

    def channel_down(self):
        self._device.set_channel(self._device.get_channel() - 1)

    def channel_up(self):
        self._device.set_channel(self._device.get_channel() + 1)


# Расширенные абстракции
class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        self._device.set_volume(0)
        print("Удаленный режим: звук отключен")

    def set_channel(self, channel: int):
        self._device.set_channel(channel)
        print(f"Удаленный режим: установлен канал {channel}")


class VoiceRemoteControl(RemoteControl):
    def voice_command(self, command: str):
        command = command.lower()
        if "включи" in command:
            self._device.enable()
        elif "выключи" in command:
            self._device.disable()
        elif "громче" in command:
            self.volume_up()
        elif "тише" in command:
            self.volume_down()
        elif "канал" in command:
            # Извлекаем номер канала из команды
            for word in command.split():
                if word.isdigit():
                    self._device.set_channel(int(word))
                    break
        print(f"Голосовая команда: '{command}' выполнена")


# Пример использования
def demonstrate_bridge():
    print("\n=== Bridge Pattern ===")

    print("\n1. Базовый пульт для TV:")
    tv = TV()
    basic_remote = RemoteControl(tv)
    basic_remote.toggle_power()
    basic_remote.channel_up()
    basic_remote.volume_up()

    print("\n2. Продвинутый пульт для Radio:")
    radio = Radio()
    advanced_remote = AdvancedRemoteControl(radio)
    advanced_remote.toggle_power()
    advanced_remote.set_channel(95)
    advanced_remote.mute()

    print("\n3. Голосовой пульт для TV:")
    voice_remote = VoiceRemoteControl(tv)
    voice_remote.voice_command("Включи телевизор")
    voice_remote.voice_command("Переключи на канал 5")
    voice_remote.voice_command("Сделай громче")


# Главная функция для демонстрации всех паттернов
def main():
    demonstrate_strategy()
    demonstrate_chain_of_responsibility()
    demonstrate_iterator()
    demonstrate_proxy()
    demonstrate_adapter()
    demonstrate_bridge()


if __name__ == "__main__":
    main()
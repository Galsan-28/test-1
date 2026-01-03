# Целевой интерфейс
class MediaPlayer:
    def play(self, audio_type: str, filename: str):
        pass


# Адаптируемый класс 1
class AdvancedMediaPlayer:
    def play_vlc(self, filename: str):
        print(f"Playing vlc file: {filename}")

    def play_mp4(self, filename: str):
        print(f"Playing mp4 file: {filename}")


# Адаптируемый класс 2 (сторонняя библиотека)
class ThirdPartyAudioPlayer:
    def play_audio(self, file_path: str, format_code: int):
        formats = {1: "mp3", 2: "wav", 3: "aac"}
        format_name = formats.get(format_code, "unknown")
        print(f"Third party player: Playing {format_name} file: {file_path}")


# Адаптер для AdvancedMediaPlayer
class MediaAdapter(MediaPlayer):
    def __init__(self, audio_type: str):
        self._advanced_player = AdvancedMediaPlayer()
        self._audio_type = audio_type

    def play(self, audio_type: str, filename: str):
        if audio_type.lower() == "vlc":
            self._advanced_player.play_vlc(filename)
        elif audio_type.lower() == "mp4":
            self._advanced_player.play_mp4(filename)
        else:
            print(f"Unsupported format: {audio_type}")


# Адаптер для ThirdPartyAudioPlayer
class ThirdPartyPlayerAdapter(MediaPlayer):
    def __init__(self):
        self._third_party_player = ThirdPartyAudioPlayer()
        self._format_map = {
            "mp3": 1,
            "wav": 2,
            "aac": 3
        }

    def play(self, audio_type: str, filename: str):
        format_code = self._format_map.get(audio_type.lower())
        if format_code:
            self._third_party_player.play_audio(filename, format_code)
        else:
            print(f"Unsupported format by third party player: {audio_type}")


# Аудиоплеер, использующий адаптеры
class AudioPlayer(MediaPlayer):
    def play(self, audio_type: str, filename: str):
        if audio_type.lower() == "mp3":
            print(f"Playing mp3 file: {filename}")
        elif audio_type.lower() in ["vlc", "mp4"]:
            adapter = MediaAdapter(audio_type)
            adapter.play(audio_type, filename)
        elif audio_type.lower() in ["mp3", "wav", "aac"]:
            adapter = ThirdPartyPlayerAdapter()
            adapter.play(audio_type, filename)
        else:
            print(f"Invalid media type: {audio_type}")


# Пример использования
def demonstrate_adapter():
    print("\n=== Adapter Pattern ===")

    player = AudioPlayer()

    # Встроенная поддержка
    player.play("mp3", "song.mp3")

    # Через адаптер для AdvancedMediaPlayer
    player.play("vlc", "movie.vlc")
    player.play("mp4", "video.mp4")

    # Через адаптер для ThirdPartyAudioPlayer
    player.play("wav", "sound.wav")
    player.play("aac", "audio.aac")

    # Неподдерживаемый формат
    player.play("avi", "video.avi")
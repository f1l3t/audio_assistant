from pydub import AudioSegment
from pydub.playback import play


file_name = f"audio_{30120369810}.mp3"


song = AudioSegment.from_mp3(file_name)
play(song)
print(file_name)


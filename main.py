from youtube_transcript_api import YouTubeTranscriptApi
import translators as ts
from gtts import gTTS
from playsound import playsound


class Translate_Video:

    def __init__(self, videoID, video_language, language_to_hear):
        self.videoId = videoID
        self.video_language = video_language
        self.language_to_hear = language_to_hear

    def video_transcript(self):
        return YouTubeTranscriptApi.get_transcript(video_id=self.videoId, languages=[self.video_language])

    def get_transcript_arr(self):
        transcrip = self.video_transcript()
        textArr = []
        for i in range(len(transcrip)):
            textArr.append(transcrip[i]["text"])
        return textArr

    def get_translated_text(self):
        phrases = self.get_transcript_arr()
        newPhrases = []

        for i in range(len(phrases)):
            newPhrases.append(ts.translate_text(phrases[i], to_language=self.language_to_hear))
        return newPhrases


def play_sound(language_to_hear, translated_text, texts):
    for text, text2 in zip(translated_text, texts):
        tts = gTTS(text, lang=language_to_hear)
        tts.save('audio.mp3')
        print(f"Translated: {text}")
        print(f"original: {text2}")
        playsound('audio.mp3')


video = Translate_Video("w-kSRbJSiD8", "es", "en")

text = video.get_transcript_arr()
translated_text = video.get_translated_text()

play_sound("en", translated_text, text)
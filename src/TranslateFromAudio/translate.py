

from TranslateFromText.translate import translateText
from Voice_Text.audio_text import voiceToText
from Voice_Text.text_audio import textToAudio


def translateAudioToAudio(lang,translator,langOutput):
   text = voiceToText(lang)
   textTrans = translateText(text,lang,translator,langOutput)
   textToAudio(textTrans)
   
   
def translateAudioToText(lang,translator,langOutput):
    text = voiceToText(lang)
    textTrans = translateText(text,lang,translator,langOutput)
    return textTrans

def translateTextToAudio(text,lang,translator,langOutput):
    textTrans = translateText(text,lang,translator,langOutput)
    textToAudio(textTrans)

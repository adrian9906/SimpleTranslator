
from googletrans import Translator
from TranslateFromAudio.translate import translateTextToAudio
from TranslateFromText.translate import translateText

translator = Translator()
text = translateText("hola me llamo Adrian",'es',translator,'en')
translateTextToAudio()

print(text)
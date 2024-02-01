# SimpleTranslator
SimpleTranslator is a project that uses the Google Translation API to translate text from one language to another. This project can be useful for those who need to translate text in real time or for those who work with multiple languages and need a quick tool to translate text.

# Features
* Text to Text Translation: Translate text from one language to another.
* Audio to Text Translation: Convert spoken words in an audio file to written text.
* Text to Audio Translation: Convert written text to spoken words in audio.
* Audio to Audio Translation: Translate spoken words in one audio to another language in audio.

# Usage
Here's an example of how to use SimpleTraductor in Python:
```bash
from googletrans import Translator
from TranslateFromAudio.translate import translateTextToAudio
from TranslateFromText.translate import translateText

translator = Translator()
text = translateText("hola me llamo Adrian",'es',translator,'en')
translateTextToAudio()

print(text)
```
## Versioning 📌

[Git](https://git-scm.com) was used for versioning. For available versions, see the [tags in this repository](https://github.com/your/project/tags).


## License 📄

This project is under MIT license - see the file [LICENSE.md](https://github.com/adrian9906/SimpleTranslator/blob/main/LICENSE) for details

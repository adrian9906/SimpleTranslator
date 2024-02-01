

def detectLang(text,translator):
    detect = translator.detect(text)
    
    return detect.lang
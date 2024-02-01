

def translateText(text,langText,translator,langTrans):
    trasnlation = translator.translate(text,src=langText,dest=langTrans)
    
    return trasnlation.text
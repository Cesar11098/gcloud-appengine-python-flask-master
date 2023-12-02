from transformers import pipeline


def analizador_sentimiento(texto):
    sentiment_analyzer = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')
    resultado = sentiment_analyzer(texto)[0]
    sentimiento = resultado['label']
    return sentimiento
textoNegativo = "me quiero dar de baja de la vida"
textoPositivo = "hoy se gana"
textoNeutral = "Dios bendiga al profe Kevin"


sentimiento = analizador_sentimiento(textoNeutral)
print(f"Sentimiento: {sentimiento}\n")
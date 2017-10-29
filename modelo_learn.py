from dados import carregar_acessos
from sklearn.naive_bayes import MultinomialNB

x,y = carregar_acessos()

treino_dados = x[:90]
teste_dados = x[-9:]

treino_marc = y[:90]
teste_marc = y[-9:]


modelo = MultinomialNB()
modelo.fit(treino_dados,treino_marc)

resultado = modelo.predict(teste_dados)
diferenca = resultado - teste_marc

acertos = [d for d in diferenca if d == 0]
total_de_acertors = len(acertos)
total_de_elementos = len(teste_dados)
taxa_de_acerto = 100.0 * total_de_acertors/ total_de_elementos
print taxa_de_acerto
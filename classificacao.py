#Gordinho? Perninha Curta? Auau?

porco1 = [1,1,0]
porco2= [1,1,0]
porco3= [1,1,0]
cachorro1=[1,1,1]
cachorro2=[0,1,1]
cachorro3=[0,1,1]
misterioso= [1,1,1]
misterioso2=[1,0,0]
misterioso3=[0,0,1]

dados = [porco1,porco3,porco2,cachorro3,cachorro2,cachorro1]

marcacoes= [1,1,1,-1,-1,-1]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(dados,marcacoes)
testes = [misterioso,misterioso2,misterioso3]
marcacoes_teste = [-1,1,-1]
resultado = modelo.predict(testes)
print resultado

diferencas = resultado - marcacoes_teste
acertos = [d for d in diferencas if d ==0]
total_de_acertos= len(acertos)
total_de_elementos = len(testes)
taxa_de_acerto = 100* (total_de_acertos/total_de_elementos)
print taxa_de_acerto

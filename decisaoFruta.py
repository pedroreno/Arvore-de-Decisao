from sklearn import tree

#superficies
lisa      = 1
irregular = 2
longa     = 3
pontuda   = 4

#cores
vermelha    = 1
verde       = 2
amarela     = 3
laranjaCor  = 4

#resultados
maça         = 1
banana       = 2
laranjaFruta = 3
pessego      = 4
abacaxi      = 5

possibilidades = [[150, lisa, vermelha], [100, lisa, vermelha], [100, lisa, verde], [150, lisa, verde],      #maças
                  [80, longa, amarela], [100, longa, amarela],                                               #bananas
                  [150, irregular, laranjaCor], [200, irregular, laranjaCor],                                #laranjas
                  [200, lisa, vermelha], [230, lisa, vermelha], [200, lisa, amarela], [230, lisa, amarela],  #pessegos
                  [800, pontuda, amarela]]                                                                  #abacaxis

resultados = [maça, maça, maça, maça,
              banana, banana,
              laranjaFruta, laranjaFruta,
              pessego, pessego, pessego, pessego,
              abacaxi]



classificacao = tree.DecisionTreeClassifier()
classificacao = classificacao.fit(possibilidades, resultados)

peso = input("Qual é o peso da fruta? ")
superficie = input("Como é a superficie da fruta? "
                   "(1 = lisa, 2 = irregular, 3 = longa, 4 = pontuda)")
cor = input("Qual é a cor da fruta? "
            "(1 = vermelha, 2 = verde, 3 = amarela, 4 = laranja)")

resultadoFinal = classificacao.predict([[peso, superficie, cor]])


if resultadoFinal == 1:
    print("A fruta é maça")
if resultadoFinal == 2:
    print("A fruta é banana")
if resultadoFinal == 3:
    print("A fruta é laranja")
if resultadoFinal == 4:
    print("A fruta é pessego")
if resultadoFinal == 5:
    print("A fruta é abacaxi")

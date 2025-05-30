class Espisificacoes_Cards:
    def __init__(self, tipo, nivel, ataque, defesa):
        self.tipo = tipo
        self.nivel = nivel
        self.ataque = ataque
        self.defesa = defesa
        
    def atacar(self):
        print("ataque basico")
        print("ataque forte")
        print("super")

    def defender(self):
        print("parry")
        print("defesa normal")
        print("defesa + shield")
        print("break")

class Mago(Espisificacoes_Cards):

    def recuperar_mana(self):
        print("recuperou 25+ mana")
        print("pula o ataque")
    
    def atacar(self):
        tem_mana_paizao = 1000
        if tem_mana_paizao >= 2150:
            print("super")
        elif tem_mana_paizao == 1000:
            print("ataque forte")
        elif tem_mana_paizao <= 500:
            print("ataque basico")
    
    def defender(self):
        pontos_de_defesa = 2100
        if pontos_de_defesa == 2100:
            print("defesa + shield")
        elif pontos_de_defesa == 1000:
            print("defesa normal")
        elif pontos_de_defesa == 500:
            print ("parry(toma gap)")
        elif pontos_de_defesa == 950:
            print ("break")

class Barbaro(Espisificacoes_Cards):
    def ugauga(self):
        print("curou 100 de vida")
        print("pulo a vez")

    def atacar(self):
        pontos_de_forca = 2500
        if pontos_de_forca >= 2150:
            print("super")
        elif pontos_de_forca == 1500:
            print("ataque forte")
        elif pontos_de_forca <= 500:
            print("ataque basico")

    def defender(self):
        pontos_de_defesa = 2000
        if pontos_de_defesa == 2000:
            print("defesa + shield")
        elif pontos_de_defesa == 9000:
            print("defesa normal")
        elif pontos_de_defesa == 400:
            print ("parry(toma gap)")
        elif pontos_de_defesa == 850:
            print ("break")


jogador1 = Mago("feiticeiro", 7, 2500, 2100)
jogador2 = Barbaro("Normal", 7, 2500, 2000)

jogador1.atacar()






        

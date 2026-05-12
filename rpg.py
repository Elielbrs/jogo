import random
import time

def pausar (segundos=1.0):
    time.sleep (segundos)

def separacao ():
    print ("=" * 30)

def titulo (texto):
    separacao ()
    print (texto.center (30))
    separacao ()

class personagem:
    def __init__ (self, nome, hp, ataque, defesa, nivel=1):
        self.nome = nome
        self.hp = hp
        self.hp_max = hp
        self.ataque = ataque
        self.defesa = defesa
        self.nivel = nivel

def esta_vivo (personagem):
    return personagem.hp > 0

def receber_dano (personagem, dano):
    dano_real = max (1, dano - personagem.defesa)
    personagem.hp = max (0, personagem.hp - dano_real)
    print (f"{personagem.nome} recebeu {dano_real} de dano! HP restante: {personagem.hp}/{personagem.hp_max}")
    if personagem.hp <= 0:
        print (f"{personagem.nome} foi derrotado!")

def atacar (personagem, alvo):
    dano = personagem.ataque + random.randint (-3, 5)
    print (f"{personagem.nome} ataca {alvo.nome}!")
    pausar ()
    receber_dano (alvo, dano)

def exibir_hp (personagem):
    proporcao = personagem.hp / personagem.hp_max
    barras = int (proporcao * 20)
    barra = "█" * barras + "░" * (20 - barras)
    print (f"{personagem.nome}: {personagem.hp}/{personagem.hp_max} HP")
    print (f"[{barra}]")

class heroi (personagem):
    def __init__ (self, nome, classe):

        stats = {
            "Guerreiro": {"hp": 120, "ataque": 15, "defesa": 10},
            "Mago": {"hp": 80, "ataque": 20, "defesa": 5},
            "Arqueiro": {"hp": 100, "ataque": 18, "defesa": 8}
        }

        s = stats[classe]
        super().__init__(nome, s["hp"], s["ataque"], s["defesa"])
        self.classe = classe
        self.experiencia = 0
        self.nivel = 1
        self.pocoes = 3
        self.habilidade_usada = False

def usar_pocao (heroi):
    if heroi.pocoes > 0:
        cura = random.randint (20, 40)
        heroi.hp = min (heroi.hp, heroi.hp_max + cura)
        heroi.pocoes -= 1
        print (f"{heroi.nome} usou uma poção e recuperou {cura} HP! HP atual: {heroi.hp}/{heroi.hp_max}")
    else:
        print (f"{heroi.nome} não tem poções restantes!")

def usar_habilidade (heroi, inimigo):
    if heroi.habilidade_usada:
        print (f"{heroi.nome} já usou sua habilidade especial nesta batalha!")
        return
        
        self.habilidade_usada = True

    if heroi.classe == "Guerreiro":
        dano = heroi.ataque * 2 + random.randint (5, 10)
        print (f"{heroi.nome} usa Golpe Poderoso!")
        pausar ()
        receber_dano (inimigo, dano)
        return dano


    elif heroi.classe == "Mago":
        dano = heroi.ataque * 2 + random.randint (10, 15)
        inimigo.hp = max (0, inimigo.hp - dano)
        print (f"{heroi.nome} conjura Bola de Fogo!")
        pausar ()
        receber_dano (inimigo, dano)
        return dano

    elif heroi.classe == "Arqueiro":
        total = 0
        print (f"{heroi.nome} dispara uma chuva de flechas!")
        for i in range (3):
            dano = heroi.ataque + random.randint (-2, 3)
            dano_cauasdo = inimigo.receber_dano (dano)
            total += dano_cauasdo
        print (f"{heroi.nome} acertou {total} de dano com a chuva de flechas!")
        pausar ()
        return total
    
def ganhar_experiencia (self, xp):
    self.experiencia += xp
    limite = self.nivel * 100
    if self.experiencia >= limite:
        self.nivel += 1
        self.experiencia -= limite
        self.hp_max += 20
        self.hp = self.hp_max
        self.ataque += 5
        self.defesa += 3
        self.pocoes += 1
        print (f"{self.nome} subiu para o nível {self.nivel}!")
        print (f"HP máximo aumentado para {self.hp_max}, ataque para {self.ataque}, defesa para {self.defesa} e poções para {self.pocoes}.")
        pausar ()

class inimigo (personagem):

    TIPOS = [
        {"nome": "Goblin", "hp": 50, "ataque": 10, "defesa": 5, "xp": 20},
        {"nome": "Orc", "hp": 80, "ataque": 15, "defesa": 8, "xp": 40},
        {"nome": "Minotauro", "hp": 100, "ataque": 18, "defesa": 10, "xp": 50},
        {"nome": "Troll", "hp": 120, "ataque": 20, "defesa": 12, "xp": 60},
        {"nome": "Dragão Supremo", "hp": 200, "ataque": 30, "defesa": 20, "xp": 100}
    ]

    def __init__ (self,nivel_heroi):
        peso = min (nivel_heroi, len (self.TIPOS))
        indice = random.randint (0, peso - 1)
        tipo = self.TIPOS[indice]

        fator = 1 + (nivel_heroi - 1) * 0.15
        hp_escalado = int (tipo["hp"] * fator)
        ataque_escalado = int (tipo["ataque"] * fator)
        defesa_escalada = int (tipo["defesa"] * fator)

        super().__init__(tipo["nome"], hp_escalado, ataque_escalado, defesa_escalada)
        self.experiencia = tipo["xp"]

def exibir_status_batalha (heroi, inimigo):
    print ("\nStatus da Batalha:")
    separacao ()
    exibir_hp (heroi)
    exibir_hp (inimigo)
    separacao ()

def turno_inimigo (inimigo, heroi):
    pausar ()
    if random.random () < 0.2:
        dano_base = random.randint (inimigo.ataque - 5, inimigo.ataque + 5)
        dano = heroi.receber_dano (dano_base)
        print (f"{inimigo.nome} usou um ataque especial!")
    else:
        dano_base = random.randint (inimigo.ataque - 3, inimigo.ataque + 3)
        dano = heroi.receber_dano (dano_base)
        print (f"{inimigo.nome} ataca e causa {dano} de dano em {heroi.nome}!")

def batalha (heroi, inimigo):
    titulo (f"BATALHA: {heroi.nome} vs {inimigo.nome}")
    heroi.habilidade_usada = False
    turno = 1

    while esta_vivo (heroi) and esta_vivo (inimigo):
        print (f"\n--- Turno {turno} ---")
        exibir_status_batalha (heroi, inimigo)

        print ("\nEscolha uma ação:")
        print ("1. Atacar")
        print ("2. Usar Habilidade Especial")
        print (f"3. Usar Poção ({heroi.pocoes}) restantes)")
        print ("4. Fugir")

        while True:
            escolha = input ("\nDigite o número da ação: ")
            if escolha in ["1", "2", "3", "4"]:
                break
            else:
                print ("Ação inválida! Tente novamente.")

            print ()

        if escolha == "1":
            dano = atacar (heroi, inimigo)
            print (f"{heroi.nome} causou {dano} de dano em {inimigo.nome}!")
        elif escolha == "2":
            dano = usar_habilidade (heroi, inimigo)
            if dano and dano > 0:
                print (f"{heroi.nome} causou {dano} de dano com a habilidade especial em {inimigo.nome}!")
        elif escolha == "3":
            usar_pocao (heroi)
        elif escolha == "4":
            if random.random () < 0.4:
                print ("Você conseguiu fugir da batalha!")
                pausar ()
                return "fugiu"
            else:
                print (f"{heroi.nome} tentou fugir, mas falhou!")
        else:
            print ("Ação inválida! Tente novamente.")
            continue

        if esta_vivo (inimigo):
            turno_inimigo (inimigo, heroi)
        else:
            print (f"{heroi.nome} venceu a batalha contra {inimigo.nome}!")
            pausar ()

        turno += 1

        if heroi.esta_vivo ():
            print (f"{heroi.nome} sobreviveu à batalha!")
            heroi.ganhar_experiencia (inimigo.experiencia)
            return "vitoria"
        else:
            print (f"{heroi.nome} foi derrotado por {inimigo.nome}...")
            return "derrota"
        
def menu_principal():
    titulo ("RPG - A JORNADA DE ELDORIA")

    print("""
            Bem-vindo a Eldoria, um mundo de magia, aventura e perigos!
            Escolha seu herói e prepare-se para enfrentar monstros, explorar masmorras
            e se tornar uma lenda!
    """)

    pausar (0.5)

    while True:
        nome = input ("Digite o nome do seu herói: ").strip ()
        if nome:
            break
        print ("O nome não pode ser vazio! Tente novamente.")

        separacao ()
    print ("\nEscolha a classe do seu herói:")
    print ("1. Guerreiro - Forte e resistente, especializado em combate corpo a corpo.")
    print ("2. Mago - Mestre das artes arcanas, capaz de conjurar feitiços poderosos.")
    print ("3. Arqueiro - Ágil e preciso, especialista em ataques à distância.")

    classes = {"1": "Guerreiro", "2": "Mago", "3": "Arqueiro"}
    while True:
        escolha = input ("\nDigite o número da classe: ").strip ()
        if escolha in classes:
            classe = classes[escolha]
            break
        print ("Escolha inválida! Tente novamente.")

        classe = classes[escolha]
        heroi = heroi (nome, classe)

        separacao ()
    print (f"\n{heroi.nome} o {heroi.classe} foi criado com sucesso!")
    print (f"HP: {heroi.hp}, Ataque: {heroi.ataque}, Defesa: {heroi.defesa}, Poções: {heroi.pocoes}")
    pausar (1.5)

    return heroi

def exibiir_status_heroi (heroi):
    titulo ("STATUS DO HERÓI")
    print (f"Nome: {heroi.nome}")
    print (f"Classe: {heroi.classe}")
    print (f"Nível: {heroi.nivel}")
    print (f"Experiência: {heroi.experiencia}/{heroi.nivel * 100}")
    print (f"HP: {heroi.hp}/{heroi.hp_max}")
    print (f"Ataque: {heroi.ataque}")
    print (f"Defesa: {heroi.defesa}")
    print (f"Poções restantes: {heroi.pocoes}")

def menu_explorar (heroi):
    while True:
        titulo ("EXPLORAR ELDORIA")
        print ("""
            Você está em uma vila pacífica, mas rumores de monstros nas redondezas
            estão se espalhando. O que você deseja fazer?
        """)

        print ("1. Explorar a floresta próxima (enfrentar monstros)")
        print ("2. Descansar na taverna (recuperar 100% HP e ganhar 1 poção)")
        print ("3. Ver status do herói")
        print ("4. Sair do jogo")

        opcao = input ("\nDigite o número da ação: ").strip ()

        

        if opcao == "1":
            return "explorar"
        elif opcao == "2":
            return "descansar"
        elif opcao == "3":
            exibiir_status_heroi (heroi)
        elif opcao == "4":
            return "sair"
        else:
            print ("Opção inválida! Tente novamente.")
            pausar (1.5)


def gamer_over(heroi, batalhas_vencidas):
    titulo ("GAME OVER")
    print ("""
        Sua jornada em Eldoria chegou ao fim. Mas não desanime, aventureiro!
        Cada derrota é uma oportunidade de aprender e crescer mais forte.
        Volte para a vila, prepare-se melhor e tente novamente!
    """)

    print (f" {heroi.nome}, o {heroi.classe}, caiu...")
    print (f"Você alcançou o nível {heroi.nivel} e acumulou {heroi.experiencia} de experiência.")
    print (f"{batalhas_vencidas} batalhas vencidas.")

    pausar (2.5)
    separacao ()


def tela_vitoria(heroi, batalhas_vencidas):
    """Tela exibida ao completar o jogo."""
    titulo("   🏆  VITÓRIA  🏆   ")
    print(f"\n  {heroi.nome} derrotou o Dragão Negro e salvou Eldoria!")
    print(f"\n  📊 RESULTADOS FINAIS:")
    print(f"     Nível alcançado  : {heroi.nivel}")
    print(f"     Batalhas vencidas: {batalhas_vencidas}")
    separacao()

def jogar():
    heroi = menu_principal()

    batalhas_vencidas = 0
    descansos = False
    boss_derrotados = False

    while True:
        acao = menu_explorar (heroi)

        if acao == "explorar":
            descansos = False

            if batalhas_vencidas >= 5 and not boss_derrotados:
                print ("\nUm poderoso inimigo sombriu a floresta... É o Dragão Supremo!")
                pausar (2)
                inimigo = inimigo.__new__ (inimigo)
                personagem.__init__ (inimigo, "Dragão Supremo", 300, 40, 25)
                inimigo.experiencia = 150
            else:
                inimigo = inimigo (heroi.nivel)

            resultado = batalha (heroi, inimigo)

            if resultado == "vitoria":
                batalhas_vencidas += 1
                if inimigo.nome == "Dragão Supremo":
                    boss_derrotados = True
                    tela_vitoria (heroi, batalhas_vencidas)
            elif resultado == "derrota":
                gamer_over (heroi, batalhas_vencidas)
                break

        elif acao == "descansar":
            if not descansos:
                heroi.hp = heroi.hp_max
                heroi.pocoes += 1
                print (f"\n{heroi.nome} descansou na taverna e recuperou HP e ganhou 1 poção!")
                descansos = True
            else:
                print ("\nVocê já descansou recentemente! Explore um pouco mais antes de descansar novamente.")

                pausar ()

        elif acao == "sair":
            print ("\nObrigado por jogar! Até a próxima aventura em Eldoria!")
            break

        print ("\n Jogar novamente? (s/n)").strip ().lower ()
        resposta = input ()
        if resposta != "s":
            print ("\nObrigado por jogar! Até a próxima aventura em Eldoria!")
            break

if __name__ == "__main__":
    jogar ()



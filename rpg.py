import random
import time


def pausar(segundos=1.0):
    # Pausa a execução por um tempo especificado
    time.sleep(segundos)


def separacao():
    # Exibe uma linha de separação
    print("=" * 30)


def titulo(texto):
    # Exibe um título centralizado com separadores
    separacao()
    print(texto.center(30))
    separacao()


# ─────────────────────────────────────────
# Classes
# ─────────────────────────────────────────

class Personagem:
    # Classe base para personagens do jogo (heróis e inimigos)
    def __init__(self, nome, hp, ataque, defesa, nivel=1):
        self.nome = nome
        self.hp = hp
        self.hp_max = hp
        self.ataque = ataque
        self.defesa = defesa
        self.nivel = nivel

    def esta_vivo(self):
        # Verifica se o personagem está vivo
        return self.hp > 0

    def receber_dano(self, dano):
        # Aplica dano ao personagem considerando sua defesa
        dano_real = max(1, dano - self.defesa)
        self.hp = max(0, self.hp - dano_real)
        print(f"{self.nome} recebeu {dano_real} de dano! HP restante: {self.hp}/{self.hp_max}")
        if self.hp <= 0:
            print(f"{self.nome} foi derrotado!")
        return dano_real

    def exibir_hp(self):
        # Exibe a barra de vida do personagem
        proporcao = self.hp / self.hp_max
        barras = int(proporcao * 20)
        barra = "█" * barras + "░" * (20 - barras)
        print(f"{self.nome}: {self.hp}/{self.hp_max} HP")
        print(f"[{barra}]")

    def atacar(self, alvo):
        # Realiza um ataque contra um alvo
        dano = self.ataque + random.randint(-3, 5)
        print(f"{self.nome} ataca {alvo.nome}!")
        pausar()
        alvo.receber_dano(dano)
        return dano


class Heroi(Personagem):
    # Classe que representa o herói jogável com habilidades especiais

    STATS = {
        "Guerreiro": {"hp": 120, "ataque": 15, "defesa": 10},
        "Mago":      {"hp": 80,  "ataque": 20, "defesa": 5},
        "Arqueiro":  {"hp": 100, "ataque": 18, "defesa": 8},
    }

    def __init__(self, nome, classe):
        s = self.STATS[classe]
        super().__init__(nome, s["hp"], s["ataque"], s["defesa"])
        self.classe = classe
        self.experiencia = 0
        self.pocoes = 3
        self.habilidade_usada = False

    def usar_pocao(self):
        # Usa uma poção para recuperar HP
        if self.pocoes > 0:
            cura = random.randint(20, 40)
            self.hp = min(self.hp + cura, self.hp_max)
            self.pocoes -= 1
            print(f"{self.nome} usou uma poção e recuperou {cura} HP! HP atual: {self.hp}/{self.hp_max}")
        else:
            print(f"{self.nome} não tem poções restantes!")

    def usar_habilidade(self, inimigo):
        # Usa a habilidade especial do herói baseada em sua classe
        if self.habilidade_usada:
            print(f"{self.nome} já usou sua habilidade especial nesta batalha!")
            return 0

        self.habilidade_usada = True

        if self.classe == "Guerreiro":
            dano = self.ataque * 2 + random.randint(5, 10)
            print(f"{self.nome} usa Golpe Poderoso!")
            pausar()
            inimigo.receber_dano(dano)
            return dano

        elif self.classe == "Mago":
            dano = self.ataque * 2 + random.randint(10, 15)
            print(f"{self.nome} conjura Bola de Fogo!")
            pausar()
            inimigo.receber_dano(dano)
            return dano

        elif self.classe == "Arqueiro":
            total = 0
            print(f"{self.nome} dispara uma chuva de flechas!")
            for _ in range(3):
                dano = self.ataque + random.randint(-2, 3)
                dano_causado = inimigo.receber_dano(dano)
                total += dano_causado
            print(f"{self.nome} acertou {total} de dano no total!")
            pausar()
            return total

        return 0

    def ganhar_experiencia(self, xp):
        # Adiciona experiência e gerencia o avanço de nível
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
            print(f"{self.nome} subiu para o nível {self.nivel}!")
            print(
                f"HP máximo: {self.hp_max} | Ataque: {self.ataque} "
                f"| Defesa: {self.defesa} | Poções: {self.pocoes}"
            )
            pausar()

    def exibir_status(self):
        # Exibe o status completo do herói
        titulo("STATUS DO HERÓI")
        print(f"Nome      : {self.nome}")
        print(f"Classe    : {self.classe}")
        print(f"Nível     : {self.nivel}")
        print(f"Experiência: {self.experiencia}/{self.nivel * 100}")
        print(f"HP        : {self.hp}/{self.hp_max}")
        print(f"Ataque    : {self.ataque}")
        print(f"Defesa    : {self.defesa}")
        print(f"Poções    : {self.pocoes}")


class Inimigo(Personagem):
    # Classe que representa um inimigo com atributos escalados

    TIPOS = [
        {"nome": "Goblin",        "hp": 50,  "ataque": 10, "defesa": 5,  "xp": 20},
        {"nome": "Orc",           "hp": 80,  "ataque": 15, "defesa": 8,  "xp": 40},
        {"nome": "Minotauro",     "hp": 100, "ataque": 18, "defesa": 10, "xp": 50},
        {"nome": "Troll",         "hp": 120, "ataque": 20, "defesa": 12, "xp": 60},
        {"nome": "Dragão Supremo","hp": 200, "ataque": 30, "defesa": 20, "xp": 100},
    ]

    def __init__(self, nivel_heroi):
        peso = min(nivel_heroi, len(self.TIPOS))
        indice = random.randint(0, peso - 1)
        tipo = self.TIPOS[indice]

        fator = 1 + (nivel_heroi - 1) * 0.15
        hp_escalado     = int(tipo["hp"]     * fator)
        ataque_escalado = int(tipo["ataque"] * fator)
        defesa_escalada = int(tipo["defesa"] * fator)

        super().__init__(tipo["nome"], hp_escalado, ataque_escalado, defesa_escalada)
        self.xp = tipo["xp"]

    def turno(self, heroi):
        # Executa o turno do inimigo atacando o herói
        pausar()
        if random.random() < 0.2:
            print(f"{self.nome} usou um ataque especial!")
            dano_base = random.randint(self.ataque - 5, self.ataque + 5)
        else:
            dano_base = random.randint(self.ataque - 3, self.ataque + 3)
        dano = heroi.receber_dano(dano_base)
        if not (random.random() < 0.2):
            print(f"{self.nome} atacou e causou {dano} de dano em {heroi.nome}!")


# ─────────────────────────────────────────
# Batalha
# ─────────────────────────────────────────

def exibir_status_batalha(heroi, mob):
    # Exibe o status de vida de ambos os combatentes
    print("\nStatus da Batalha:")
    separacao()
    heroi.exibir_hp()
    mob.exibir_hp()
    separacao()


def batalha(heroi, mob):
    # Gerencia o sistema de combate entre o herói e um inimigo
    titulo(f"BATALHA: {heroi.nome} vs {mob.nome}")
    heroi.habilidade_usada = False
    turno = 1

    while heroi.esta_vivo() and mob.esta_vivo():
        print(f"\n--- Turno {turno} ---")
        exibir_status_batalha(heroi, mob)

        print("\nEscolha uma ação:")
        print("1. Atacar")
        print("2. Usar Habilidade Especial")
        print(f"3. Usar Poção ({heroi.pocoes} restantes)")
        print("4. Fugir")

        while True:
            escolha = input("\nDigite o número da ação: ").strip()
            if escolha in ["1", "2", "3", "4"]:
                break
            print("Ação inválida! Tente novamente.")

        print()

        if escolha == "1":
            dano = heroi.atacar(mob)
            print(f"{heroi.nome} causou {dano} de dano em {mob.nome}!")

        elif escolha == "2":
            dano = heroi.usar_habilidade(mob)
            if dano and dano > 0:
                print(f"Habilidade causou {dano} de dano em {mob.nome}!")

        elif escolha == "3":
            heroi.usar_pocao()

        elif escolha == "4":
            if random.random() < 0.4:
                print("Você conseguiu fugir da batalha!")
                pausar()
                return "fugiu"
            else:
                print(f"{heroi.nome} tentou fugir, mas falhou!")

        if mob.esta_vivo():
            mob.turno(heroi)

        turno += 1

    if heroi.esta_vivo():
        print(f"\n{heroi.nome} venceu a batalha contra {mob.nome}!")
        pausar()
        heroi.ganhar_experiencia(mob.xp)
        return "vitoria"
    else:
        print(f"\n{heroi.nome} foi derrotado por {mob.nome}...")
        pausar()
        return "derrota"


# ─────────────────────────────────────────
# Menus e fluxo principal
# ─────────────────────────────────────────

def menu_principal():
    # Menu inicial onde o jogador cria seu herói
    titulo("RPG - A JORNADA DE ELDORIA")
    print("""
    Bem-vindo a Eldoria, um mundo de magia, aventura e perigos!
    Escolha seu herói e prepare-se para enfrentar monstros,
    explorar masmorras e se tornar uma lenda!
    """)
    pausar(0.5)

    while True:
        nome = input("Digite o nome do seu herói: ").strip()
        if nome:
            break
        print("O nome não pode ser vazio! Tente novamente.")

    separacao()
    print("\nEscolha a classe do seu herói:")
    print("1. Guerreiro - Forte e resistente, especializado em combate corpo a corpo.")
    print("2. Mago      - Mestre das artes arcanas, capaz de conjurar feitiços poderosos.")
    print("3. Arqueiro  - Ágil e preciso, especialista em ataques à distância.")

    classes = {"1": "Guerreiro", "2": "Mago", "3": "Arqueiro"}
    while True:
        escolha = input("\nDigite o número da classe: ").strip()
        if escolha in classes:
            classe = classes[escolha]
            break
        print("Escolha inválida! Tente novamente.")

    protagonista = Heroi(nome, classe)

    separacao()
    print(f"\n{protagonista.nome} o {protagonista.classe} foi criado com sucesso!")
    print(
        f"HP: {protagonista.hp} | Ataque: {protagonista.ataque} "
        f"| Defesa: {protagonista.defesa} | Poções: {protagonista.pocoes}"
    )
    pausar(1.5)

    return protagonista


def menu_explorar(heroi):
    # Menu de exploração onde o jogador escolhe suas ações
    while True:
        titulo("EXPLORAR ELDORIA")
        print("""
    Você está em uma vila pacífica. Rumores de monstros nas
    redondezas estão se espalhando. O que deseja fazer?
        """)
        print("1. Explorar a floresta próxima (enfrentar monstros)")
        print("2. Descansar na taverna (recuperar 100% HP e ganhar 1 poção)")
        print("3. Ver status do herói")
        print("4. Sair do jogo")

        opcao = input("\nDigite o número da ação: ").strip()

        if opcao == "1":
            return "explorar"
        elif opcao == "2":
            return "descansar"
        elif opcao == "3":
            heroi.exibir_status()
        elif opcao == "4":
            return "sair"
        else:
            print("Opção inválida! Tente novamente.")
            pausar(1.5)


def game_over(heroi, batalhas_vencidas):
    # Exibe a tela de derrota com estatísticas finais
    titulo("GAME OVER")
    print("""
    Sua jornada em Eldoria chegou ao fim. Mas não desanime!
    Cada derrota é uma oportunidade de crescer mais forte.
    """)
    print(f"  {heroi.nome}, o {heroi.classe}, caiu em batalha...")
    print(f"  Nível alcançado   : {heroi.nivel}")
    print(f"  Experiência final : {heroi.experiencia}")
    print(f"  Batalhas vencidas : {batalhas_vencidas}")
    pausar(2.5)
    separacao()


def tela_vitoria(heroi, batalhas_vencidas):
    # Exibe a tela de vitória após derrotar o chefe final
    titulo("🏆  VITÓRIA  🏆")
    print(f"\n  {heroi.nome} derrotou o Dragão Supremo e salvou Eldoria!")
    print(f"\n  RESULTADOS FINAIS:")
    print(f"     Nível alcançado  : {heroi.nivel}")
    print(f"     Batalhas vencidas: {batalhas_vencidas}")
    separacao()


def jogar():
    # Função principal que controla o fluxo do jogo
    heroi = menu_principal()

    batalhas_vencidas = 0
    ja_descansou = False
    boss_derrotado = False

    while True:
        acao = menu_explorar(heroi)

        if acao == "explorar":
            ja_descansou = False

            # Boss após 5 batalhas
            if batalhas_vencidas >= 5 and not boss_derrotado:
                print("\nUm poder sombrio emerge da floresta... É o Dragão Supremo!")
                pausar(2)
                mob = Inimigo.__new__(Inimigo)
                Personagem.__init__(mob, "Dragão Supremo", 300, 40, 25)
                mob.xp = 150
            else:
                mob = Inimigo(heroi.nivel)

            resultado = batalha(heroi, mob)

            if resultado == "vitoria":
                batalhas_vencidas += 1
                if mob.nome == "Dragão Supremo":
                    boss_derrotado = True
                    tela_vitoria(heroi, batalhas_vencidas)
                    break

            elif resultado == "derrota":
                game_over(heroi, batalhas_vencidas)
                break

        elif acao == "descansar":
            if not ja_descansou:
                heroi.hp = heroi.hp_max
                heroi.pocoes += 1
                print(f"\n{heroi.nome} descansou na taverna e recuperou todo o HP e ganhou 1 poção!")
                ja_descansou = True
            else:
                print("\nVocê já descansou recentemente! Explore mais antes de descansar novamente.")
            pausar()

        elif acao == "sair":
            print("\nObrigado por jogar! Até a próxima aventura em Eldoria!")
            break

    resposta = input("\nJogar novamente? (s/n): ").strip().lower()
    if resposta == "s":
        jogar()
    else:
        print("\nObrigado por jogar! Até a próxima aventura em Eldoria!")


if __name__ == "__main__":
    jogar()
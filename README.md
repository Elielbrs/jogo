# RPG - A Jornada de Eldoria 🏆

Um jogo de RPG em texto desenvolvido em Python, onde você cria um herói e enfrenta monstros em uma aventura épica pelo mundo de Eldoria!

## 📋 Descrição

Neste RPG, você cria seu próprio herói escolhendo entre três classes diferentes, explora a floresta enfrentando diversos inimigos, ganha experiência, sobe de nível e, eventualmente, desafia o Dragão Supremo como chefe final.

O jogo oferece um sistema completo de combate com escolhas estratégicas, itens (poções), habilidades especiais e progressão de personagem.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x** - Linguagem principal
- **Módulos Padrão**:
  - `random` - Para gerar valores aleatórios (dano, encontros, etc)
  - `time` - Para criar pausas e efeitos de timing no jogo

## 🎮 Como Jogar

### 1. **Iniciando o Jogo**

```bash
python rpg.py
```

### 2. **Criação do Herói**

- Digite o nome do seu herói
- Escolha uma das três classes:
  - **Guerreiro**: Alto HP e defesa, especializado em combate corpo a corpo
  - **Mago**: Menor HP, mas maior poder de ataque mágico
  - **Arqueiro**: Equilíbrio entre defesa e ataque

### 3. **Exploração**

No menu principal, você pode:

- **1. Explorar a floresta** - Enfrenta monstros aleatórios:
  - Goblin (fraco)
  - Orc (médio)
  - Minotauro (forte)
  - Troll (muito forte)
  - Dragão Supremo (chefe final - após 5 vitórias)

- **2. Descansar na taverna** - Recupera 100% de HP e ganha 1 poção (uma vez por ciclo)

- **3. Ver status** - Mostra seus atributos e progressão

- **4. Sair** - Encerra o jogo

### 4. **Sistema de Combate**

Durante uma batalha, você escolhe uma ação por turno:

- **1. Atacar** - Ataque básico com dano variável
- **2. Usar Habilidade Especial** (uma vez por batalha):
  - Guerreiro: Golpe Poderoso (2x dano)
  - Mago: Bola de Fogo (2x dano)
  - Arqueiro: Chuva de Flechas (3 ataques)
- **3. Usar Poção** - Recupera 20-40 HP
- **4. Fugir** - 40% de chance de sucesso

### 5. **Sistema de Progressão**

- **Experiência**: Ganha XP ao derrotar inimigos
- **Níveis**: A cada 100 XP, suba de nível e melhore seus atributos
- **Batalhas Vencidas**: Após 5 vitórias, o Dragão Supremo aparecerá
- **Escolha do Desafio**: Após 5 vitórias, você pode escolher quando enfrentar o dragão

### 6. **Vitória Final**

Derrote o Dragão Supremo para completar a jornada e ver os resultados finais!

## 📊 Mecânicas do Jogo

### Dano e Defesa
- Dano recebido = (Dano do atacante - Defesa) com mínimo de 1
- Cada classe tem defesa diferente

### Escalamento de Dificuldade
- Inimigos ficam mais fortes conforme seu nível aumenta
- O Dragão Supremo é o maior desafio com stats muito altos

### Habilidades Especiais
Cada classe tem uma habilidade única que pode ser usada uma vez por batalha:
- **Guerreiro**: Dobra seu ataque base + dano extra
- **Mago**: Dobra seu ataque base + dano extra (mais poderoso)
- **Arqueiro**: Realiza 3 ataques em sequência

## 🎯 Dicas para Vencer

1. Use poções estrategicamente durante o combate
2. Guarde a habilidade especial para momentos críticos
3. Fuja se estiver perdendo muito HP (40% de chance)
4. Suba de nível antes de enfrentar o Dragão Supremo
5. Descanse na taverna para recuperar vida entre batalhas

## 📁 Estrutura do Projeto

```
rpg.py
├── Funções utilitárias (pausar, separacao, titulo)
├── Classe Personagem (base para heróis e inimigos)
├── Classe Herói (jogável)
├── Classe Inimigo (adversários)
├── Sistema de Batalha
└── Menus e fluxo principal
```

## 🎓 Conceitos de Programação Utilizados

- **Programação Orientada a Objetos**: Classes e herança
- **Estruturas de Dados**: Dicionários e listas
- **Controle de Fluxo**: Loops, condicionais
- **Funções**: Modularização do código
- **Randomização**: Para criar variedade nas batalhas

## 📝 Exemplo de Gameplay

```
RPG - A JORNADA DE ELDORIA
==============================
Bem-vindo a Eldoria, um mundo de magia, aventura e perigos!
...
Digite o nome do seu herói: Aragorn
Escolha a classe do seu herói:
1. Guerreiro
2. Mago
3. Arqueiro
Digite o número da classe: 1

Aragorn o Guerreiro foi criado com sucesso!
HP: 120 | Ataque: 15 | Defesa: 10 | Poções: 3
```

## 🚀 Melhorias Futuras

- Sistema de inventário expandido
- Diferentes tipos de itens e equipamentos
- Múltiplos chefes de fase
- Sistema de save/load
- Interface gráfica
- Más mais para explorar

---

**Desenvolvido por**: Eliel  
**Linguagem**: Python  
**Versão**: 1.0  

Bom jogo! 🎮✨

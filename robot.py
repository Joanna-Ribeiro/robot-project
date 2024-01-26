class Parte():
    def __init__(self, nome: str, nivel_ataque=0, nivel_defesa=0, consumo_energia=0):
        self.nome = nome
        self.nivel_ataque = nivel_ataque
        self.nivel_defesa = nivel_defesa
        self.consumo_energia = consumo_energia

    def obter_dicionario_status(self):
        nome_formatado = self.nome.replace(" ", "_").lower()
        return {
            "{}_nome".format(nome_formatado): self.nome.upper(),
            "{}_status".format(nome_formatado): self.esta_disponivel(),
            "{}_ataque".format(nome_formatado): self.nivel_ataque,
            "{}_defesa".format(nome_formatado): self.nivel_defesa,
            "{}_consumo_energia".format(nome_formatado): self.consumo_energia,
        }

    def reduzir_edefesa(self, nivel_ataque):
        self.nivel_defesa = self.nivel_defesa - nivel_ataque
        if self.nivel_defesa <= 0:
            self.nivel_defesa = 0

    def esta_disponivel(self):
        return self.nivel_defesa <= 0

class Robo:
    def __init__(self, nome, codigo_cor):
        self.nome = nome
        self.codigo_cor = codigo_cor
        self.energia = 100
        self.partes = [
            Parte("Cabeça", nivel_ataque=5, nivel_defesa=10, consumo_energia=5),
            Parte("Arma", nivel_ataque=15, nivel_defesa=0, consumo_energia=10),
            Parte("Braço Esquerdo", nivel_ataque=3, nivel_defesa=20, consumo_energia=10),
            Parte("Braço Direito", nivel_ataque=6, nivel_defesa=20, consumo_energia=10),
            Parte("Perna Esquerda", nivel_ataque=4, nivel_defesa=20, consumo_energia=15),
            Parte("Perna Direita", nivel_ataque=8, nivel_defesa=20, consumo_energia=15),
        ]

    def imprimir_status(self):
        print(self.codigo_cor)
        str_robo = arte_robo.format(**self.obter_status_parte())
        self.cumprimentar()
        self.imprimir_energia()
        print(str_robo)
        print(cores["Branco"])

    def cumprimentar(self):
        print("Olá, meu nome é", self.nome)

    def imprimir_energia(self):
        print("Nós temos", self.energia, " por cento de energia restante")

    def obter_status_parte(self):
        status_parte = {}
        for parte in self.partes:
            dicionario_status = parte.obter_dicionario_status()
            status_parte.update(dicionario_status)
        return status_parte

    def existe_parte_disponivel(self):
        for parte in self.partes:
            if parte.esta_disponivel():
                return True
        return False

    def esta_ativo(self):
        return self.energia >= 0

    def atacar(self, robo_inimigo, parte_a_usar, parte_a_atacar):
        robo_inimigo.partes[parte_a_atacar].reduzir_edefesa(self.partes[parte_a_usar].nivel_ataque)
        self.energia -= self.partes[parte_a_usar].consumo_energia

arte_robo = r"""
      0: {cabeça_nome}
      Está disponível: {cabeça_status}
      Ataque: {cabeça_ataque}
      Defesa: {cabeça_defesa}
      Consumo de energia: {cabeça_consumo_energia}
              ^
              |                  |1: {arma_nome}
              |                  |Está disponível: {arma_status}
     ____     |    ____          |Ataque: {arma_ataque}
    |oooo|  ____  |oooo| ------> |Defesa: {arma_defesa}
    |oooo| '    ' |oooo|         |Consumo de energia: {arma_consumo_energia}
    |oooo|/\_||_/\|oooo|
    `----' / __ \  `----'           |2: {braço_esquerdo_nome}
   '/  |#|/\/__\/\|#|  \'           |Está disponível: {braço_esquerdo_status}
   /  \|#|| |/\| ||#|/  \           |Ataque: {braço_esquerdo_ataque}
  / \_/|_|| |/\| ||_|\_/ \          |Defesa: {braço_esquerdo_defesa}
 |_\/    O\=----=/O    \/_|         |Consumo de energia: {braço_esquerdo_consumo_energia}
 <_>      |=\__/=|      <_> ------> |
 <_>      |------|      <_>         |3: {braço_direito_nome}
 | |   ___|======|___   | |         |Está disponível: {braço_direito_status}
// \\ / |O|======|O| \  //\\        |Ataque: {braço_direito_ataque}
|  |  | |O+------+O| |  |  |        |Defesa: {braço_direito_defesa}
|\/|  \_+/        \+_/  |\/|        |Consumo de energia: {braço_direito_consumo_energia}
\__/  _|||        |||_  \__/
      | ||        || |          |4: {perna_esquerda_nome}
     [==|]        [|==]         |Está disponível: {perna_esquerda_status}
     [===]        [===]         |Ataque: {perna_esquerda_ataque}
      >_<          >_<          |Defesa: {perna_esquerda_defesa}
     || ||        || ||         |Consumo de energia: {perna_esquerda_consumo_energia}
     || ||        || || ------> |
     || ||        || ||         |5: {perna_direita_nome}
   __|\_/|__    __|\_/|__       |Está disponível: {perna_direita_status}
  /___n_n___\  /___n_n___\      |Ataque: {perna_direita_ataque}
                                |Defesa: {perna_direita_defesa}
                                |Consumo de energia: {perna_direita_consumo_energia}
"""

cores = {
    "Preto": '\x1b[90m',
    "Azul": '\x1b[94m',
    "Ciano": '\x1b[96m',
    "Verde": '\x1b[92m',
    "Magenta": '\x1b[95m',
    "Vermelho": '\x1b[91m',
    "Branco": '\x1b[97m',
    "Amarelo":'\x1b[93m',
}

def obter_status_parte(self):
    status_parte = {}
    for parte in self.partes:
        dicionario_status = parte.obter_dicionario_status()
        status_parte.update(dicionario_status)
    return status_parte

def construir_robo():
    nome_robo = input("Nome do Robô: ")
    codigo_cor = escolher_cor()
    robo = Robo(nome_robo, codigo_cor)
    robo.imprimir_status()
    return robo

def escolher_cor():
    cores_disponiveis = cores
    print("Cores disponíveis:")
    for chave, valor in cores_disponiveis.items():
        print(valor, chave)
    print(cores["Branco"])
    cor_escolhida = input("Escolha uma cor: ")
    codigo_cor = cores_disponiveis[cor_escolhida]
    return codigo_cor

def jogar():
    jogando = True
    print("Bem-vindo ao jogo!")
    print("Dados para o jogador 1:")
    robo_um = construir_robo()
    print("Dados para o jogador 2:")
    robo_dois = construir_robo()

    robo_atual = robo_um
    robo_inimigo = robo_dois
    rodada = 0

    while jogando:
        if rodada % 2 == 0:
            robo_atual = robo_um
            robo_inimigo = robo_dois
        else:
            robo_atual = robo_dois
            robo_inimigo = robo_um
        robo_atual.imprimir_status()
        print("Qual parte devo usar para atacar?:")
        parte_a_usar = input("Escolha um número de parte: ")
        parte_a_usar = int(parte_a_usar)

        robo_inimigo.imprimir_status()
        print("Qual parte do inimigo devemos atacar?")
        parte_a_atacar = input("Escolha um número de parte do inimigo para atacar: ")
        parte_a_atacar = int(parte_a_atacar)

        robo_atual.atacar(robo_inimigo, parte_a_usar, parte_a_atacar)
        rodada += 1
        if not robo_inimigo.esta_ativo() or robo_inimigo.existe_parte_disponivel() == False:
            jogando = False
            print("Parabéns, você venceu")

jogar()
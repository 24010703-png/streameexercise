import random

# 포켓몬 클래스 정의
class Pokemon:
    def __init__(self, name, type_, hp, attack, defense, moves):
        self.name = name
        self.type_ = type_
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.moves = moves

    def is_alive(self):
        return self.hp > 0

    def attack_target(self, move, target):
        damage = max(0, self.attack + move["power"] - target.defense)
        # 랜덤 보너스
        damage = int(damage * random.uniform(0.85, 1.15))
        target.hp -= damage
        if target.hp < 0:
            target.hp = 0
        print(f"{self.name}의 {move['name']}! {target.name}에게 {damage} 데미지!")
        print(f"{target.name} HP: {target.hp}/{target.max_hp}\n")

# 예시 포켓몬
pikachu = Pokemon(
    name="피카츄",
    type_="전기",
    hp=100,
    attack=20,
    defense=10,
    moves=[{"name": "전기쇼크", "power": 25}, {"name": "몸통박치기", "power": 15}]
)

charmander = Pokemon(
    name="파이리",
    type_="불",
    hp=100,
    attack=18,
    defense=12,
    moves=[{"name": "불꽃세례", "power": 22}, {"name": "할퀴기", "power": 18}]
)

# 배틀 진행
def battle(pokemon1, pokemon2):
    print("포켓몬 배틀 시작!\n")
    turn = 0
    while pokemon1.is_alive() and pokemon2.is_alive():
        if turn % 2 == 0:
            # 플레이어1 공격
            move = random.choice(pokemon1.moves)
            pokemon1.attack_target(move, pokemon2)
        else:
            # 플레이어2 공격
            move = random.choice(pokemon2.moves)
            pokemon2.attack_target(move, pokemon1)
        turn += 1

    if pokemon1.is_alive():
        print(f"{pokemon1.name} 승리!")
    else:
        print(f"{pokemon2.name} 승리!")

# 배틀 시작
battle(pikachu, charmander)




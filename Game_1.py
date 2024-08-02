import random

class Character:
    def __init__(self, name, health=100, attack=10):
        self.name = name
        self.health = health
        self.attack = attack
        self.inventory = []

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def attack_enemy(self, enemy):
        damage = random.randint(1, self.attack)
        enemy.take_damage(damage)
        print(f"{self.name} attacks {enemy.name} for {damage} damage.")

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{self.name} picked up {item.name}.")

class Item:
    def __init__(self, name):
        self.name = name

class Map:
    def __init__(self, size):
        self.size = size

class Game:
    def __init__(self):
        self.player = Character("Player")
        self.enemy = Character("Enemy", health=50, attack=8)
        self.map = Map(10)
        self.game_over = False

    def move_player(self):
        # In a real game, you would implement movement logic here
        print("Player moved.")

    def combat(self):
        while self.player.is_alive() and self.enemy.is_alive():
            self.player.attack_enemy(self.enemy)
            if self.enemy.is_alive():
                self.enemy.attack_enemy(self.player)
            if not self.enemy.is_alive():
                print("Enemy defeated.")
                break
            if not self.player.is_alive():
                print("Player defeated.")
                self.game_over = True
                break

    def pickup_item(self, item):
        self.player.add_to_inventory(item)

    def run(self):
        print("Welcome to the game!")
        while not self.game_over:
            command = input("Enter a command (move/attack/pickup/quit): ").lower()
            if command == "move":
                self.move_player()
            elif command == "attack":
                self.combat()
            elif command == "pickup":
                item = Item("Sword")
                self.pickup_item(item)
            elif command == "quit":
                print("Thanks for playing!")
                break
            else:
                print("Invalid command.")

if __name__ == "__main__":
    game = Game()
    game.run()

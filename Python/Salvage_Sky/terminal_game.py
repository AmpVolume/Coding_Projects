import random
import json
import os

# ---------------- SAVE / LOAD ----------------
def save_game(data):
    with open("save.json", "w") as f:
        json.dump(data, f)
    print("💾 Game saved!")

def load_game():
    if os.path.exists("save.json"):
        with open("save.json", "r") as f:
            return json.load(f)
    return None

# ---------------- ENEMIES ----------------
enemies = {
    "Crawler": {"hp": 30, "attack": (5, 10)},
    "Watcher": {"hp": 40, "attack": (8, 15)},
    "Void Beast": {"hp": 60, "attack": (10, 20)}
}

# ---------------- ITEMS ----------------
weapons = {
    "none": 0,
    "blade": 5,
    "void_sword": 10
}

artifacts = {
    "heart": {"effect": "heal", "value": 20},
    "core": {"effect": "power", "value": 5}
}

# ---------------- COMBAT ----------------
def combat(player):
    enemy_name = random.choice(list(enemies.keys()))
    enemy = enemies[enemy_name].copy()

    print(f"\n👾 A {enemy_name} appears!")

    while enemy["hp"] > 0 and player["health"] > 0:
        print(f"\n❤️ You: {player['health']} | 👾 {enemy_name}: {enemy['hp']}")
        print("1. Attack\n2. Block\n3. Heal")

        choice = input("> ")

        # --- ATTACK ---
        if choice == "1":
            dmg = random.randint(10, 15) + weapons[player["weapon"]]
            print(f"You deal {dmg} damage!")
            enemy["hp"] -= dmg

        # --- BLOCK ---
        elif choice == "2":
            print("You brace for impact (reduced damage).")

        # --- HEAL ---
        elif choice == "3":
            if "heart" in player["inventory"]:
                print("You use the Heart artifact (+20 HP)")
                player["health"] += 20
                player["inventory"].remove("heart")
            else:
                print("No healing item!")

        else:
            print("Invalid move.")
            continue

        # Enemy turn
        if enemy["hp"] > 0:
            dmg = random.randint(*enemy["attack"])

            if choice == "2":
                dmg //= 2

            print(f"The {enemy_name} hits you for {dmg}")
            player["health"] -= dmg

    if player["health"] > 0:
        print(f"\nYou defeated the {enemy_name}!")
        player["kills"] += 1
    else:
        print("\n💀 You were slain...")

# ---------------- GAME START ----------------
save = load_game()

if save:
    print("Load saved game? (yes/no)")
    if input("> ").lower() == "yes":
        player = save
    else:
        player = None
else:
    player = None

if not player:
    print("🌌 VOIDFALL 🌌")
    name = input("Enter your name: ")

    player = {
        "name": name,
        "health": 100,
        "weapon": "none",
        "inventory": [],
        "phase": 1,
        "cycle": "day",
        "turns": 0,
        "kills": 0,
        "night_turns": 0,
        "refused_escape": False
    }

print(f"\nWelcome, {player['name']}.")

# ---------------- GAME LOOP ----------------
while True:
    print("\n" + "-"*40)
    print(f"❤️ {player['health']} | Phase: {player['phase']} | {player['cycle'].upper()}")
    print("-"*40)

    # -------- PHASE 1 --------
    if player["phase"] == 1:
        print("\n1. Explore\n2. Search\n3. Rest\n4. Save Game")

        choice = input("> ")

        if choice == "1":
            if player["cycle"] == "night":
                combat(player)
            else:
                print("The island is calm.")

        elif choice == "2":
            loot = random.choice(["blade", "heart", "nothing"])
            if loot == "blade":
                print("You found a Blade! (+5 damage)")
                player["weapon"] = "blade"
            elif loot == "heart":
                print("You found a Heart artifact!")
                player["inventory"].append("heart")
            else:
                print("Nothing found.")

        elif choice == "3":
            if player["cycle"] == "day":
                print("You rest (+15 HP)")
                player["health"] += 15
            else:
                print("Too dangerous to rest.")

        elif choice == "4":
            save_game(player)

        # Transition to Phase 2
        if player["turns"] >= 5:
            print("\nThe fragment awakens...")
            print("You feel power surge through you.")
            player["phase"] = 2
            player["weapon"] = "void_sword"

    # -------- PHASE 2 --------
    else:
        print("\n1. Hunt\n2. Move\n3. Escape\n4. Save Game")

        choice = input("> ")

        if choice == "1":
            combat(player)

        elif choice == "2":
            print("Creatures avoid you...")

        elif choice == "3":
            print("\nA portal appears.")
            print("1. Enter\n2. Turn away")

            final = input("> ")

            if final == "1":
                print("You escaped... but something lingers.")
                break

            elif final == "2":
                player["refused_escape"] = True

                if player["kills"] >= 3 and player["night_turns"] >= 3:
                    print("\n🔥 VOID SLAYER ENDING 🔥")
                    print("They are trapped with you.")
                    break
                else:
                    print("Nothing happens...")

        elif choice == "4":
            save_game(player)

    # -------- CYCLE --------
    player["turns"] += 1

    if player["cycle"] == "day":
        player["cycle"] = "night"
        player["night_turns"] += 1
        print("\n🌑 Night falls...")
    else:
        player["cycle"] = "day"
        print("\n🌤 Day rises...")

    # -------- GAME OVER --------
    if player["health"] <= 0:
        print("\n💀 Game Over")
        break
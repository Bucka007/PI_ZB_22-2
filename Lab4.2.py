import random

def roll_dice():
    dice_value = random.randint(1, 6)
    print(f"Кубик: {dice_value}")

    if dice_value >= 5:
        print("Вы победили")
    elif dice_value >= 3:
        print("Получаем новое значение")
        roll_dice()
    else:
        print("Вы проиграли")

if __name__ == "__main__":
    roll_dice()
from card import Cards as divination


def start_divination():
    print("Привіт, я ворожка. Чи хочеш ти дізнатись відповідь на своє питання?")
    user_choice = input("Введи 'Так' чи 'Ні': ")

    while True:
        if user_choice == "Так":
            print("Галя, ти не виділа мої карти? Тут хочуть щоб я поворожила. О, знайшла!")
            return divination.cards_divination()
        elif user_choice == "Ні":
            break
        else:
            user_choice = input("Введи 'Так' чи 'Ні': ")


start_divination()

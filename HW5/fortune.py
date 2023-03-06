from card import Cards as divination

# consts
YES = "так"
NO = "ні"

print("Привіт, я ворожка.")
while True:
    print("Чи хочеш ти дізнатись відповідь на своє питання?")
    user_choice = input("Введи 'Так' чи 'Ні': ")
    if user_choice.lower().strip() == YES:
        print("Галя, ти не виділа мої карти? Тут хочуть щоб я поворожила. О, знайшла!")
        divination.cards_divination()
    elif user_choice.lower().strip() == NO:
        break
    else:
        print("Ти ввів щось неправильне")

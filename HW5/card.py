import itertools
import random
import time


class Cards:
    """Class for magic game with cards"""
    ranks = list(range(6, 10 + 1)) + list('JQKA')
    suits = {
        '\u2660',  # spades
        '\u2663',  # clubs
        '\u2665',  # hearts
        '\u2666'}  # diamonds

    @classmethod
    def cards_deck(cls):
        """Return full cards deck"""
        deck = list(itertools.product(cls.ranks, cls.suits))
        return deck

    @classmethod
    def random_card(cls):
        """Return one random card"""
        deck = list(itertools.product(cls.ranks, cls.suits))
        card = random.choice(deck)
        return f"{card[0]} {card[1]}"

    @staticmethod
    def wait_for_divination():

        for i in range(3):
            print("...")
            time.sleep(1)

    @staticmethod
    def cards_divination():
        one_card = Cards.random_card()

        user_desire = input("Отже, добре подумай та напиши своє найбажаніше питання, а я відповім чи збудеться воно. "
                            "\n \t Введи його сюди: ")

        print(f"У тебе випала така карта: {one_card}. Зачекай 3 секунди, потрібно добре обдумати.")

        Cards.wait_for_divination()

        if '\u2660' in one_card:  # if card is ♠
            if '6' in one_card:
                print("Стовідсотково ні! Також тебе чекають великі неприємності!!! Бережи себе.")
            else:
                print("Нажаль ні(")
        elif '\u2663' in one_card:  # if card is ♣
            print(
                "Швидше за все ні(. Але якщо ти будеш дуже старатись, то можливо й зможеш повернути "
                "фортуну у свій бік.")
        elif '\u2665' in one_card:  # if card is ♥
            if 'Q' in one_card:
                print("Тебе чекає велика удача. Однозначно так)))")
            else:
                print("Дуже вірогідно що це збудеться.")
        else:  # if card is ♦
            print("Можливо це й щбудеться! Але це не точно.")


if __name__ == '__main__':
    Cards()

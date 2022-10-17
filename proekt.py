from random import choice

items = {
    "камінь": "ножиці",
    "ножиці": "бумага",
    "бумага": "камінь"
}

player_score = 0
bot_score = 0


def main():
    global bot_score
    global player_score

    player_input = input("Камінь, ножиці або бумага?\n=> ").lower()

    if player_input not in items:
        print("Такого не має!")
        main()
    else:
        bot_input = choice("камінь/ножиці/бумага".split("/"))
        print(bot_input)

        if items[bot_input] == player_input:
            print("+1 очко боту")
            bot_score += 1
        else:
            print("+1 очко гравцю")
            player_score += 1

prv = player_score + bot_score == 3


    a = input("Продовжити? так/ні\n=>").lower()

    if a == "так":
            main()

    elif a == 'ні':
        print(str(bot_score) + " у бота")
        print(str(player_score) + " у гравця")

    if bot_score > player_score:
        print("Бот виграв!")
    elif bot_score < player_score:
        print("Гравець виграв!")
    else:
        print("Виграла дружба!")

main()

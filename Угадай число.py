import random
import time

def play_single_player():
    """Режим: угадай число, загаданное компьютером"""
    print("\n🎮 Режим: Угадай число (один игрок)")
    secret = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Твоё число (1-100): "))
            attempts += 1
            
            if guess < secret:
                print("📈 Больше!")
            elif guess > secret:
                print("📉 Меньше!")
            else:
                print(f"🎉 Поздравляю! Ты угадал число {secret} за {attempts} попыток!")
                break
        except ValueError:
            print("❌ Введи целое число!")

def play_vs_computer():
    """Режим: кто первый угадает случайное число"""
    print("\n🤖 Режим: Игрок vs Компьютер")
    print("Кто угадает загаданное число быстрее?")
    
    secret = random.randint(1, 50)
    print("🎯 Число загадано (1-50)!")
    
    # Ход игрока
    print("\n👤 Твой ход:")
    start_player = time.time()
    while True:
        try:
            guess = int(input("Твоя догадка: "))
            if guess == secret:
                player_time = time.time() - start_player
                print(f"✅ Ты угадал за {player_time:.1f} секунд!")
                break
            elif guess < secret:
                print("Больше!")
            else:
                print("Меньше!")
        except ValueError:
            print("Число, пожалуйста!")
    
    # Ход компьютера
    print("\n💻 Ход компьютера:")
    start_computer = time.time()
    low, high = 1, 50
    computer_guesses = 0
    
    while True:
        guess = random.randint(low, high)
        computer_guesses += 1
        print(f"Компьютер пробует: {guess}")
        time.sleep(0.5)
        
        if guess == secret:
            computer_time = time.time() - start_computer
            print(f"✅ Компьютер угадал за {computer_time:.1f} секунд!")
            break
        elif guess < secret:
            low = guess + 1
        else:
            high = guess - 1
    
    # Результат
    print("\n" + "="*30)
    if player_time < computer_time:
        print("🏆 Ты победил! Быстрее компьютера!")
    elif player_time > computer_time:
        print("💀 Компьютер победил... Попробуй ещё раз!")
    else:
        print("🤝 Ничья!")
    print(f"⏱️ Твоё время: {player_time:.1f} сек | Время компьютера: {computer_time:.1f} сек")

def guess_the_word():
    """Игра: угадай слово по буквам"""
    words = ["питон", "компьютер", "игра", "программирование", "алгоритм"]
    secret = random.choice(words)
    guessed = ["_"] * len(secret)
    attempts = 6
    
    print("\n📖 Игра: Угадай слово")
    print(f"Слово из {len(secret)} букв. У тебя {attempts} ошибок.")
    
    while attempts > 0 and "_" in guessed:
        print("\nСлово: " + " ".join(guessed))
        letter = input("Назови букву: ").lower()
        
        if len(letter) != 1 or not letter.isalpha():
            print("Введи одну русскую букву!")
            continue
        
        if letter in secret:
            print("✅ Есть такая буква!")
            for i, ch in enumerate(secret):
                if ch == letter:
                    guessed[i] = letter
        else:
            attempts -= 1
            print(f"❌ Нет такой буквы! Осталось попыток: {attempts}")
    
    if "_" not in guessed:
        print(f"\n🎉 Победа! Слово: {secret}")
    else:
        print(f"\n💀 Ты проиграл! Было загадано: {secret}")

def main():
    print("🎲 Добро пожаловать в сборник игр!")
    
    while True:
        print("\n" + "="*30)
        print("1️⃣ Угадай число (один игрок)")
        print("2️⃣ Соревнование с компьютером")
        print("3️⃣ Угадай слово по буквам")
        print("4️⃣ Выйти из игр")
        
        choice = input("Выбери игру: ").strip()
        
        if choice == "1":
            play_single_player()
        elif choice == "2":
            play_vs_computer()
        elif choice == "3":
            guess_the_word()
        elif choice == "4":
            print("👋 Спасибо за игру! До встречи!")
            break
        else:
            print("❌ Неверный выбор. Попробуй снова!")

if __name__ == "__main__":
    main()

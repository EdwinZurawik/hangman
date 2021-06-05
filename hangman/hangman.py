import random
import hangman_art as ha

words = [ 'first', 'second', 'four' ]

def main():
    end_game = False

    while not end_game:
        draw_menu()
        input("Press any key to exit.")
        end_game = True

def draw_menu():
    print(ha.hangman_title, ha.hangman_stages[-1])

def select_word(words):
    selected_word = random.choice(words)

if __name__ == '__main__':
    main()

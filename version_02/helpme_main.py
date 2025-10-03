from analyse import analyse_sentence; from random_msgs import *
from colorama import Fore, Style, init
init()

def help_me():
    print(f"{Fore.MAGENTA}{random_msgs1()}")
    
    answer = 'да'
    while answer.lower() == 'да':
        sentence = input(f"{Fore.MAGENTA}HelpMe:{Style.RESET_ALL} ")
        if sentence.lower() == 'да':
            continue
        elif sentence.lower() == 'нет':
            break
        
        analyse_sentence(sentence)
        sentence = input(f"\n{Fore.MAGENTA}Вам помогла цитата? 🙂 {Style.RESET_ALL}(да/нет) ")
        while ('нет' in sentence) or ('не' in sentence):
            analyse_sentence(sentence)
            sentence = input(f"\n{Fore.MAGENTA}А теперь помогла 😊 {Style.RESET_ALL}(да/нет) ? ")
        else:
            print(f"{Fore.MAGENTA}{random_msgs2()}{Style.RESET_ALL}")
        
        answer = input(f'\n{Fore.MAGENTA}🙂 Хотите продолжить сеанс? {Style.RESET_ALL}(да/нет) ')
    else:
        print(f"{Fore.MAGENTA}{random_msgs3()}")

if __name__ == '__main__':
    help_me()
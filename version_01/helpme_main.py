from analyse import analyse_sentence

def help_me():
    show_info(); answer = 'да'
    
    while answer.lower() == 'да':
        sentence = input('HelpMe: ')
        if sentence.lower() == 'да':
            continue
        elif sentence.lower() == 'нет':
            break
        
        analyse_sentence(sentence)
        
        answer = input('\n🙂 Хотите продолжить сеанс? (да/нет) ')
    else:
        print("Возвращайтесь, я всегда тут 😉")

def show_info():
    print("Готов поддержать вас цитатами в трудную минуту 🙂")

if __name__ == '__main__':
    help_me()
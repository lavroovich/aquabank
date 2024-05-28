#AquaBank-первый банк, работающий на PyCharm
#Файл what?.txt хранит в себе пароль, и текущий баланс пользователя.
import time

aquacore=open('what.txt','a+')
class safecore:
    def __init__(safe,passw,bal,fullname):
        safe.password=passw
        safe.balance=bal
        safe.name=fullname

    def deposit(safe):
        depos=(str(input("Введи число денег, которое ты хочешь положить себе на баланс, это безопасно\n")))
        depos=int(depos)
        safe.balance=(int(safe.balance))
        safe.balance+=depos
        safe.balance = (str(safe.balance))
        a.SaveDataToBober()
        depos=''
        time.sleep(2)
        print("Успешно!")
        time.sleep(1)
        a.menu()
    def changePassWithBober(safe):
        oldpass=input("Введи свой старый пароль ") #для смены (так всегда спрашиваю просто и я сделал)
        aquacore.seek(0)
        vernpass = aquacore.readline()
        if vernpass.strip() == oldpass:
            print("\nПроверено!")
            time.sleep(1)
            newpass=input("Введи новый пароль ")
            safe.password=newpass
            a.SaveDataToBober() #сохранение
            print("Идёт сохранение пароля в базе")
            time.sleep(2)
            print("Успешно!")
            exit(56)
        else:
            print("Пароль неверен! Вернём Вас в меню") #почему бы и нет?:)
            time.sleep(1)
            a.menu()
    def changeNameWithBober(safe):
        newname=input("Введи своё ФИО ")
        safe.name=newname
        a.SaveDataToBober()
        print("Сохраняем Ваше новое имя в базе")
        time.sleep(2)
        print("Успешно!")
        time.sleep(1)
        a.menu()
    def removeDataWithBober(safe):
        print("Это действие уничтожит АБСОЛЮТНО ВСЕ ДАННЫЕ с базы банка.")
        c=input("Выполнить данную команду? Y/N     (чуствительно к регистру)")
        if c=="Y":
            print("Сносим... Премичание: восстановить можно только обращением в банк, или прочитав документацию о проге")
            aquacore.truncate(0) #а всё, нет больше
            exit(56)
        else:
            print("Вернём тебя в меню...")
            time.sleep(1)
            a.menu()
    def SaveDataToBober(safe):
        aquacore.truncate(0) #чистит файл, старая информация исчезает
        aquacore.write(safe.password+'\n')#сохранение пароля
        aquacore.write(safe.balance+'\n')#сохранение баланса
        aquacore.write(safe.name+'\n')#сохранение имени
        #Да, в этой функции Я НЕ ИЩУ ЛЁГКИХ ПУТЕЙ!!!!
    def withdraw(safe):
        summa=input("Вводи число, которое снять с твоего счета ")
        summa=(int(summa))#всё в int, для вычисления
        safe.balance=(int(safe.balance))#тут тоже
        if safe.balance<summa:
            print("А, у тебя столько денег нет")
            time.sleep(3)
        else:
            safe.balance-=summa
            safe.balance=(str(safe.balance))
            a.SaveDataToBober()
            summa=''
            time.sleep(2)
            print("Успешно!")
            time.sleep(1)
            a.menu()
    def menu(safe):
        print('Добро пожаловать в AquaBank!')
        print('==================================')
        print("Сейчас у тебя на балансе:",safe.balance)
        print("Имя, зарегестрированное в банке:",safe.name)
        print("\n\nКоманды на изменение данных, указаны в дополнении")
        atputi=input()
        if atputi=="пополнить":
            print("Команда выбрана! Включаем режим вноса денег\n\n")
            a.deposit()
        elif atputi=='снять':
            print("Команда выбрана! Включаем режим снятия деньжат\n\n")
            a.withdraw()
        elif atputi=='выход':
            print("Команда выбрана! Выходим с сохранением данных")
            a.SaveDataToBober()
            time.sleep(1)
            exit(56)
        elif atputi=='пароль':
            print("Команда выбрана! Включаем режим смены пароля")
            time.sleep(1)
            a.changePassWithBober()
        elif atputi=='имя':
            print("Команда выбрана! Включаем режим смены имени")
            time.sleep(1)
            a.changeNameWithBober()
        elif atputi=="затереть":
            print("Команда выбрана! Стереть все данные, включая баланс\n\n")
            time.sleep(1)
            a.removeDataWithBober()
passw = input("Введи пароль для входа в прогу\n")
aquacore.seek(0)
vernpass = aquacore.readline()
if vernpass.strip() == passw:
    print("\nВход успешен! Загрузка...")
    time.sleep(3)
    aquacore.seek(0)  # начнём читать
    loadpass = aquacore.readline()
    loadbal = aquacore.readline()
    loadname = aquacore.readline()
    a = safecore(passw=loadpass.strip(), bal=loadbal.strip(),fullname=loadname.strip())  # эти данные нужно менять в проге
    # strip убирает ненужные \n. Они мешают работать проге.
    a.menu()
else:
    print('Пароль неверен! Попробуй ещё раз')
    exit(56)
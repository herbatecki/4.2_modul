import sys      # byłaby potrzebna jakbym od razu chciał pobrać 2 lub więcej składników od użytkownika kalkulatora
import logging  # też żeby korzystać z logging zamiast print

logging.basicConfig(level=logging.DEBUG)
logging.warning("warning!")
logging.debug("debug")


operation_choice = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
args_choice1 = input("Podaj składnik nr 1: ")
args_choice2 = input("Podaj składnik nr 2: ")

"""def demo_function():   # prosta funkcja na zerkanie na jej mechanizm
    print("I am inside of a function!")
    # return demo_function""" # bez sensu bo w return jest funkcja... definiowana

# demo_function()

def add_operation(operation_choice):
    while True:
        operation_choice = int(operation_choice) # bez przekształcenia na liczby nie porównuje w ogóle!
        if operation_choice > 4:
            logging.info("nie ma takiej operacji!")
            break
        elif operation_choice == 1:
            logging.info(f"dodaję składniki {args_choice1} i {args_choice2}")
            add_result =(int(args_choice1) + int(args_choice2))
            # print(f'Wynik to {add_result}')
            return add_result
        elif operation_choice == 2:
            logging.info(f"odejmuję składniki {args_choice1} i {args_choice2}")
            add_result =(int(args_choice1) - int(args_choice2))
            # print(f'Wynik to {add_result}')
            return add_result
        elif operation_choice == 3:
            logging.info(f"mnożę składniki {args_choice1} i {args_choice2}")
            add_result =(int(args_choice1) * int(args_choice2))
            # print(f'Wynik to {add_result}')
            return add_result
        elif operation_choice == 4:
            logging.info(f"dzielę składniki {args_choice1} i {args_choice2}")
            add_result =(int(args_choice1) / int(args_choice2))
            # print(f'Wynik to {add_result}')
            return add_result # nie zwracamy funkcji (w tym przypadku add_operation), którą definiujemy

# add_operation(operation_choice) # taki zapis prawdiłowy bez returna
final_result = add_operation(operation_choice)
print(f'Wynik to {final_result}')
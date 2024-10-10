def is_number(str):
    #Sprawdz, czy podany ciag znakow mozna przekonwertowac na wartosc liczbowa.
    try:
        float(str)
        return True
    except ValueError:
        return False

def convert_number(str):
    #Przekonwertuj podany ciag na wartosc liczbowa.
    if is_number(str):
        return float(str)
    else:
        raise ValueError(f"Cannot convert {str} to a number.")

def ask_for_a_number(force_valid_input):
    #Popros uzytkownika o podanie liczby, w oparciu o warunek waznosci.
    while True:
        user_input = input("Please provide a number! ")
        if is_number(user_input):
            return convert_number(user_input)
        else:
            if force_valid_input:
                print("This didn't look like a number, try again.")
            else:
                return None

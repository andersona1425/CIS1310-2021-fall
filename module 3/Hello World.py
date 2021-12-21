x = int(input("What year is it?"))
y = int(input("What year were you born?"))

try: 
    birth_year = x - y
    print("The amount of years you were born is or a year off from....")
    print(birth_year)

except ValueError:
    print("Please enter a valid key. Numbers only.")
    x = 2021 
    input("What year were you born?")
except:
    print("an error has occured")
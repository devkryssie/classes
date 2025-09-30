def read_int(promt,min, max):
    should_promt = True
    while should_promt:
        try:
            user_input = input(promt)
            if  float(user_input) not in range(min,max):
                raise IndexError
            else:
                should_promt = False
                return user_input
        except ValueError:
            print("wrong input")
        except IndexError:
            print("the value is not within permitted range")
        except Exception:
            print("oops something happened")
v = read_int("enter a number: ", -10, 10)
print("the number is:", v)

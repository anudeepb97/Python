def do_stuff(num):
    try:
        if num and type(num)!=bool:
            print(type(num))
            return int(num) + 5
        else:
            return 'Please enter a number'
    except ValueError as err:
        return err
    except TypeError as tp:
        return tp

# a = input('Enter a number: ')
print(do_stuff(True))

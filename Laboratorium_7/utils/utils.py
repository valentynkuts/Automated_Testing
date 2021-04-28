def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error.Division by Zero"
    except:
        return "Something wrong"

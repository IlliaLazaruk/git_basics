def avg(*args:int|float) -> float:
    """Average value of one or more numbers.

    This function return the average value of received number or numbers.

    Args:
        arg: first argument
        *args: next arguments

    Return:
        Average value
    """
    args_sum = 0
    try:
        args_sum += sum(args)
        average = args_sum / len(args)   
        return average
    
    except TypeError:
        print("An error occured. Please recheck your argument and enter it again")

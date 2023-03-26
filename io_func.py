def repeatOnError(*exceptions):
    def checking(function):
        def checked(*args, **kwargs):
            while True:
                try:
                    result = function(*args, **kwargs)
                except exceptions as except_obj:
                    print(except_obj)
                    print("Повторите")
                else:
                    return result
        return checked
    return checking


@repeatOnError(ValueError)
def get_int(message_text):
    return int(input(f"{message_text}: "))

def repeatOnError(*exceptions):
    def checking(function):
        def checked(message_text):
            while True:
                try:
                    result = function(message_text)
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

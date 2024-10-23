def test_function():
    # Внутренняя функция
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызов внутренней функции внутри test_function
    inner_function()


# Вызов функции test_function, которая вызовет inner_function
test_function()

# Попытка вызвать inner_function вне функции test_function приведет к ошибке,
# так как она не определена в глобальной области видимости.
# inner_function()

# Tuple
immutable_var = (1, 2, "a", "b")

print("Immutable tuple:", immutable_var)

# immutable_var[0] = 10 - Попытка изменить значения кортежа.
# Выдаст ошибку - кортежи неизменяемы.


# List
mutable_list = [1, 2, "a", "b"]

mutable_list[0] = 10
mutable_list.append("Modified")

print("Mutable list:", mutable_list)

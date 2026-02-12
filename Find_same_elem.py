def common_elements():
    set_3 = {i for i in range(100) if i % 3 == 0}
    set_5 = {i for i in range(100) if i % 5 == 0}

    intersection = set( set_3) & set(set_5)

    return intersection

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("Результат:", common_elements())



def main():
    # [] array XD
    # ['Isable', 'Mulan', 255, ['Pucca', 'percy']]
    fruits = []
    fruits.append('Kiwi')
    fruits.append('Berry')
    fruits.append('Melon')

    print(fruits)

    fruits.sort()

    pop_element = fruits.pop()
    print(pop_element)

    fruits.insert(0, "apple") # Insert at index 0
    print(fruits)

    pop_index = fruits.pop(1) # Remove at index 1
    print(pop_index)

    # fruits.remove('Dragon fruit') # No exist in list
    # ValueError: list.remove(x): x not in list

    # Ejemplo de Operaciones esenciales
    def pyramid_sum(lower, upper, margin = 0):
        blanks = ' ' * margin
        print(blanks, lower, upper)

        if lower > upper:
            print(blanks, 'Done')
            return 0
        else:
            result = lower + pyramid_sum(lower + 1, upper, margin + 4)
            print(blanks, result)
            return result

    pyramid_sum(1, 4)


if __name__ == '__main__':
    main()
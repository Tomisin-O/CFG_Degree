# This is a sample Python script.
'cat' + 3 -- cant preform same type of operation on different types
should be "cat" + "3"

--anything after a dot is a method

can call variables into function
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    Item_1_name = "Burger"
    Item_1_price = 10.99

    Item_2_name = "Fries"
    Item_2_price = 2.99

    Item_3_name = "Milkshake"
    Item_3_price = 4.99

    total = Item_1_price + Item_2_price + Item_3_price
    return (print(total))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


wrd="Python"
ans_1= slice(4)
print(wrd[ans_1])




wrd="Python"
ans_1= slice(2, 4, 6)
print(wrd[ans_1])



for key, value in pets.items():
    print(f"We have {value} {key}.")
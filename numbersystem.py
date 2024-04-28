def print_sequence(start, end, step, vertical=True, forward=True):
    if step <= 0:
        print("Enter a positive step value.")
        return

    if start <= end:
        if forward:
            if vertical:
                print("Forward order in vertical:")
                for i in range(start, end + 1, step):
                    print(i)
            else:
                print("Forward order in horizontal:")
                for i in range(start, end + 1, step):
                    print(i, end=" ")
        else:
            if vertical:
                print("Reversed order in vertical:")
                for i in range(end, start - 1, -step):
                    print(i)
            else:
                print("Reversed order in horizontal:")
                for i in range(end, start - 1, -step):
                    print(i, end=" ")
    else:
        if forward:
            if vertical:
                print("Forward order in vertical:")
                for i in range(end, start + 1, step):
                    print(i)
            else:
                print("Forward order in horizontal:")
                for i in range(end, start + 1, step):
                    print(i, end=" ")
        else:
            if vertical:
                print("Reversed order in vertical:")
                for i in range(start, end - 1, -step):
                    print(i)
            else:
                print("Reversed order in horizontal:")
                for i in range(start, end - 1, -step):
                    print(i, end=" ")


def main():
    start_point = int(input("Enter starting number: "))
    end_point = int(input("Enter ending point: "))
    updation = int(input("Enter updation value: "))
    choice_vertical = int(input("Enter 1 for result in vertical or enter 2 for result in horizontal: "))
    choice_forward = int(input("Enter 1 for forward order or enter 2 for reverse order: "))

    if choice_vertical == 1:
        vertical = True
    elif choice_vertical == 2:
        vertical = False
    else:
        print("Enter a valid choice for vertical printing.")

    if choice_forward == 1:
        forward = True
    elif choice_forward == 2:
        forward = False
    else:
        print("Enter a valid choice for order of printing.")

    print_sequence(start_point, end_point, updation, vertical, forward)


if __name__ == "__main__":
    main()
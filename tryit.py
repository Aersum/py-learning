def newfunc(t):
    try:
        t=int(t)
        print("Number! {0}".format(t))
    except ValueError:
        print('Error')
newfunc(input('Enter number: '))

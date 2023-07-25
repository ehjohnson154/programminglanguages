
def main():
    array = [0, 1, -1, -1, -1, -1, -1, -1]

    for i in range(0 ,len(array)):
        array[i +1] = array[i] + array[ i -1]


def better_main():
    '''
    Catching errors helps us debug, and can help us circumvent errors if they are expected

    :return:
    '''
    array = [0, 1, -1, -1, -1, -1, -1, -1]

    try:
        for i in range(0, len(array)):
            array[i + 1] = array[i] + array[i - 1]
    except Exception as e:
        print(e)
        print('We looked up index: {} for an array of size: {}'.format(i+1, len(array)))
        print(array)


def betterer_main():
    '''
    More specific error types help us isolate errors

    :return:
    '''
    array = [0, 1, -1, -1, -1, -1, -1, -1]

    try:
        fib_dict = {}
        for i in range(0, len(array)):
            array[i + 1] = array[i] + array[i - 1]
            fib_dict[i] = array[i]
            print(fib_dict[i+1])
    except IndexError as e:
        print(e)
    except KeyError as e:
        print('Fib Dict is missing key: {}'.format(e))
    else:
        print('Everything good here!')
    finally:
        print(array)


def good_main():
    '''
    A good try, except will highlight the problem for us

    :return:
    '''
    array = [0, 1, -1, -1, -1, -1, -1, -1]

    try:
        for i in range(0, len(array)):
            array[i + 1] = array[i] + array[i - 1]
    except IndexError as e:
        print(e)
        print((len(array), i+1))
    else:
        print('Everything good here!')
    finally:
        print(array)



def real_main():
    '''
    We can nest try, excepts if we need to

    :return:
    '''
    array = [0, 1, -1, -1, -1, -1, -1, -1]

    for i in range(0,len(array)):
        try:
            if i-1 < 0:
                raise ValueError('Cannot have a negative array index.')
            array[i + 1] = array[i] + array[i - 1]
        except IndexError:
            continue
        except ValueError:
            val1, val2 = 0, 1
            try:
                array[i + 1] = val1 + val2
            except IndexError:
                continue
    print(array)

if __name__ == '__main__':
    main()

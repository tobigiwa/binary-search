
import sys

def recursive_binary_search(arr:list, low:int, high:int, key:int):
    if low == high:
        if arr[low] == key:
            return f'list contain only one element, value: {key} at index {low}'
        else:
            return f'search not in list'
    else:
        if low <= high:

            mid = (low + high) // 2

            print('----------------------------')
            print(f'At start/another interation: \nlow is {low}, mid is {mid}, high is {high}')
            print('----------------------------\n')

            if key == arr[mid]:
                print("Found key")
                return f"search(key): {key}, low is: {low}, mid is: {mid}, mid value is(arr[mid]): {arr[mid]}, high is: {high}"

            elif key < arr[mid]:
                print('key was lesser than our mid value, so high became mid minus 1')
                print(f"search(key): {key}, low is: {low}, mid is: {mid}, mid value is(arr[mid]): {arr[mid]}, high is: {high} \n")
                return recursive_binary_search(arr, low, mid - 1, key)

            else:
                print('key was higher than our mid value, so low became mid plus 1')
                print(f"search(key): {key}, low is: {low}, mid is: {mid}, mid value is(arr[mid]): {arr[mid]}, high is: {high} \n")
                return recursive_binary_search(arr, mid + 1, high, key)

        else:
            return "Search not in list"



if __name__ == '__main__':
    test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # test = [3]
    try:
        args = int(sys.argv[1])
        find = recursive_binary_search(test, 0, len(test)-1, args)
        print(find)
    except IndexError:
        try:
            print("Pick any number to search from this list to search\n", test)
            search = int(input('enter number to search:'))
            find = recursive_binary_search(test, 0, len(test)-1, search)
            print(find)
        except ValueError as err:
            print('No input, program will exit')
            sys.exit()

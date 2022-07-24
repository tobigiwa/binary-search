from cgi import test
import sys

def iterative_binary_search(arr: list[int], key: int) -> str:
    low, high = 0, len(arr) - 1

    if low == high:
        if arr[low] == key:
            return f'list contain only one element, value: {key} at index {low}'
        else:
            return f'search not in list'
    else:
        while low <= high:
            mid = (low + high) // 2
            print('----------------------------')
            print(f'At start/another interation: \nlow is {low}, mid is {mid}, high is {high}')
            print('----------------------------\n')

            if arr[mid] == key:
                print("Found key")
                return f"search(key): {key}, low is: {low}, mid is: {mid}, mid value is(arr[mid]): {arr[mid]}, high is: {high}"

            elif key < arr[mid]:
                high = mid - 1
                print('key was lesser than our mid value, so high became mid minus 1')
                print(f"search(key): {key}, low is: {low}, mid is: {mid}, mid value is(arr[mid]): {arr[mid]}, high is: {high} \n")

            else:
                low = mid + 1
                print('key was higher than our mid value, so low became mid plus 1')
                print(f"search(key): {key}, low is: {low}, mid is: {mid}, mid value is(arr[mid]): {arr[mid]}, high is: {high} \n")

        return "Search not in list"



if __name__ == '__main__':
    test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # test = [3]
    try:
        args = int(sys.argv[1])
        find = iterative_binary_search(test, args)
        print(find)
    except IndexError:
        print("Pick any number to search from this list to search", test)
        try:
            search = int(input('enter number to search:'))
            find = iterative_binary_search(test, search)
            print(find)
        except ValueError as err:
            print('No input, program will exit')
            sys.exit()
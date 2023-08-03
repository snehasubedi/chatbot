from botwork.functions import conversation
from botwork.path import mapping as mp_func


def main():
    conversation.greeting()
    while True:
        data = input(f'user: ')
        mp_func(data)
    

if __name__ == "__main__":
    main()
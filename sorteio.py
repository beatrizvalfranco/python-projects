import numpy as np

def main():
    hiatus = int(input())
    numbers = int(input())

    sorteio = np.random.permutation(hiatus)[:numbers]

    for i in sorteio:
        print(i)


if __name__ == "__main__":
    main()

def is_primo(numero: int) -> bool:
    list_end = [i for i in range(2, numero) if numero % i == 0]

    return len(list_end) == 0


def run():
    print(is_primo(4))


if __name__ == "__main__":
    run()

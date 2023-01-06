import typer


def fill_T_from_key(key: list):
    T = []
    while len(T) < 256:
        for i in key:
            T.append(i)
    return T[:256]


def rc4(plain_text: str, key: list = [1, 2, 3, 6]):
    S = []
    T = fill_T_from_key(key)

    for i in range(256):
        S.append(i)

    j = 0
    for i in range(256):
        j = (j + S[i] + T[i]) % 256
        S[i], S[j] = S[j], S[i]

    i = 0
    j = 0
    C = []
    for p in plain_text:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        k = S[t]

        C.append(int(bin(k), 2) ^ int(bin(ord(p)), 2))
    return C


def main(plain_text: str = typer.Option(..., prompt=True)):
    cipher_text = rc4(plain_text)
    print(f"{cipher_text=}")


if __name__ == "__main__":
    typer.run(main)

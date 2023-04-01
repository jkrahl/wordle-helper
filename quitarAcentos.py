import io

def main():
    words = []
    lista = []
    with io.open('palabras_con_acentos.txt', 'r', encoding='utf-8') as f:
        words = f.read().splitlines()
    for word in words:
        lista.append(quitarAcentos(word))

    with io.open('palabras.txt', 'w', encoding='utf-8') as f:
        for word in lista:
            f.write(word + '\n')

                    
def quitarAcentos(word):
    word = word.replace('á', 'a')
    word = word.replace('Á', 'A')
    word = word.replace('é', 'e')
    word = word.replace('É', 'E')
    word = word.replace('è', 'e')
    word = word.replace('È', 'E')
    word = word.replace('í', 'i')
    word = word.replace('Í', 'I')
    word = word.replace('ó', 'o')
    word = word.replace('Ó', 'O')
    word = word.replace('ú', 'u')
    word = word.replace('Ú', 'U')
    word = word.replace('ü', 'u')
    word = word.replace('Ü', 'U')
    return word

if __name__ == '__main__':
    main()
import sys

def revert_file():
    file = input('Insira o nome do arquivo(path): ')
    try:
        with open(file, 'r') as f:
            for line in reversed(f.readlines()):
                print(line.rstrip()[::-1])
    except FileNotFoundError:
        print('Arquivo não encontrado')
        sys.exit(1)

def main():
    revert_file()

if __name__ == "__main__":
    sys.exit(main())
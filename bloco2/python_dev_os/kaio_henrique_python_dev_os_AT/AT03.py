import os
import sys

def files_list(directory):
    list_of_files = []
    for file in os.listdir(directory):
        list_of_files.append(directory + "/" + file)
    return list_of_files

def get_byte_size(file):
    return os.path.getsize(file)


def create_report_header(report_file):
    try:
        with open(report_file, "w") as report:
            report.write("| File Name |  Size |\n")
            report.write("|-----------|-------|\n")
    except Exception as e:
        print(e)
    finally:
        report.close()

def create_report(list_of_files_and_size):
    try:
        with open("report.txt", "a+") as report:
            for file, size in list_of_files_and_size:
                file_name = file.split("/")[-1]
                report.write(f"{file_name} {size}\n")
    except:
        print("Erro ao criar arquivo report.txt")
    finally:
        report.close()

def print_report_file(report_file):
    try:
        with open(report_file, "r") as report:
            for line in report:
                print(line, end="")
    except:
        print("Erro ao imprimir o arquivo report.txt")
    finally:
        report.close()

def main():
    try:
        directory = input("Digite o diretório(path): ")
        list_of_files = files_list(directory)
        list_of_files_and_size = []
        for file in list_of_files:
            list_of_files_and_size.append((file, get_byte_size(file)))
        list_of_files_and_size.sort(key=lambda x: x[1], reverse=True)
        create_report_header("report.txt")
        create_report(list_of_files_and_size)
        print_report_file("report.txt")
    except FileNotFoundError:
        print("O diretório não existe")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    sys.exit(main())
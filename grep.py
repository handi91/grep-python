import os
import sys
import re


def list_files(folder):
    """Mencari sekumpulan file ditentukan dari folder"""
    locations = []
    for (root, dirs, files) in os.walk(folder, topdown=True):
        for arr in files:
            if root[-1:] != "\\":
                locations.append("{}\{}".format(root, arr))
            else:
                locations.append("{}{}".format(root, arr))
    return locations


def mode_default(pattern, location):
    """Mode tanpa argumen options"""
    files = list_files(location)
    if (len(files) > 0):
        for i in range(len(files)):
            sentences = scan_file(files[i])
            for count in range(len(sentences)):
                # hanya mengecek konten di dalam kalimat
                if(pattern in sentences[count]):
                    print_line(files[i], count + 1, sentences[count])
    else:
        sentences = scan_file(location)
        for count in range(len(sentences)):
            # hanya mengecek konten di dalam kalimat
            if(pattern in sentences[count]):
                print_line(location, count + 1, sentences[count])

# TODO: edit logic pattern match string
def mode_whole_word(pattern, location):
    """Mode argumen menggunakan -w"""
    files = list_files(location)
    if (len(files) > 0):
        for i in range(len(files)):
            sentences = scan_file(files[i])
            for count in range(len(sentences)):
                if(re.search(rf"\b{pattern}\b", sentences[count])):
                    print_line(files[i], count + 1, sentences[count])
    else:
        sentences = scan_file(location)
        for count in range(len(sentences)):
            if(re.search(rf"\b{pattern}\b", sentences[count])):
                print_line(location, count + 1, sentences[count])

# TODO: edit logic pattern match string
def mode_insensitive(pattern, location):
    """Mode argumen menggunakan -i"""
    files = list_files(location)
    if (len(files) > 0):
        for i in range(len(files)):
            sentences = scan_file(files[i])
            for count in range(len(sentences)):
                if(re.search(f"{pattern.lower()}", sentences[count].lower())):
                    print_line(files[i], count + 1, sentences[count])
    else:
        sentences = scan_file(location)
        for count in range(len(sentences)):
            if(re.search(f"{pattern.lower()}", sentences[count].lower())):
                print_line(location, count + 1, sentences[count])


def scan_file(location):
    """Melakukan pemindaian isi dari file"""
    try:
        with open(location, "r") as file:
            output = []
            for sentence in file:
                output.append(sentence.strip())
            return output
    except FileNotFoundError:
        print(f"Path {location} tidak ditemukan")


def print_line(location, line, sentence):
    """Mencetak format string di terminal"""
    print(f"{location:<40} line {line:<3} {sentence[0:40]}")


if __name__ == "__main__":
    # input berdasarkan argumen program berjumlah 3
    if (2 < len(sys.argv) <= 4):
        option = sys.argv[1]
        pattern = sys.argv[len(sys.argv) - 2]
        location = sys.argv[len(sys.argv) - 1]
        # case: option tidak digunakan
        if (option == pattern):
            # TODO: kalau pattern adalah option
            mode_default(pattern, location)
        elif (option == '-w'):
            mode_whole_word(pattern, location)
        elif (option == '-i'):
            mode_insensitive(pattern, location)
        else:
            raise ValueError("Argumen program tidak benar.")
    else:
        raise ValueError("Argumen program tidak benar.")
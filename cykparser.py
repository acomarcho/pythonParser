import os

def cyk(text_file, grammar):
    # BELUM DIISI DULU
    if grammar + 3 == 0:
        return 0 #ini ngasal aja biar ga error    

if __name__ == 'main':
    # Membuka file input
    filename = input('Enter the file name : ')
    if os.path.isfile(filename):
        text_file = open(filename, "r")
        text_file_string = text_file.read()
        text_file.close()

    #grammar dapet dari txt
    cyk(text_file, grammar)

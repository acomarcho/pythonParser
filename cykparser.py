import os

def logo():
    print("                                          __                     __     ")  
    print("                              _    _____ / /______  __ _  ___   / /____ ")
    print("                             | |/|/ / -_) / __/ _ \/  ' \/ -_) / __/ _ \ ")
    print("                             |__,__/\__/_/\__/\___/_/_/_/\__/  \__/\___/ \n\n")
    print("██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗    ██████╗  █████╗ ██████╗ ███████╗███████╗██████╗ ")
    print("██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗")
    print("██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║    ██████╔╝███████║██████╔╝███████╗█████╗  ██████╔╝")
    print("██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║    ██╔═══╝ ██╔══██║██╔══██╗╚════██║██╔══╝  ██╔══██╗")
    print("██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║    ██║     ██║  ██║██║  ██║███████║███████╗██║  ██║")
    print("╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝\n")
    print("=========================================================================================================")
    print("                            Ketik X apabila anda ingin keluar dari program!")
    print("=========================================================================================================")

def cyk(text_file, grammar):
    length = len(text_file)
    table = [[[] for x in range(length - y)] for y in range(length)]

    if grammar + 3 == 0:
        return 0 #ini ngasal aja biar ga error    

if __name__ == '__main__':
    logo()
    # Membuka file input                                                                                                
    filename = input('Enter the file name : ')
    while filename != 'X' :
        if os.path.isfile(filename):
            text_file = open(filename, "r")
            text_file_string = text_file.read()
            text_file.close()
            print(text_file_string)
        else : 
            print('File tidak ditemukan, Silahkan tulis ulang nama file!')
        filename = input('\nEnter the file name : ')

    print("=========================================================================================================")
    #grammar dapet dari txt
    #cyk(text_file, grammar)

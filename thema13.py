"""
/*
* It reads form a file. You should type the path where the
* file is stored. If it does not find it throws an error
* message
* @return list(text): It returns the content of the file
* as a list
*/
"""
def read_from_file():
    while True:
        try:
            filePath = input("Insert file path: ")
            infile = open(filePath, 'r')
            break
        except (FileNotFoundError, IOError):
            print("Wrong file or file path ")
            continue
    text = infile.read()
    infile.close()
    return list(text)

"""
/*
* Extracts the spaces and the new line char
* from the inserted list
* @return lista: Returns a list of digits
*/
"""
def  save_file_into_list(file):
    lista = []
    for i in range(len(file)):
        if(file[i] == " " or file[i] == "\n"):
            continue
        lista.append(file[i])
    return lista

"""
/**
* Ιt fils the incorporated list
* @return values: Returns the incorporated list
*/
"""
def initialize_list(lista):
    values = [ [0, 0, 0],
               [0, 0, 0],
               [0, 0, 0] ]
    count = 0
    for i in range(3):
        for j in range(3):
            values[i][j] = int(lista[count])
            count = count + 1
    return values
"""
/*
* It calculates the determinant
* @return det: It returns the result of the determinant
*/
"""
def calculate_determinant(lista):
    det = lista[0][0]*(lista[1][1]*lista[2][2] - lista[1][2]*lista[2][1]) - lista[0][1]*(lista[1][0]*lista[2][2] - lista[1][2]*lista[2][0]) + lista[0][2]*(lista[1][0]*lista[2][1]- lista[1][1]*lista[2][0])
    return det

"""
/*
* Here the is where the main program begins
*/
"""
def main():
    flag = 'yes'
    while(flag.casefold() == 'yes'):
        file = read_from_file()
        lista = save_file_into_list(file)
        initialization = initialize_list(lista)
        print("The det is: " + str(calculate_determinant(initialization)))
        flag = input("If you want to continue type 'yes' anything else will terminate the program: ")
    print("Terminating the program!")

#Invokes the main method to start the program
main()

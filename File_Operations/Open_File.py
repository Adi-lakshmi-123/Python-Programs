#This is a program for file opening.

def open_file():
    filename = "File_Operations/NewFile.txt"
    '''Extracting the text file'''
'''Checking the errors and others'''
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
            file.close()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")

if _name_ == "_main_":
    '''calling the function'''
    open_file()
filename.close()

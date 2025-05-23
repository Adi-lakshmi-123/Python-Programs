'''This is a file to add data into the text'''


def write_file():
    filename = "File_Operations/NewFile.txt"  # Extracting the path of file.
    data = "This is a sample text written to the file."

    try:
        with open(filename, 'a') as file:  # appending data to the existing file.
            file.write(data)
            print(f"Successfully wrote to '{filename}'.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")

if _name_ == "_main_":
    write_file()

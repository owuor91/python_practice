

def write_to_file(text_to_write):
    with open('desert_file.txt', 'a+') as open_file:
        open_file.write("\n"+text_to_write)
        open_file.close()
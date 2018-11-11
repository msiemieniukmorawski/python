def write_line(file_name, var_to_write):
    with open(file_name, 'a') as plik:
        plik.write(str(var_to_write) + '\n')


_file = 'text2.txt'
string = 'test te st tes t set ets'

write_line(_file, string)

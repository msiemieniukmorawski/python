string1 = "Ala ma kota, kot ma Ale"
string2 = "Arek woli psy, a najbardziej boksery"

string1_len = len(string1)
string2_len = len(string2)

if( string1_len <= string2_len ):
    string_longer = string2_len
    space = string2_len - string1_len
    short_string = string1
    long_string = string2
else:
    string_longer = string1_len
    space = string1_len - string2_len
    short_string = string2
    long_string = string1

string_longer = int(string_longer)
short_string = short_string + (' ' * space)
short_string =list(short_string)
i = 0

while i < string_longer:
    if (ord(short_string[i]) != ord(long_string[i])):
        short_string[i] = long_string[i]

    i += 1

short_string = ''.join(short_string)
print(short_string)




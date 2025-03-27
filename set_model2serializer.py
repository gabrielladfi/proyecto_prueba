serializer_parenthesis = "( "

with open('convertme.txt') as f:
    lines = f.readlines()
    for line in lines:
        values = line.split('=')
        value = values[0].replace(" ", "")
        print(value)
        serializer_parenthesis+=f"'{value}', "

serializer_parenthesis+=")"
print(serializer_parenthesis)
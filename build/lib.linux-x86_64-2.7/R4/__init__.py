def encode(params):
    ask = params.upper()
    no = len(ask)
    kata = ''
    for i in range(0,len(ask)):
        if ask[i] == "A":
            kata += "R40Z"
        elif ask[i] == "B":
            kata += "R49Y"
        elif ask[i] == "C":
            kata += "R48X"
        elif ask[i] == "D":
            kata += "R47W"
        elif ask[i] == "E":
            kata += "R46P"
        elif ask[i] == "F":
            kata += "R45U"
        elif ask[i] == "G":
            kata += "R44T"
        elif ask[i] == "H":
            kata += "R43S"
        elif ask[i] == "I":
            kata += "R42R"
        elif ask[i] == "J":
            kata += "R41Q"
        elif ask[i] == "K":
            kata += "R410P"
        elif ask[i] == "L":
            kata += "R412N"
        elif ask[i] == "M":
            kata += "R413M"
        elif ask[i] == "N":
            kata += "R414L"
        elif ask[i] == "O":
            kata += "R415K"
        elif ask[i] == "P":
            kata += "R416J"
        elif ask[i] == "Q":
            kata += "R417I"
        elif ask[i] == "R":
            kata += "R418H"
        elif ask[i] == "S":
            kata += "R419G"
        elif ask[i] == "T":
            kata += "R420F"
        elif ask[i] == "U":
            kata += "R421E"
        elif ask[i] == "V":
            kata += "R422O"
        elif ask[i] == "W":
            kata += "R423C"
        elif ask[i] == "X":
            kata += "R424B"
        elif ask[i] == "Y":
            kata += "R425A"
        elif ask[i] == "Z":
            kata += "R430ZA"
        ## ANgka
        elif ask[i] == "1":
            kata+= "R4PUT"
        elif ask[i] == "2":
            kata += "R4AD"
        elif ask[i] == "3":
            kata += "R4IA"
        elif ask[i] == "4":
            kata += "R4PT"
        elif ask[i] == "5":
            kata += "R4AI"
        elif ask[i] == "6":
            kata += "R4NM"
        elif ask[i] == "7":
            kata += "R4RH"
        elif ask[i] == "8":
            kata += "R4DP"
        elif ask[i] == "9":
            kata += "R4EN"
        elif ask[i] == "0":
            kata += "R4LO"
        ## KARAKTER
        elif ask[i] == "~":
            kata += "R4BTK"
        elif ask[i] == "`":
            kata += "R4KT"
        elif ask[i] == "!":
            kata += "R4TRU"
        elif ask[i] == "@":
            kata += "R4MSN"
        elif ask[i] == "#":
            kata += "R4HSA"
        elif ask[i] == "$":
            kata += "R4RL"
        elif ask[i] == "%":
            kata += "R4CNT"
        elif ask[i] == "^":
            kata += "R4IPT"
        elif ask[i] == "&":
            kata += "R4DN"
        elif ask[i] == "*":
            kata += "R4ILK"
        elif ask[i] == "(":
            kata += "R4BKRNG"
        elif ask[i] == ")":
            kata += "R4TTKRNG"
        elif ask[i] == "+":
            kata += "R4SLP"
        elif ask[i] == "-":
            kata += "R4CTRP"
        elif ask[i] == "_":
            kata += "R4UDRSR"
        elif ask[i] == "=":
            kata += "R4SMNGD"
        elif ask[i] == "'\'":
            kata += "R4RHLS"
        elif ask[i] == "/":
            kata += "R4LHLS"
        elif ask[i] == "}":
            kata += "R4SKBRSH"
        elif ask[i] == "{":
            kata += "R4ESKBRSH"
        elif ask[i] == "[":
            kata += "R4SKKG"
        elif ask[i] == "]":
            kata += "R4EKKG"
        elif ask[i] == "'":
            kata += "R4SQT"
        elif ask[i] == ":":
            kata += "R4DDT"
        elif ask[i] == ";":
            kata += "R4IKM"
        elif ask[i] == "?":
            kata += "R4TTY"
        elif ask[i] == ".":
            kata += "R4PNT"
        elif ask[i] == ">":
            kata += "R4BKRGT"
        elif ask[i] == ",":
            kata += "R4AMMC"
        elif ask[i] == "<":
            kata += "R4TTPGKR"
        elif ask[i] == "|":
            kata += "R4TGK"
        else:
            kata += "R459C"
    return kata

def decode(params):
    ask = params.upper()
    no = len(ask)
    data = ask.split("R4")
    kata = ''
    hasil = ''
    for i in data:
        if i == "0Z":
            kata += "A"
        elif i == "9Y":
            kata += "B"
        elif i == "8X":
            kata += "C"
        elif i == "7W":
            kata += "D"
        elif i == "6P":
            kata += "E"
        elif i == "5U":
            kata += "F"
        elif i == "4T":
            kata += "G"
        elif i == "3S":
            kata += "H"
        elif i == "2R":
            kata += "I"
        elif i == "1Q":
            kata += "J"
        elif i == "10P":
            kata += "K"
        elif i == "12N":
            kata += "L"
        elif i == "13M":
            kata += "M"
        elif i == "14L":
            kata += "N"
        elif i == "15K":
            kata += "O"
        elif i == "16J":
            kata += "P"
        elif i == "17I":
            kata += "Q"
        elif i == "18H":
            kata += "R"
        elif i == "19G":
            kata += "S"
        elif i == "20F":
            kata += "T"
        elif i == "21E":
            kata += "U"
        elif i == "22O":
            kata += "V"
        elif i == "23C":
            kata += "W"
        elif i == "24B":
            kata += "X"
        elif i == "25A":
            kata += "Y"
        elif i == "30ZA":
            kata += "Z"
        ## ANgka
        elif i == "PUT":
            kata+= "1"
        elif i == "AD":
            kata += "2"
        elif i == "IA":
            kata += "3"
        elif i == "PT":
            kata += "4"
        elif i == "AI":
            kata += "5"
        elif i == "NM":
            kata += "6"
        elif i == "RH":
            kata += "7"
        elif i == "DP":
            kata += "8"
        elif i == "EN":
            kata += "9"
        elif i == "LO":
            kata += "0"
        ## KARAKTER
        elif i == "R4BTK":
            kata += "'~'"
        elif i == "R4KT":
            kata += "`"
        elif i == "R4TRU":
            kata += "'!'"
        elif i == "R4MSN":
            kata += "@"
        elif i == "R4HSA":
            kata += "#"
        elif i == "R4RL":
            kata += "$"
        elif i == "R4CNT":
            kata += "%"
        elif i == "R4IPT":
            kata += "^"
        elif i == "RPDN":
            kata += "&"
        elif i == "RPILK":
            kata += "*"
        elif i == "R4BKRNG":
            kata += "("
        elif i == "R4TTPKRNG":
            kata += ")"
        elif i == "R4SLP":
            kata += "+"
        elif i == "R4CTRP":
            kata += "-"
        elif i == "R4UDRSR":
            kata += "_"
        elif i == "R4SMNGD":
            kata += "="
        elif i == "R4RHLS":
            kata += "'\'"
        elif i == "R4LHLS":
            kata += "/"
        elif i == "R4SKBRSH":
            kata += "}"
        elif i == "R4ESKBRSH":
            kata += "{"
        elif i == "R4SKKG":
            kata += "["
        elif i == "R4EKKG":
            kata += "]"
        elif i == "R4SQT":
            kata += "'"
        elif i == "R4DDT":
            kata += ":"
        elif i == "R4IKM":
            kata += ";"
        elif i == "R4TTY":
            kata += "?"
        elif i == "R4PNT":
            kata += "."
        elif i == "R4BKRGT":
            kata += ">"
        elif i == "R4AMMC":
            kata += ","
        elif i == "R4PPTGKR":
            kata += "<"
        elif i == "R4TGK":
            kata += "|"
        else:
            kata += " "
    for i in range(1, len(kata)):
        hasil += kata[i]
    return hasil


if __name__ == "__main__":
    print("Not Main Files")
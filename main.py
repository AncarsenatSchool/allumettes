PLR_WIN = 1


def think(matches):
    return matches

def ask_for_input(matches):

    try:
        line = int(input("ligne : "))
        qtt  = int(input("qtt   : "))
    except ValueError:
        return ask_for_input(matches)

    if not line or not qtt:
        return ask_for_input(matches)    
    
    try:
        return matches[line]-qtt
    except:
        return ask_for_input(matches)

def draw_matches(matches):
    for i in matches:
        print(i*"| ")



def main():
    matches=8,8


    draw_matches(matches)
    matches=ask_for_input(matches)
    if matches[0]==0 or matches[1]==0:
        return PLR_WIN

Running = True
while Running:
    main()

    
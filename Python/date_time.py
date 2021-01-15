import datetime

def print_time():
    parser = datetime.datetime.now()
    return parser.strftime("%d-%m-%Y %H:%M:%S")
    #pv . kk . vvvv & aika tunti:min:s
    #kantsii olla tarkana koska ajanvyöhykke (kesä- vai talviaika kyseessä)
    
print(print_time())

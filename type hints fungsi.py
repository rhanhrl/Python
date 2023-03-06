# type hints fungsi
import string

def typehints(parameter):
    "typehints"
    hasil = parameter**2
    print(hasil)
    return hasil
typehints(20)
#typehints(True)

# penggunaan type hints

def fungsihints(argument:int) -> int:
    "fungsi hints"
    output = 10**argument
    return output
hasil = fungsihints(5)
print(hasil)

def display(argument:string) -> str:
    print(argument)
    return argument
display("raihan")
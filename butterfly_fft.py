import cmath
import math
from point8_diffft_or_ditifft import point8_diffft_or_ditifft
from point8_ditfft_or_dififft import point8_ditfft_or_dififft

transform_choice = input("What do you what to find?\n1)DFT\t2)IDFT\n->")
method_choice = input("Using what method do you what to find\n1)DIT\t2)DIF\n->")
input_entered1 = ['DFT','dft','Dft','dFt','dfT','DFt','dFT','DfT','1','1.','1)','1)DFT']
input_entered2 = ['IFT','idft','IDft','idFt','idfT','IDFt','idFT','IDfT','2','2.','2)','2)IDFT']
input_entered3 = ['dit','DIT','Dit','dIt','diT','DIt','dIT','DiT','1','1.','1)','1)DIT']
input_entered4 = ['dif','DIF','Dif','dIf','diF','DIf','dIF','DiF','2','2.','2)','2)DIF']

x = input("Enter the 8 number sequence:") 
# xk = 0.5,0.5,0.5,0.5,0,0.5,0.5,0.5  xk = 1,2,3,4,4,3,2,1  xk=36,-4+9.7j,-4+4j,-4+7.7j,-4,-4-7.7j,-4-4j,-4-9.7j
#xn = 0,0,0,0,8,0,0,0  
x = x.split(","or" ")

def butterfly_fft(x,transform_choice,method_choice):
    """ Butterfly FFT and IFFT using DIF and DIT methods"""
    global input_entered1
    global input_entered2
    global input_entered3
    global input_entered4
    for i,num in enumerate(x):
        try:
            x[i] = complex(num)
        except:
            print("You didn't enter a number")
    w = [1,complex(1,-1)*(1/math.sqrt(2)),complex(0,-1),complex(-1,-1)*(1/math.sqrt(2))]
    wc = [w[0],w[1].conjugate(),w[2].conjugate(),w[3].conjugate()]

    if transform_choice in input_entered1:
        if method_choice in input_entered3:
            print("\nX(k) =",point8_ditfft_or_dififft(x,0))
        elif method_choice in input_entered4:
            print("\nX(k) =",point8_diffft_or_ditifft(x,0))
        else:
            print("Typo in choosing method")
    elif transform_choice in input_entered2:
        if method_choice in input_entered3:
            print("\nx(n) =",point8_diffft_or_ditifft(x,1))
        elif method_choice in input_entered4:
            print("\nx(n) =",point8_ditfft_or_dififft(x,1))
        else:
            print("Typo in choosing method")
    else:
            print("Typo in choosing transform")    

butterfly_fft(x,transform_choice,method_choice)

import cmath
import math

def point8_diffft_or_ditifft(x,num):
    """Point-8 DIF FFT or DIT IFFT"""
    twiddle = [1,complex(1,-1)*(1/math.sqrt(2)),complex(0,-1),complex(-1,-1)*(1/math.sqrt(2))]
    twiddle_conjugate = [twiddle[0],twiddle[1].conjugate(),twiddle[2].conjugate(),twiddle[3].conjugate()]
    if num == 0:
        w = twiddle
    elif num == 1:
        w = twiddle_conjugate
    else:
        print("Invalid input attribute")
        return num
    first_stage_output = [x[0]+x[4],x[1]+x[5],x[2]+x[6],x[3]+x[7],-x[4]+x[0],-x[5]+x[1],-x[6]+x[2],-x[7]+x[3]]
    #print("\nFirst stage output =",first_stage_output)
    second_stage_input = [first_stage_output[0],first_stage_output[1],first_stage_output[2],first_stage_output[3],
                     first_stage_output[4]*w[0],first_stage_output[5]*w[1],first_stage_output[6]*w[2],first_stage_output[7]*w[3]]
    #print("\nSecond stage input =",second_stage_input)
    second_stage_output = [second_stage_input[0]+second_stage_input[2],second_stage_input[1]+second_stage_input[3],-second_stage_input[2]+second_stage_input[0],-second_stage_input[3]+second_stage_input[1],
                       second_stage_input[4]+second_stage_input[6],second_stage_input[5]+second_stage_input[7],-second_stage_input[6]+second_stage_input[4],-second_stage_input[7]+second_stage_input[5]]
    #print("\nSecond stage output =",second_stage_output)
    third_stage_input = [second_stage_output[0],second_stage_output[1],second_stage_output[2]*w[0],second_stage_output[3]*w[2],
                     second_stage_output[4],second_stage_output[5],second_stage_output[6]*w[0],second_stage_output[7]*w[2]]
    #print("\nThird stage input =",third_stage_input)
    third_stage_output = [third_stage_input[0]+third_stage_input[1],-third_stage_input[1]+third_stage_input[0],third_stage_input[2]+third_stage_input[3],-third_stage_input[3]+third_stage_input[2],
                       third_stage_input[4]+third_stage_input[5],-third_stage_input[5]+third_stage_input[4],third_stage_input[6]+third_stage_input[7],-third_stage_input[7]+third_stage_input[6]]
    #print("\nThird stage output =",third_stage_output)
    y = [third_stage_output[0],third_stage_output[4],third_stage_output[2],third_stage_output[6],
          third_stage_output[1],third_stage_output[5],third_stage_output[3],third_stage_output[7]]
    for i,k in enumerate(y):
        if num == 1:
            y[i]=y[i]/8
        if y[i].imag == 0.0:
            y[i] = y[i].real
    return y

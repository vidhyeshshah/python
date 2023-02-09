number=int(input("Enter number: "))
a=len(str(number))
b=str(number)
words=""single_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
two_digits = ["","ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens_multiple= ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
tens_power = ["hundred", "thousand"]
if(a==0 or a>4):   
     print("Enter Valid input")
else:    
    while(a!=0):    
            if(a==1):        
                    print(single_digits[number], end = ' ') 
                    a-=1        
            elif(a==2):            
                if(number==0):               
                     break            
                elif(number>=10 and number<=19):          
                              print(two_digits[number-9], end = ' ')                
                              a-=2            
                elif(number>=20 and number%10==0):               
                                 print(tens_multiple[number//10], end = ' ')                
                                 a-=2           
                else:               
                     print(tens_multiple[number//10], end = ' ')               
                     number=number%10               
                     a-=1       
            elif(a==3):            
                    print(single_digits[number//100] ,""+ tens_power[0], end = ' ')           
                    number=number%100            
                    a-=1        
            elif(a==4):            
                 print(single_digits[number // 1000], "" + tens_power[1], end = ' ' )            
                 number = number % 1000            
                 if(number==0):                
                    break            
                 elif((len(str(number))==2 or len(str(number))==1)):               
                  a -= 2            
                 else:              
                  a-=1
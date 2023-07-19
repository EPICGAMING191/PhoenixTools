class steamKeyGeneration():
   def keyGenerator():
      from tqdm import tqdm
      import os 
      keyfile="keyfile.txt"
      combinations=0
      maxcombs=1
      num1=0
      num2=0
      num3=0
      num4=0
      num5=0
      num6=0
      num7=0
      num8=0
      num9=0
      num10=0
      num11=0
      num12=0
      for x in range(12):
         maxcombs=maxcombs * 35
      pbar=tqdm("Generating all possible combinations", maxcombs)
      def convertToLetters(number):
         if number==1:
            letter="A"
         elif number==2: 
            letter="B"
         elif number==3: 
            letter="C"
         elif number==4: 
            letter="D"
         elif number==5: 
            letter="E"
         elif number==6: 
            letter="F"
         elif number==7: 
            letter="G"
         elif number==8: 
            letter="H"
         elif number==9: 
            letter="I"
         elif number==10: 
            letter="J"
         elif number==11: 
            letter="K"
         elif number==12: 
            letter="L"
         elif number==13: 
            letter="M"
         elif number==14: 
            letter="N"
         elif number==15: 
            letter="O"
         elif number==16: 
            letter="P"
         elif number==17: 
            letter="Q"
         elif number==18: 
             letter="R"
         elif number==19: 
            letter="S"
         elif number==20: 
            letter="T"
         elif number==21: 
            letter="U"
         elif number==22: 
            letter="V"
         elif number==23: 
            letter="W"
         elif number==24: 
            letter="X"
         elif number==25: 
            letter="Y"
         elif number==26: 
             letter="Z"
         elif number==27: 
            letter=str(1)
         elif number==28: 
            letter=str(2)
         elif number==29: 
             letter=str(3)
         elif number==30: 
           letter=str(4)
         elif number==31: 
            letter=str(5)
         elif number==32: 
            letter=str(6)
         elif number==33: 
            letter=str(7)
         elif number==34:
          letter=str(8)
         elif number==35:
            letter=str(9)
         else:
            quit(1)
         return letter
      with open (keyfile,"r+") as kf:
         while combinations<maxcombs:
            num1=num1+1
            if num1>35:
               num2=num2+1
               num1=0
            if num2>35:
               num3=num3+1
               num2=0
            if num3>35:
               num4=num4+1
               num3=0
            if num4>35:
               num5=num5+1
               num4=0
            if num5>35:
               num6=num6+1
               num5=0
            if num6>35:
               num7=num7+1
               num6=0
            if num7>35:
               num8=num8+1
               num7=0
            if num8>35:
               num9=num9+1
               num8=0
            if num9>35:
               num10=num10+1
               num9=0
            if num10>35:
               num11=num11+1
               num10=0
            if num11>35:
               num12=num12+1
               num11=0
            if num12>35:
               done=1
               num12=0
         char1=convertToLetters(num1)
         char2=convertToLetters(num2)
         char3=convertToLetters(num3)
         char4=convertToLetters(num4)
         char5=convertToLetters(num5)
         char6=convertToLetters(num6)
         char7=convertToLetters(num7)
         char8=convertToLetters(num8)
         char9=convertToLetters(num9)
         char10=convertToLetters(num10)
         char11=convertToLetters(num11)
         char12=convertToLetters(num12)
         pt1=char1+char2+char3+char4+"-"
         pt2=char5+char6+char7+char8+"-"
         pt3=char9+char10+char11+char12
         key=pt1+pt2+pt3
         os.system("cls")
         pbar.update(1)
         print(key)
         kf.write(key)
         combinations=combinations+1
#-----------------------------------
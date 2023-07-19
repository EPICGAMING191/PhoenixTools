from .iptools import iptools
from .colors import colors
from .math import math
from .encryption import encryptionTools
from .steamkeygen import steamkeygen
from .writemodes import writemodes
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
    else:
      quit(1)
    return letter 
def helloWorld(): 
  print("Hell0 W0rld")
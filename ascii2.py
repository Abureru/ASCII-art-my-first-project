def section(answer,artsection):
    if ans == answer:
      print(dict1[answer])
      print(f"Welcome to the {artsection} section!!! :)")
      choice1 = input("""Would you like your art to be random or see your option?
      (a) random
      (b) see my option
       Answer here: """)
      while choice1 not in 'ab':
          choice1 = input("Error T^T!!! Try again: ")
      return choice1
    
def ran(dic):
    print("You chose random!")
    import random
    num = random.randint(1,3)
    if num == 1:
      return(dic['a'])
    elif num == 2:
      return(dic['b'])
    elif num == 3:
      return(dic['c'])
    
def option(dic):
      option1 = input("Input your option: ")
      while option1 not in 'abc':
          option1 = input("Error T^T!!! Try again: ")
      return(dic[option1])  
      
dict1 = {'a': """                _                 _
     __ _ ____ (_)_ __ ___   __ _| |___ 
    / _` | '_ \| | '_ ` _ \ / _` | / __|
   | (_| | | | | | | | | | | (_| | \__ \
   
    \__,_|_| |_|_|_| |_| |_|\__,_|_|___/
  """,
         'b': """                        _        
    _ __ ___  _   _ ___(_) ___ 
   | '_ ` _ \| | | / __| |/ __|
   | | | | | | |_| \__ \ | (__ 
   |_| |_| |_|\__,_|___/_|\___|
  """,
         'c':"""          _             _       
    _ __ | | __ _ _ __ | |_ ___ 
   | '_ \| |/ _` | '_ \| __/ __|
   | |_) | | (_| | | | | |_\__ \
  
   | .__/|_|\__,_|_| |_|\__|___/
   |_|                          
  """,
         'd':"""                    
  _           _ _     _ _                       
 | |__  _   _(_) | __| (_)_ __   __ _ ___   
 | '_ \| | | | | |/ _` | | '_ \ / _` / __|  
 | |_) | |_| | | | (_| | | | | | (_| \__ \ 
 |_.__/ \__,_|_|_|\__,_|_|_| |_|\__, |___/ 
                                |___/                                  
  """}


dict_animal = {'a': """   Cat :333
 |\__/,|   (`\
 
 |_ _  |.--.) )
 ( T   )     /
(((^_(((/(((_/
""",
         'b': """   Dog :333
        .-"-.
       /|6 6|\
    
      {/(_0_)\}
       _/ ^ \_
      (/ /^\ \)-'
       ""' '""
""",
         'c':"""   Wolf :333
                     .
                    / V \
                
                  / `  /
                 <<   |
                 /    |
               /      |
             /        |
           /    \  \ /
          (      ) | |
  ________|   _/_  | |
<__________\______)\__)

"""}


dict_music = {'a': """   Drum :333
======o     o======
   ___________
  |___________|  
   |\  /\  /\|
   |_\/__\/__|
  |___________| 
  """,
         'b': """   Trumpet :333
                     /|
       =  =  =      / |
  ____| || || |____/  | -_-_-_-_-_-_
|)----| || || |____   |     
  ((  | || || |  ))\  | _-_-_-_-_-_-
   \\_|_||_||_|_//  \ |
    \___________/    \|
""",
         'c':"""   Guitar :333
   _______       __
 /   ------.   / ._`_
|  /         ~--~    \\
| |             __    `.____________________ _^-----^
| |  I=|=======/--\=========================| o o o |
\ |  I=|=======\__/=========================|_o_o_o_|
 \|                   /                       ~    ~
   \       .---.    .
     -----'     ~~''

"""}

dict_plant = {'a' : """   Maple leaf :333
     .\^/.          
   . |`|/| .         
   |\|\|'|/|         
.--'-\`|/-''--.      
 \`-._\|./.-'/       
  >`-._|/.-'<         
 '~|/~~|~~\|~'       
       |
""",
         'b': """   Rose :333
    _,--._.-,
   /\_r-,\_ )
.-.) _;='_/ (.;
 \ \'     \/S )
  L.'-. _.'|-'
 <_`-'\'_.'/
   `'-._( \\
    ___   \\\,      ___
    \ .'-. \\\   .-'_. /
     '._' '.\\\/.-'_.'
        '--``\\('--'
              \\\\
              `\\\,
                \|
""",
         'c':"""   Cactus :333
                     
    ,*-.
    |  |
,.  |  |
| |_|  | ,.
`---.  |_| |
    |  .--`
    |  |
    |  | 
"""}

dict_building = {'a': """   House :333
       _
     _|=|__________
    /              \\
   /                \\
  /__________________\\
   ||  || /--\ ||  ||
   ||[]|| | .| ||[]||
 ()||__||_|__|_||__||()
( )|-|-|-|====|-|-|-|( ) 
^^^^^^^^^^====^^^^^^^^^^^

""",
         'b': """   Castle :333
               T~~
               |
              /"\\
      T~~     |'| T~~
  T~~ |    T~ WWWW|
  |  /"\   |  |  |/\T~~
 /"\ WWW  /"\ |' |WW|
WWWWW/\| /   \|'/\|/"\\
|   /__\/]WWW[\/__\WWWW
|"  WWWW'|I_I|'WWWW'  |
|   |' |/  -  \|' |'  |
|'  |  |LI=H=LI|' |   |
|   |' | |[_]| |  |'  |
|   |  |_|###|_|  |   |
'---'--'-/___\-'--'---'
""",
         'c':"""   Here is your lighthouse :333
  /^\\
  |#|
 |===|
  |0|
  | |
 =====
_||_||_
-------
"""}

print("""Welcome to Ascii Art generator!!!
    (a) Animals
    (b) Music instruments
    (c) Plants
    (d) Buildings""")
ans = input('Choose a category you would like and input its alphabet: ')
dict_start = {'a':'animal', 'b':'music', 'c':'plant', 'd':'music'}

while ans not in 'abcd':
  ans = input('Error T^T!!! Try again: ')
  
choice1 = section(ans, dict_start[ans])
if ans == 'a':
  if choice1 == 'a':
    print(ran(dict_animal))
  elif choice1 == 'b':
      print("""
        (a) Cat
        (b) Dog
        (c) Wolf
        """)
      print (option(dict_animal))

elif ans == 'b':
  if choice1 == 'a':
    print(ran(dict_music))
  elif choice1 == 'b':
      print("""
        (a) Drum
        (b) Trumpet
        (c) Guitar
        """)
      print (option(dict_music))
     
elif ans == 'c':
  if choice1 == 'a':
    print(ran(dict_plant))
  elif choice1 == 'b':
      print("""
        (a) Maple leaf
        (b) Rose
        (c) Cactus
        """)
      print (option(dict_plant))
 
elif ans == 'd':
  while choice1 not in 'ab':
      choice1 = input("Error T^T!!! Try again: ")
  if choice1 == 'a':
    print(ran(dict_building))
  elif choice1 == 'b':
      print("""
        (a) House
        (b) Castle
        (c) Lighthouse
        """)
      print (option(dict_building))
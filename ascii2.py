def section(ans):
    if ans == ans:
      print("""                _                 _
         __ _ ____ (_)_ __ ___   __ _| |___ 
        / _` | '_ \| | '_ ` _ \ / _` | / __|
       | (_| | | | | | | | | | | (_| | \__ \
       
        \__,_|_| |_|_|_| |_| |_|\__,_|_|___/
      """)
      print("Welcome to the animal section!!! :)")
      choice1 = input("""Would you like your art to be random or see your option?
      (a) random
      (b) see my option
       Answer here: """)

# efficient way should i use a libary for this?

print("""Welcome to Ascii Art generator!!!
    (a) Animals
    (b) Music instruments
    (c) Plants
    (d) Buildings""")
ans = input('Choose a category you would like and input its alphabet: ')

if ans == 'a':
  print("""                _                 _
     __ _ ____ (_)_ __ ___   __ _| |___ 
    / _` | '_ \| | '_ ` _ \ / _` | / __|
   | (_| | | | | | | | | | | (_| | \__ \
   
    \__,_|_| |_|_|_| |_| |_|\__,_|_|___/
  """)
  print("Welcome to the animal section!!! :)")
  choice1 = input("""Would you like your art to be random or see your option?
  (a) random
  (b) see my option
   Answer here: """)
  if choice1 == 'a':
    import random
    num = random.randint(1,3)
    if num == 1:
      print("""   OMG it is a cat :333
 |\__/,|   (`\
 
 |_ _  |.--.) )
 ( T   )     /
(((^_(((/(((_/
""")
    elif num == 2:
      print("""   OMG it is a dog :333
        .-"-.
       /|6 6|\
    
      {/(_0_)\}
       _/ ^ \_
      (/ /^\ \)-'
       ""' '""
""")
    elif num == 3:
      print("""   OMG it is a wolf :333
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

""")
  elif choice1 == 'b':
      print("""
        (a) cat
        (b) dog
        (c) wolf
        """)
      option1 = input("Input your option: ")
      if option1 == 'a':
        print("""   Here is your cat :333
 |\__/,|   (`\
 
 |_ _  |.--.) )
 ( T   )     /
(((^_(((/(((_/
""")
      elif option1 == 'b':
        print("""   Here is your dog :333
        .-"-.
       /|6 6|\
    
      {/(_0_)\}
       _/ ^ \_
      (/ /^\ \)-'
       ""' '""
""")
      elif option1 == 'c':
        print("""   Here is your wolf :333
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

""")
      
  else:
      print("error")
      
elif ans == 'b':
  print("""                        _        
    _ __ ___  _   _ ___(_) ___ 
   | '_ ` _ \| | | / __| |/ __|
   | | | | | | |_| \__ \ | (__ 
   |_| |_| |_|\__,_|___/_|\___|
  """) 
  print("Welcome to the music section!!! :)")
  choice1 = input("""Would you like your art to be random or see your option?
  (a) random
  (b) see my option
   Answer here: """)
  
  
  if choice1 == 'a':
    import random
    num = random.randint(1,3)
    if num == 1:
      print("""   OMG it is a drum :333
======o     o======
   ___________
  |___________|  
   |\  /\  /\|
   |_\/__\/__|
  |___________| 
  """)
    elif num == 2:
      print("""   OMG it is a trumpet :333
                     /|
       =  =  =      / |
  ____| || || |____/  | -_-_-_-_-_-_
|)----| || || |____   |     
  ((  | || || |  ))\  | _-_-_-_-_-_-
   \\_|_||_||_|_//  \ |
    \___________/    \|
""")
    elif num == 3:
      print("""   OMG it is a guitar :333
   _______       __
 /   ------.   / ._`_
|  /         ~--~    \
| |             __    `.____________________ _^-----^
| |  I=|=======/--\=========================| o o o |
\ |  I=|=======\__/=========================|_o_o_o_|
 \|                   /                       ~    ~
   \       .---.    .
     -----'     ~~''

""")
  elif choice1 == 'b':
      print("""
        (a) drum
        (b) trumpet
        (c) guitar
        """)
      option1 = input("Input your option: ")
      if option1 == 'a':
        print("""   Here is your cat :333
======o     o======
   ___________
  |___________|  
   |\  /\  /\|
   |_\/__\/__|
  |___________| 
""")
      elif option1 == 'b':
        print("""   Here is your dog :333
                     /|
       =  =  =      / |
  ____| || || |____/  | -_-_-_-_-_-_
|)----| || || |____   |     
  ((  | || || |  ))\  | _-_-_-_-_-_-
   \\_|_||_||_|_//  \ |
    \___________/    \|
""")
      elif option1 == 'c':
        print("""   Here is your guitar :333
   _______       __
 /   ------.   / ._`_
|  /         ~--~    \
| |             __    `.____________________ _^-----^
| |  I=|=======/--\=========================| o o o |
\ |  I=|=======\__/=========================|_o_o_o_|
 \|                   /                       ~    ~
   \       .---.    .
     -----'     ~~''
""")
      
  else:
      print("error")
elif ans == 'c':
  print("""          _             _       
    _ __ | | __ _ _ __ | |_ ___ 
   | '_ \| |/ _` | '_ \| __/ __|
   | |_) | | (_| | | | | |_\__ \
  
   | .__/|_|\__,_|_| |_|\__|___/
   |_|                          
  """)
  print("Welcome to the plants section!!! :)")
  choice1 = input("""Would you like your art to be random or see your option?
  (a) random
  (b) see my option
   Answer here: """)
  if choice1 == 'a':
    import random
    num = random.randint(1,3)
    if num == 1:
      print("""   OMG it is a maple leaf :333
     .\^/.          
   . |`|/| .         
   |\|\|'|/|         
.--'-\`|/-''--.      
 \`-._\|./.-'/       
  >`-._|/.-'<         
 '~|/~~|~~\|~'       
       |
""")
    elif num == 2:
      print("""   OMG it is a rose :333
    _,--._.-,
   /\_r-,\_ )
.-.) _;='_/ (.;
 \ \'     \/S )
  L.'-. _.'|-'
 <_`-'\'_.'/
   `'-._( \
    ___   \\,      ___
    \ .'-. \\   .-'_. /
     '._' '.\\/.-'_.'
        '--``\('--'
              \\
              `\\,
                \|
""")
    elif num == 3:
      print("""   OMG it is a cactus :333
                     .
    ,*-.
    |  |
,.  |  |
| |_|  | ,.
`---.  |_| |
    |  .--`
    |  |
    |  | 

""")
  elif choice1 == 'b':
      print("""
        (a) maple leaf
        (b) rose
        (c) cactus
        """)
      option1 = input("Input your option: ")
      if option1 == 'a':
        print("""   Here is your maple leaf :333
     .\^/.          
   . |`|/| .         
   |\|\|'|/|         
.--'-\`|/-''--.      
 \`-._\|./.-'/       
  >`-._|/.-'<         
 '~|/~~|~~\|~'       
       |
""")
      elif option1 == 'b':
        print("""   Here is your rose :333
    _,--._.-,
   /\_r-,\_ )
.-.) _;='_/ (.;
 \ \'     \/S )
  L.'-. _.'|-'
 <_`-'\'_.'/
   `'-._( \
    ___   \\,      ___
    \ .'-. \\   .-'_. /
     '._' '.\\/.-'_.'
        '--``\('--'
              \\
              `\\,
                \|
""")
      elif option1 == 'c':
        print("""   Here is your cactus :333
    ,*-.
    |  |
,.  |  |
| |_|  | ,.
`---.  |_| |
    |  .--`
    |  |
    |  | 
""")
  else:
      print("error")
      
elif ans == 'd':
  print("""                    
  _           _ _     _ _                       
 | |__  _   _(_) | __| (_)_ __   __ _ ___   
 | '_ \| | | | | |/ _` | | '_ \ / _` / __|  
 | |_) | |_| | | | (_| | | | | | (_| \__ \ 
 |_.__/ \__,_|_|_|\__,_|_|_| |_|\__, |___/ 
                                |___/                                  
  """)  

  print("Welcome to the buildings section!!! :)")
  choice1 = input("""Would you like your art to be random or see your option?
  (a) random
  (b) see my option
   Answer here: """)
  if choice1 == 'a':
    import random
    num = random.randint(1,3)
    if num == 1:
      print("""   OMG it is a castle :333
               T~~
               |
              /"\
      T~~     |'| T~~
  T~~ |    T~ WWWW|
  |  /"\   |  |  |/\T~~
 /"\ WWW  /"\ |' |WW|
WWWWW/\| /   \|'/\|/"\
|   /__\/]WWW[\/__\WWWW
|"  WWWW'|I_I|'WWWW'  |
|   |' |/  -  \|' |'  |
|'  |  |LI=H=LI|' |   |
|   |' | |[_]| |  |'  |
|   |  |_|###|_|  |   |
'---'--'-/___\-'--'---'
""")
    elif num == 2:
      print("""   OMG it is a lighthouse :333
  /^\
  |#|
 |===|
  |0|
  | |
 =====
_||_||_
-------
""")
    elif num == 3:
      print("""   OMG it is a house :333
     _
     _|=|__________
    /              \
   /                \
  /__________________\
   ||  || /--\ ||  ||
   ||[]|| | .| ||[]||
 ()||__||_|__|_||__||()
( )|-|-|-|====|-|-|-|( ) 
^^^^^^^^^^====^^^^^^^^^^^

""")
  elif choice1 == 'b':
      print("""
        (a) castle
        (b) lighthouse
        (c) house
        """)
      option1 = input("Input your option: ")
      if option1 == 'a':
        print("""   Here is your cat :333
               T~~
               |
              /"\
      T~~     |'| T~~
  T~~ |    T~ WWWW|
  |  /"\   |  |  |/\T~~
 /"\ WWW  /"\ |' |WW|
WWWWW/\| /   \|'/\|/"\
|   /__\/]WWW[\/__\WWWW
|"  WWWW'|I_I|'WWWW'  |
|   |' |/  -  \|' |'  |
|'  |  |LI=H=LI|' |   |
|   |' | |[_]| |  |'  |
|   |  |_|###|_|  |   |
'---'--'-/___\-'--'---'
""")
      elif option1 == 'b':
        print("""   Here is your lighthouse :333
  /^\
  |#|
 |===|
  |0|
  | |
 =====
_||_||_
-------
""")
      elif option1 == 'c':
        print("""   Here is your wolf :333
     _
     _|=|__________
    /              \
   /                \
  /__________________\
   ||  || /--\ ||  ||
   ||[]|| | .| ||[]||
 ()||__||_|__|_||__||()
( )|-|-|-|====|-|-|-|( ) 
^^^^^^^^^^====^^^^^^^^^^^

""")
      
  else:
      print("error")
else:
  print('Error')
  input('Try again')
      

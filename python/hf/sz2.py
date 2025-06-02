text = input()
length = int(text.count(' '))

if length==1:
    article_1, noun = text.split( )
    if article_1 == "l'" :
        print(f"{noun}: a szó nemét nem tudjuk a névelő alapján megmondani.")
    elif article_1 == "la" or article_1 == "une" :
        print(f"{noun}: nőnemű főnév.")
    elif article_1 == "le" or article_1 == "du" or article_1 == "au" or article_1 == "un":
        print(f"{noun}: hímnemű főnév.")
    else: 
        print('Hibás névelő.')

elif length==2:
    article_1, arcticle_2, noun = text.split( )
    if article_1 + " " + arcticle_2 == "à l'" or article_1 + " " + arcticle_2 == "de l'" :
        print(f"{noun}: a szó nemét nem tudjuk a névelő alapján megmondani.")
    elif article_1 + " " + arcticle_2 == "de la" or article_1 + " " + arcticle_2 == "à la" : 
        print(f"{noun}: nőnemű főnév.")
    else : 
        print('Hibás névelő.')
    

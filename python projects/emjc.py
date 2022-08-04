# def emojie(text):
#     msg = text.split(" ")
#     emojie = {":)" : "😀" , ":(" : "😔"}

#     output = ""
#     for N in msg:
#             output += emojie.get(N , N) +" "
#             return output

# text = input("Enter text : ")

# emojie(text=text)

class Emojie():
    def emojie(self , text):
        msg = text.split(" ")
        emojie = {":)" : "😀" , ":(" : "😔"}

        output = ""
        for N in msg:
                output += emojie.get(N , N) +" "
                return output

texti = "messagenigga :)"

Emojiee = Emojie()

Emojiee.emojie(texti)



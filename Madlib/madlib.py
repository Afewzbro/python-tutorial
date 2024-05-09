# # STRING CONCATENATION (AKA HOW TO PUT STRINGS TOGETHER)
# # SUPPOSE WE WANT TO CREATE A STRING THAT SAYS "sUBSCRIBE TO _____"
# youtuber = "AfewZBro" # SOME STRING VARIABLE

# # A FEW WAYS TO DO THIS
# print("subscribe to "+ youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person= input("Famous person: ")

madlib= f"Computer programming is so {adj}! it makes me so excited all the time because\
    i love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
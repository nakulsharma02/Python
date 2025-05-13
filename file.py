# r = open('text.txt')
# data = r.read()
# import pyttsx3
# engine=pyttsx3.init()
# engine.say(data)
# engine.runAndWait()
# r.close()
# st=input("Give Your intro here")
# w = open('text.txt','w')
# w.write(st)
# w.close()

##The same can be written using 'with' statement like this:
with open("text.txt") as f:
    print(f.read())

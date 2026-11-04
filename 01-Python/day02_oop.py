# class Chatbot :
#     pass
 
# #creating objects
# chatbot1 = Chatbot()
# chatbot2 = Chatbot()

# print(chatbot1)
# print(chatbot2)

class Chatbot:

    def __init__(self, name, model):
        self.name = name
        self.model = model


chatbot1 = Chatbot("LOOMA", "GPT")
chatbot2 = Chatbot("Raghu AI", "Custom Model")

print("Chatbot 1:", chatbot1.name)
print("Model:", chatbot1.model)

print("Chatbot 2:", chatbot2.name)
print("Model:", chatbot2.model)


class Chatbot:

    def __init__(self, name, model):
        self.name = name
        self.model = model

    def introduce(self):
        print("Hello! I am", self.name)
        print("I am powered by", self.model)


chatbot1 = Chatbot("LOOMA", "GPT")
chatbot2 = Chatbot("Raghu AI", "Custom Model")

chatbot1.introduce()
chatbot2.introduce()
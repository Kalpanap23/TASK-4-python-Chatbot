import random

class ChatBot:
    def __init__(self):
        self.intents = {
            "greeting": {
                "keywords": ["hi", "hello", "hey", "good morning", "good evening"],
                "responses": ["Hello! 😊", "morning", "Hey there!", "Hi! How can I help you?", "I'am fine thanks"]
            },
            "name": {
                "keywords": ["your name", "who are you"],
                "responses": ["I'm PyBot 🤖, your assistant!", "You can call me PyBot."]
            },
            "help": {
                "keywords": ["help", "support", "what can you do"],
                "responses": ["I can chat with you, answer basic questions, and help you learn Python!"]
            },
            "bye": {
                "keywords": ["bye", "exit", "quit"],
                "responses": ["Goodbye! 👋", "See you soon!", "Bye! Have a great day!"]
            }
        }

    def get_response(self, user_input):
        user_input = user_input.lower()

        best_match = None
        max_score = 0

        # Check all intents
        for intent, data in self.intents.items():
            score = sum(1 for word in data["keywords"] if word in user_input)

            if score > max_score:
                max_score = score
                best_match = intent

        if best_match:
            return random.choice(self.intents[best_match]["responses"])
        else:
            return "I'm not sure I understand 🤔. Try asking something else!"

    def run(self):
        print("🤖 PyBot: Hello! Type 'bye' to exit.\n")

        while True:
            user_input = input("You: ")

            response = self.get_response(user_input)
            print("PyBot:", response)

            if "bye" in user_input.lower() or "exit" in user_input.lower():
                break


# Run chatbot
if __name__ == "__main__":
    bot = ChatBot()
    bot.run()
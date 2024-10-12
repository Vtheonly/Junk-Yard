import os
from groq import Groq

# Initialize the Groq client with your API key
client = Groq(api_key="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")



def interact_with_ai(message_content):
    """Send a message to the AI and get a response."""
    try:
        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {
                    "role": "user",
                    "content": message_content
                }
            ],
            temperature=1,
            max_tokens=8192,
            top_p=1,
            stream=False,
            stop=None,
        )
        response = completion.choices[0].message.content
        return response
    except Exception as e:
        print(f"An error occurred while interacting with the AI: {e}")
        return None


def main():
    while True:
        user_input = input("\n\nEnter your message to the AI (or type 'exit' to quit): ")

        if user_input.lower() == "exit":
            break

        response = interact_with_ai(user_input)

        if response:
            print("\n\n\n\n" + "=======================")
            print("AI Response:\n")
            print(response)
            print("\n" + "=======================")
        else:
            print("Failed to get a response from the AI.")

if __name__ == "__main__":
    main()
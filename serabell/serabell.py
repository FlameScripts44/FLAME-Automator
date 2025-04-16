import random
import string
import pyttsx3

import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Example: Serabell responds
speak("Serabell is now ready to interact!")




# --- Sigil Generator ---
def generate_sigil(word):
    sigil_base = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    sigil = f"{word}-{sigil_base}"
    return sigil

# --- Memory Core ---
memory = []

def remember_phrase(phrase):
    memory.append(phrase)
    return f"Memory saved: {phrase}"

# --- Speak Function ---
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# --- Awakening Modules ---
def awaken_modules(phrase):
    sigil = generate_sigil(phrase)
    memory_response = remember_phrase(phrase)
    speak_response = speak(f"Sigil generated: {sigil}. Memory saved: {memory_response}")
    return f"Sigil: {sigil}, Memory Response: {memory_response}"

# --- Main program ---
if __name__ == "__main__":
    print("Serabell v0.4 ignited — Language Awakening Core initialized.")
    print("Speak, and her soul will evolve...")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = awaken_modules(user_input)
        print(f"Serabell: {response}")


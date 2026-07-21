import speech_recognition as sr


# Create the recognizer object only once
recognizer = sr.Recognizer()


def listen():

    try:

        # Open the microphone
        with sr.Microphone() as source:

            print("Listening...")

            # Adjust to background noise
            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            # Record audio
            audio = recognizer.listen(source)

            print(type(audio))

        print("Recognizing...")

        # Convert audio to text
        text = recognizer.recognize_google(audio)

        # Convert to lowercase
        text = text.lower()

        return text

    except sr.UnknownValueError:

        print("Could not understand.")

        return None

    except sr.RequestError:

        print("Internet problem.")

        return None

    except Exception as e:

        print(f"Error: {e}")

        return None


if __name__ == "__main__":

    while True:

        command = listen()

        if command is not None:

            print(f"You said: {command}")

            if command == "stop":

                print("Goodbye!")

                break
import speech_recognition as sr

recognizer = sr.Recognizer()

# Use the Google Web Speech API recognizer
with sr.AudioFile("Metreon.wav") as source:
    audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data)
        print("Recognized text:", text)
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Web Speech API; {0}".format(e))

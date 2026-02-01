import speech_recognition as sr

r = sr.Recognizer()

try:
    with sr.AudioFile("sample.wav") as source:
        audio = r.record(source)

    text = r.recognize_google(audio, language="en-IN")
    print("You said:", text)

except sr.UnknownValueError:
    print("Speech was not clear, could not recognize.")

except sr.RequestError:
    print("Network error or Google API issue.")
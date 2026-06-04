import mediapipe as mp

print("Version:", mp.__version__)
print("Module:", mp.__file__)
print("Has solutions:", hasattr(mp, "solutions"))

try:
    print(mp.solutions)
except Exception as e:
    print("Error:", e)
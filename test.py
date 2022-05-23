from pocketsphinx import LiveSpeech, get_model_path, get_data_path

print(get_model_path())
print(get_data_path())

for phrase in LiveSpeech():
    print(phrase)
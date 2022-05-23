from pocketsphinx import LiveSpeech

acoust = 'en-us'
langmo = 'en-us.lm.bin'
phonet = 'cmudict-en-us.dict'

recognizer = LiveSpeech(verbose = False, sampling_rate=16000, buffer_size=2048, no_search=False, full_utt=False, hmm=acoust, lm=langmo, dic=phonet)

for phrase in recognizer:
    print(phrase)
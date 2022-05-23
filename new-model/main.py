import os
from pocketsphinx import Pocketsphinx, LiveSpeech, AudioFile, get_model_path, get_data_path

# acoust = 'en-us'
# langmo = 'en-us.lm.bin'
# phonet = 'cmudict-en-us.dict'


acoust = 'an4.ci_cont'
langmo = 'en-us.lm.bin'
phonet = 'cmudict-en-us.dict'


model_path = get_model_path()
data_path = get_data_path()

print('data path',data_path)
# recognizer = LiveSpeech(verbose = False, sampling_rate=16000, buffer_size=2048, no_search=False, full_utt=False, hmm=acoust, lm=langmo, dic=phonet)

# for phrase in recognizer:
#     print(phrase)


config = {
    # 'hmm': os.path.join(model_path, acoust),
    'hmm': os.path.join(os.getcwd(), acoust),
    # 'hmm': acoust,
    'lm': os.path.join(model_path, langmo),
    'dict': os.path.join(model_path, phonet)
}
print(config)

data_dir = os.path.join(os.getcwd(), 'data')

ps = Pocketsphinx(**config)
for file_audio in data_dir:
    ps.decode(
        # audio_file=os.path.join(data_path, 'goforward.raw'),
        audio_file=file_audio,
        buffer_size=2048,
        no_search=False,
        full_utt=False
    )

# print(ps.segments()) # => ['<s>', '<sil>', 'go', 'forward', 'ten', 'meters', '</s>']
# print('Detailed segments:', *ps.segments(detailed=True), sep='\n') # => [
# #     word, prob, start_frame, end_frame
# #     ('<s>', 0, 0, 24)
# #     ('<sil>', -3778, 25, 45)
# #     ('go', -27, 46, 63)
# #     ('forward', -38, 64, 116)
# #     ('ten', -14105, 117, 152)
# #     ('meters', -2152, 153, 211)
# #     ('</s>', 0, 212, 260)
# # ]

# print(ps.hypothesis())  # => go forward ten meters
# print(ps.probability()) # => -32079
# print(ps.score())       # => -7066
# print(ps.confidence())  # => 0.04042641466841839


# model_path = get_model_path()
# data_path = get_data_path()

# config = {
#     'verbose': False,
#     'audio_file': os.path.join(data_path, 'goforward.raw'),
#     'buffer_size': 2048,
#     'no_search': False,
#     'full_utt': False,
#     'hmm': os.path.join(model_path, 'en-us'),
#     'lm': os.path.join(model_path, 'en-us.lm.bin'),
#     'dict': os.path.join(model_path, 'cmudict-en-us.dict')
# }

# audio = AudioFile(**config)
# for phrase in audio:
#     print(phrase)


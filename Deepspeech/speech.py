import argparse
import os

import TTS
from TTS.server.synthesizer import Synthesizer
import librosa
import librosa.display


import IPython
from IPython.display import Audio
#from synthesis import *

def create_argparser():
    def convert_boolean(x):
        return x.lower() in ['true', '1', 'yes']

    parser = argparse.ArgumentParser()
    parser.add_argument('--tts_checkpoint', type=str, default= 'tts_model/checkpoint_130000.pth.tar', help='path to TTS checkpoint file')
    parser.add_argument('--tts_config', type=str, default='tts_model/config.json', help='path to TTS config.json file')
    parser.add_argument('--tts_speakers', type=str, default=None, help='path to JSON file containing speaker ids, if speaker ids are used in the model')
    parser.add_argument('--wavernn_lib_path', type=str, default=None, help='path to WaveRNN project folder to be imported. If this is not passed, model uses Griffin-Lim for synthesis.')
    parser.add_argument('--wavernn_file', type=str, default=None, help='path to WaveRNN checkpoint file.')
    parser.add_argument('--wavernn_config', type=str, default=None, help='path to WaveRNN config file.')
    parser.add_argument('--is_wavernn_batched', type=convert_boolean, default=False, help='true to use batched WaveRNN.')
    parser.add_argument('--pwgan_lib_path', type=str, default=None, help='path to ParallelWaveGAN project folder to be imported. If this is not passed, model uses Griffin-Lim for synthesis.')
    parser.add_argument('--pwgan_file', type=str, default=None, help='path to ParallelWaveGAN checkpoint file.')
    parser.add_argument('--pwgan_config', type=str, default=None, help='path to ParallelWaveGAN config file.')
    parser.add_argument('--use_cuda', type=convert_boolean, default=False, help='true to use CUDA.')
    parser.add_argument('--text', type=str, help='input file to read text from')
    parser.add_argument('--out', type=str, default="output.wav", help='output file to save speech as')
    return parser


synthesizer = None

embedded_models_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'model')

embedded_tts_folder = os.path.join(embedded_models_folder, 'tts')
tts_checkpoint_file = os.path.join(embedded_tts_folder, 'checkpoint.pth.tar')
tts_config_file = os.path.join(embedded_tts_folder, 'config.json')

embedded_wavernn_folder = os.path.join(embedded_models_folder, 'wavernn')
wavernn_checkpoint_file = os.path.join(embedded_wavernn_folder, 'checkpoint.pth.tar')
wavernn_config_file = os.path.join(embedded_wavernn_folder, 'config.json')

embedded_pwgan_folder = os.path.join(embedded_models_folder, 'pwgan')
pwgan_checkpoint_file = os.path.join(embedded_pwgan_folder, 'checkpoint.pkl')
pwgan_config_file = os.path.join(embedded_pwgan_folder, 'config.yml')

args = create_argparser().parse_args()

# If these were not specified in the CLI args, use default values with embedded model files
if not args.tts_checkpoint and os.path.isfile(tts_checkpoint_file):
    args.tts_checkpoint = tts_checkpoint_file
if not args.tts_config and os.path.isfile(tts_config_file):
    args.tts_config = tts_config_file
if not args.wavernn_file and os.path.isfile(wavernn_checkpoint_file):
    args.wavernn_file = wavernn_checkpoint_file
if not args.wavernn_config and os.path.isfile(wavernn_config_file):
    args.wavernn_config = wavernn_config_file
if not args.pwgan_file and os.path.isfile(pwgan_checkpoint_file):
    args.pwgan_file = pwgan_checkpoint_file
if not args.pwgan_config and os.path.isfile(pwgan_config_file):
    args.pwgan_config = pwgan_config_file

from utils.audio import AudioProcessor

import torch

args.vocoder_checkpoint = False
#cp = torch.load('best_model.pth.tar')
synthesizer = Synthesizer(args)
#synthesizer.config = args
#synthesizer.use_cuda = False
#synthesizer.ap = AudioProcessor(**config.audio)
#synthesizer.model = Tacotron(config.embedding_size, self.ap.num_freq, self.ap.num_mels, config.r)
#synthesizer.load_model('tts_model', 'checkpoint_130000.pth.tar', 'config.json', False)
#with open(args.text, "r") as f:
#    text = f.read()
text = 'This is an example'
data = synthesizer.tts(text)

with open(args.out, "wb") as f:
    f.write(data.getbuffer())

import os.path as osp

from openvino.inference_engine import IECore
from argparse import ArgumentParser, SUPPRESS


class ForwardTacotronIE:
    def __init__(self, model, ie, device='CPU', verbose=False):
        self.verbose = verbose
        self.device = device

        self.ie = ie

        self.duration_predictor_net = self.load_network(model)
        self.duration_predictor_exec = self.create_exec_network(self.duration_predictor_net)


    def load_network(self, model_xml):
        model_bin_name = ".".join(osp.basename(model_xml).split('.')[:-1]) + ".bin"
        model_bin = osp.join(osp.dirname(model_xml), model_bin_name)
        print("Loading network files:\n\t{}\n\t{}".format(model_xml, model_bin))
        net = self.ie.read_network(model=model_xml, weights=model_bin)
        return net

    def create_exec_network(self, net):
        exec_net = self.ie.load_network(network=net, device_name=self.device)
        return exec_net

def build_argparser():
    parser = ArgumentParser(add_help=False)
    args = parser.add_argument_group('Options')
    args.add_argument('-h', '--help', action='help', default=SUPPRESS, help='Show this help message and exit.')
    args.add_argument("-m_duration", "--model_duration",
                      help="Required. Path to ForwardTacotron`s duration prediction part (*.xml format).",
                      required=True, type=str)
    args.add_argument("-m_forward", "--model_forward",
                      help="Required. Path to ForwardTacotron`s mel-spectrogram regression part (*.xml format).",
                      required=False, type=str)
    args.add_argument("-i", "--input", help="Text file with text.", required=False,
                      type=str)
    args.add_argument("-o", "--out", help="Required. Path to an output .wav file", default='out.wav',
                      type=str)

    args.add_argument("-d", "--device",
                      help="Optional. Specify the target device to infer on; CPU, GPU, HDDL, MYRIAD or HETERO is "
                           "acceptable. The demo will look for a suitable plugin for device specified. "
                           "Default value is CPU",
                      default="CPU", type=str)

    args.add_argument("-m_upsample", "--model_upsample",
                      help="Path to WaveRNN`s part for mel-spectrogram upsampling "
                           "by time axis (*.xml format).",
                      default=None, required=False, type=str)
    args.add_argument("-m_rnn", "--model_rnn",
                      help="Path to WaveRNN`s part for waveform autoregression (*.xml format).",
                      default=None, required=False, type=str)
    args.add_argument("--upsampler_width", default=-1,
                      help="Width for reshaping of the model_upsample in WaveRNN vocoder. "
                           "If -1 then no reshape. Do not use with FP16 model.",
                      required=False,
                      type=int)

    args.add_argument("-m_melgan", "--model_melgan",
                      help="Path to model of the MelGAN (*.xml format).",
                      default=None, required=False,
                      type=str)

    args.add_argument("-s_id", "--speaker_id",
                      help="Ordinal number of the speaker in embeddings array for multi-speaker model. "
                           "If -1 then activates the multi-speaker TTS model parameters selection window.",
                      default=19, required=False,
                      type=int)

    args.add_argument("-a", "--alpha",
                      help="Coefficient for controlling of the speech time (inversely proportional to speed).",
                      default=1.0, required=False,
                      type=float)

    return parser
args = build_argparser().parse_args()
ie = IECore()
ForwardTacotronIE(args.model_duration, ie, args.device, verbose=False)
ForwardTacotronIE(args.model_forward, ie, args.device, verbose=False)

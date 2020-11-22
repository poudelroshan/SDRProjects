#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun Nov 22 14:37:36 2020
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import audio
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import iio
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self, audio_device='default', decimation=1, fm_station=100.1e6, uri='ip:pluto.local'):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "C:\Program Files\GNURadio-3.7\share\icons\hicolor\scalable/apps\gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Parameters
        ##################################################
        self.audio_device = audio_device
        self.decimation = decimation
        self.fm_station = fm_station
        self.uri = uri

        ##################################################
        # Variables
        ##################################################
        self.sample_rate = sample_rate = 2800000

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=106.1e6,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=sample_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='FFT Plot',
        	peak_hold=False,
        	win=window.flattop,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.pluto_source_0 = iio.pluto_source(uri, 106100000, sample_rate, 20000000, 0x20000, True, True, True, "manual", 64.0, '', True)
        self.low_pass_filter_0 = filter.fir_filter_ccf(sample_rate / (384000 * decimation), firdes.low_pass(
        	1, sample_rate / decimation, 44100, 44100, firdes.WIN_HAMMING, 6.76))
        self.audio_sink_0 = audio.sink(48000, audio_device, True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=384000,
        	audio_decimation=8,
        )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv_0, 0), (self.audio_sink_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.pluto_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.pluto_source_0, 0), (self.wxgui_fftsink2_0, 0))

    def get_audio_device(self):
        return self.audio_device

    def set_audio_device(self, audio_device):
        self.audio_device = audio_device

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.sample_rate / self.decimation, 44100, 44100, firdes.WIN_HAMMING, 6.76))

    def get_fm_station(self):
        return self.fm_station

    def set_fm_station(self, fm_station):
        self.fm_station = fm_station

    def get_uri(self):
        return self.uri

    def set_uri(self, uri):
        self.uri = uri

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self.wxgui_fftsink2_0.set_sample_rate(self.sample_rate)
        self.pluto_source_0.set_params(106100000, self.sample_rate, 20000000, True, True, True, "manual", 64.0, '', True)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.sample_rate / self.decimation, 44100, 44100, firdes.WIN_HAMMING, 6.76))


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--audio-device", dest="audio_device", type="string", default='default',
        help="Set Audio device [default=%default]")
    parser.add_option(
        "", "--decimation", dest="decimation", type="intx", default=1,
        help="Set Decimation [default=%default]")
    parser.add_option(
        "", "--fm-station", dest="fm_station", type="eng_float", default=eng_notation.num_to_str(100.1e6),
        help="Set FM station [default=%default]")
    parser.add_option(
        "", "--uri", dest="uri", type="string", default='ip:pluto.local',
        help="Set URI [default=%default]")
    return parser


def main(top_block_cls=top_block, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable real-time scheduling."

    tb = top_block_cls(audio_device=options.audio_device, decimation=options.decimation, fm_station=options.fm_station, uri=options.uri)
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sat Nov 21 23:39:22 2020
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
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "C:\Program Files\GNURadio-3.7\share\icons\hicolor\scalable/apps\gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.volume = volume = 1
        self.shift = shift = 200000
        self.samp_rate = samp_rate = 2e6
        self.gain = gain = 48
        self.freq = freq = 98.5e6
        self.cutoff = cutoff = 75000

        ##################################################
        # Blocks
        ##################################################
        self.Notebook = self.Notebook = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.Notebook.AddPage(grc_wxgui.Panel(self.Notebook), "Tuner")
        self.Notebook.AddPage(grc_wxgui.Panel(self.Notebook), "Audio")
        self.Add(self.Notebook)
        _volume_sizer = wx.BoxSizer(wx.VERTICAL)
        self._volume_text_box = forms.text_box(
        	parent=self.Notebook.GetPage(1).GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	label='volume',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._volume_slider = forms.slider(
        	parent=self.Notebook.GetPage(1).GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	minimum=0,
        	maximum=2,
        	num_steps=10,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Notebook.GetPage(1).Add(_volume_sizer)
        _shift_sizer = wx.BoxSizer(wx.VERTICAL)
        self._shift_text_box = forms.text_box(
        	parent=self.Notebook.GetPage(0).GetWin(),
        	sizer=_shift_sizer,
        	value=self.shift,
        	callback=self.set_shift,
        	label='shift',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._shift_slider = forms.slider(
        	parent=self.Notebook.GetPage(0).GetWin(),
        	sizer=_shift_sizer,
        	value=self.shift,
        	callback=self.set_shift,
        	minimum=0,
        	maximum=400000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Notebook.GetPage(0).Add(_shift_sizer)
        _gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._gain_text_box = forms.text_box(
        	parent=self.Notebook.GetPage(0).GetWin(),
        	sizer=_gain_sizer,
        	value=self.gain,
        	callback=self.set_gain,
        	label='gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._gain_slider = forms.slider(
        	parent=self.Notebook.GetPage(0).GetWin(),
        	sizer=_gain_sizer,
        	value=self.gain,
        	callback=self.set_gain,
        	minimum=0,
        	maximum=50,
        	num_steps=50,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Notebook.GetPage(0).Add(_gain_sizer)
        _freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_text_box = forms.text_box(
        	parent=self.Notebook.GetPage(0).GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	label='freq',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_slider = forms.slider(
        	parent=self.Notebook.GetPage(0).GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	minimum=87e6,
        	maximum=108e6,
        	num_steps=210,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Notebook.GetPage(0).Add(_freq_sizer)
        _cutoff_sizer = wx.BoxSizer(wx.VERTICAL)
        self._cutoff_text_box = forms.text_box(
        	parent=self.Notebook.GetPage(0).GetWin(),
        	sizer=_cutoff_sizer,
        	value=self.cutoff,
        	callback=self.set_cutoff,
        	label='cutoff',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._cutoff_slider = forms.slider(
        	parent=self.Notebook.GetPage(0).GetWin(),
        	sizer=_cutoff_sizer,
        	value=self.cutoff,
        	callback=self.set_cutoff,
        	minimum=0,
        	maximum=2e5,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Notebook.GetPage(0).Add(_cutoff_sizer)
        self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_f(
        	self.Notebook.GetPage(1).GetWin(),
        	baseband_freq=0,
        	dynamic_range=100,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=48000,
        	fft_size=512,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='Waterfall Plot',
        )
        self.Notebook.GetPage(1).Add(self.wxgui_waterfallsink2_0.win)
        self.wxgui_fftsink2_1 = fftsink2.fft_sink_c(
        	self.Notebook.GetPage(0).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=150,
        	average=False,
        	avg_alpha=None,
        	title='FFT Plot',
        	peak_hold=False,
        )
        self.Notebook.GetPage(0).Add(self.wxgui_fftsink2_1.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
        	self.Notebook.GetPage(1).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=48000,
        	fft_size=1024,
        	fft_rate=20,
        	average=False,
        	avg_alpha=None,
        	title='FFT Plot',
        	peak_hold=False,
        )
        self.Notebook.GetPage(1).Add(self.wxgui_fftsink2_0.win)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(freq+shift, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(True, 0)
        self.rtlsdr_source_0.set_gain(gain, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)

        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=int(samp_rate/500e3),
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=48,
                decimation=50,
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, cutoff, cutoff*2, firdes.WIN_HAMMING, 6.76))
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(1, (1, ), -shift, samp_rate)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((volume, ))
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=500000,
        	audio_decimation=10,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.wxgui_waterfallsink2_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.wxgui_fftsink2_1, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self._volume_slider.set_value(self.volume)
        self._volume_text_box.set_value(self.volume)
        self.blocks_multiply_const_vxx_0.set_k((self.volume, ))

    def get_shift(self):
        return self.shift

    def set_shift(self, shift):
        self.shift = shift
        self._shift_slider.set_value(self.shift)
        self._shift_text_box.set_value(self.shift)
        self.rtlsdr_source_0.set_center_freq(self.freq+self.shift, 0)
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(-self.shift)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_fftsink2_1.set_sample_rate(self.samp_rate)
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.cutoff*2, firdes.WIN_HAMMING, 6.76))

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self._gain_slider.set_value(self.gain)
        self._gain_text_box.set_value(self.gain)
        self.rtlsdr_source_0.set_gain(self.gain, 0)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_slider.set_value(self.freq)
        self._freq_text_box.set_value(self.freq)
        self.rtlsdr_source_0.set_center_freq(self.freq+self.shift, 0)

    def get_cutoff(self):
        return self.cutoff

    def set_cutoff(self, cutoff):
        self.cutoff = cutoff
        self._cutoff_slider.set_value(self.cutoff)
        self._cutoff_text_box.set_value(self.cutoff)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.cutoff*2, firdes.WIN_HAMMING, 6.76))


def main(top_block_cls=top_block, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable real-time scheduling."

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()

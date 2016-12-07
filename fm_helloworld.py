#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: ww
# Author: ee
# Description: rr
# Generated: Wed Dec  7 21:16:17 2016
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import wx

class fm_helloworld(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="ww")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.xlate_tune = xlate_tune = 0
        self.usrp_freq = usrp_freq = 93.3e6
        self.transition_slider = transition_slider = 1e3
        self.volume = volume = 3
        self.transition = transition = transition_slider * 1e3
        self.samp_rate = samp_rate = 1e6
        self.rx_freq = rx_freq = usrp_freq+xlate_tune
        self.rf_gain = rf_gain = 20
        self.quadrature = quadrature = 250e3
        self.cutoff = cutoff = 100e3
        self.audio_rate = audio_rate = 48e3

        ##################################################
        # Blocks
        ##################################################
        self.nbook = self.nbook = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.nbook.AddPage(grc_wxgui.Panel(self.nbook), "Receiver")
        self.GridAdd(self.nbook, 0, 0, 5, 5)
        _volume_sizer = wx.BoxSizer(wx.VERTICAL)
        self._volume_text_box = forms.text_box(
        	parent=self.nbook.GetPage(0).GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	label="Volume",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._volume_slider = forms.slider(
        	parent=self.nbook.GetPage(0).GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	minimum=0,
        	maximum=10,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nbook.GetPage(0).GridAdd(_volume_sizer, 5, 0, 1, 5)
        self._rx_freq_static_text = forms.static_text(
        	parent=self.nbook.GetPage(0).GetWin(),
        	value=self.rx_freq,
        	callback=self.set_rx_freq,
        	label="Receive",
        	converter=forms.float_converter(),
        )
        self.nbook.GetPage(0).GridAdd(self._rx_freq_static_text, 0, 0, 1, 1)
        _rf_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rf_gain_text_box = forms.text_box(
        	parent=self.nbook.GetPage(0).GetWin(),
        	sizer=_rf_gain_sizer,
        	value=self.rf_gain,
        	callback=self.set_rf_gain,
        	label="RF Gain",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rf_gain_slider = forms.slider(
        	parent=self.nbook.GetPage(0).GetWin(),
        	sizer=_rf_gain_sizer,
        	value=self.rf_gain,
        	callback=self.set_rf_gain,
        	minimum=0,
        	maximum=50,
        	num_steps=50,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nbook.GetPage(0).GridAdd(_rf_gain_sizer, 3, 0, 1, 5)
        _xlate_tune_sizer = wx.BoxSizer(wx.VERTICAL)
        self._xlate_tune_text_box = forms.text_box(
        	parent=self.nbook.GetPage(0).GetWin(),
        	sizer=_xlate_tune_sizer,
        	value=self.xlate_tune,
        	callback=self.set_xlate_tune,
        	label="Fine frequency",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._xlate_tune_slider = forms.slider(
        	parent=self.nbook.GetPage(0).GetWin(),
        	sizer=_xlate_tune_sizer,
        	value=self.xlate_tune,
        	callback=self.set_xlate_tune,
        	minimum=-250e3,
        	maximum=250e3,
        	num_steps=500,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nbook.GetPage(0).GridAdd(_xlate_tune_sizer, 2, 0, 1, 5)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_c(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.wbfm_analog_receiver = analog.wfm_rcv(
        	quad_rate=quadrature,
        	audio_decimation=1,
        )
        self.volume_multiplier = blocks.multiply_const_vff((volume, ))
        _usrp_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._usrp_freq_text_box = forms.text_box(
        	parent=self.nbook.GetPage(0).GetWin(),
        	sizer=_usrp_freq_sizer,
        	value=self.usrp_freq,
        	callback=self.set_usrp_freq,
        	label="USRP frequency",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._usrp_freq_slider = forms.slider(
        	parent=self.nbook.GetPage(0).GetWin(),
        	sizer=_usrp_freq_sizer,
        	value=self.usrp_freq,
        	callback=self.set_usrp_freq,
        	minimum=88e6,
        	maximum=108e6,
        	num_steps=200,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nbook.GetPage(0).GridAdd(_usrp_freq_sizer, 1, 0, 1, 5)
        _transition_slider_sizer = wx.BoxSizer(wx.VERTICAL)
        self._transition_slider_text_box = forms.text_box(
        	parent=self.nbook.GetPage(0).GetWin(),
        	sizer=_transition_slider_sizer,
        	value=self.transition_slider,
        	callback=self.set_transition_slider,
        	label="Low-Pass Transition (kHz)",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._transition_slider_slider = forms.slider(
        	parent=self.nbook.GetPage(0).GetWin(),
        	sizer=_transition_slider_sizer,
        	value=self.transition_slider,
        	callback=self.set_transition_slider,
        	minimum=1,
        	maximum=1e3,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nbook.GetPage(0).GridAdd(_transition_slider_sizer, 4, 0, 1, 5)
        self.rtlsdr_source = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source.set_sample_rate(samp_rate)
        self.rtlsdr_source.set_center_freq(rx_freq, 0)
        self.rtlsdr_source.set_freq_corr(0, 0)
        self.rtlsdr_source.set_dc_offset_mode(0, 0)
        self.rtlsdr_source.set_iq_balance_mode(0, 0)
        self.rtlsdr_source.set_gain_mode(False, 0)
        self.rtlsdr_source.set_gain(rf_gain, 0)
        self.rtlsdr_source.set_if_gain(20, 0)
        self.rtlsdr_source.set_bb_gain(20, 0)
        self.rtlsdr_source.set_antenna("", 0)
        self.rtlsdr_source.set_bandwidth(0, 0)
          
        self.resampler_toward_sink_rate = filter.rational_resampler_fff(
                interpolation=int(audio_rate/1e3),
                decimation=int(quadrature/1e3),
                taps=None,
                fractional_bw=None,
        )
        self.fm_low_pass_filter = filter.fir_filter_ccf(int(samp_rate/quadrature), firdes.low_pass(
        	1, samp_rate, cutoff, transition, firdes.WIN_HAMMING, 6.76))
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blks2_tcp_sink_0 = grc_blks2.tcp_sink(
        	itemsize=gr.sizeof_gr_complex*1,
        	addr="127.0.0.1",
        	port=8011,
        	server=False,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.fm_low_pass_filter, 0), (self.wbfm_analog_receiver, 0))
        self.connect((self.resampler_toward_sink_rate, 0), (self.volume_multiplier, 0))
        self.connect((self.rtlsdr_source, 0), (self.fm_low_pass_filter, 0))
        self.connect((self.wbfm_analog_receiver, 0), (self.resampler_toward_sink_rate, 0))
        self.connect((self.volume_multiplier, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blks2_tcp_sink_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.wxgui_scopesink2_0, 0))



    def get_xlate_tune(self):
        return self.xlate_tune

    def set_xlate_tune(self, xlate_tune):
        self.xlate_tune = xlate_tune
        self.set_rx_freq(self.usrp_freq+self.xlate_tune)
        self._xlate_tune_slider.set_value(self.xlate_tune)
        self._xlate_tune_text_box.set_value(self.xlate_tune)

    def get_usrp_freq(self):
        return self.usrp_freq

    def set_usrp_freq(self, usrp_freq):
        self.usrp_freq = usrp_freq
        self.set_rx_freq(self.usrp_freq+self.xlate_tune)
        self._usrp_freq_slider.set_value(self.usrp_freq)
        self._usrp_freq_text_box.set_value(self.usrp_freq)

    def get_transition_slider(self):
        return self.transition_slider

    def set_transition_slider(self, transition_slider):
        self.transition_slider = transition_slider
        self.set_transition(self.transition_slider * 1e3)
        self._transition_slider_slider.set_value(self.transition_slider)
        self._transition_slider_text_box.set_value(self.transition_slider)

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self.volume_multiplier.set_k((self.volume, ))
        self._volume_slider.set_value(self.volume)
        self._volume_text_box.set_value(self.volume)

    def get_transition(self):
        return self.transition

    def set_transition(self, transition):
        self.transition = transition
        self.fm_low_pass_filter.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.transition, firdes.WIN_HAMMING, 6.76))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.fm_low_pass_filter.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.transition, firdes.WIN_HAMMING, 6.76))
        self.rtlsdr_source.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        self._rx_freq_static_text.set_value(self.rx_freq)
        self.rtlsdr_source.set_center_freq(self.rx_freq, 0)

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self.rtlsdr_source.set_gain(self.rf_gain, 0)
        self._rf_gain_slider.set_value(self.rf_gain)
        self._rf_gain_text_box.set_value(self.rf_gain)

    def get_quadrature(self):
        return self.quadrature

    def set_quadrature(self, quadrature):
        self.quadrature = quadrature

    def get_cutoff(self):
        return self.cutoff

    def set_cutoff(self, cutoff):
        self.cutoff = cutoff
        self.fm_low_pass_filter.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.transition, firdes.WIN_HAMMING, 6.76))

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = fm_helloworld()
    tb.Start(True)
    tb.Wait()

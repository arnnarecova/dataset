#!/usr/bin/env python
from transmitters import transmitters
from source_alphabet import source_alphabet
from gnuradio import channels, gr, blocks
import matplotlib.pyplot as plt
import numpy as np
import numpy.fft

for alphabet_type in transmitters.keys():
    print alphabet_type
    for i,mod_type in enumerate(transmitters[alphabet_type]):
        print "running test", i,mod_type

        tx_len = int(10e3)
        src = source_alphabet(alphabet_type, tx_len)
        mod = mod_type()
        #chan = channels.selective_fading_model(8, 20.0/1e6, False, 4.0, 0, (0.0,0.1,1.3), (1,0.99,0.97), 8)

        snk = blocks.vector_sink_c()

        tb = gr.top_block()
        tb.connect(src, mod, snk)
        #tb.connect(src, mod, chan, snk)
        tb.run()

        print "finished: ", len(snk.data())

        plt.figure()
        plt.plot(10*np.log10(numpy.fft.fftshift(numpy.fft.fft(snk.data()))))
        #plt.plot(snk.data())
        plt.title("Modulated %s"%(mod_type.modname))


plt.show()


import numpy as np
import matplotlib.pylab as plt

plt.rcParams["figure.figsize"] = (9, 4)

from obspy import UTCDateTime
from obspy.clients.fdsn import Client

client = Client("EARTHSCOPE")

net = "IU"       
sta = "COR"
loc = "*"         
chan_Z = "HHZ"
event_time = UTCDateTime("2021-01-21T23:00:00")
starttime = event_time
endtime = event_time + (1 * 60 * 60 *24)   # 24 hours i think

st_inv = client.get_stations(
    network=net,
    station=sta,
    location=loc,
    channel=chan_Z,
    starttime=starttime,
    endtime=endtime,
    level="response",
)

my_stream = client.get_waveforms(
    net, sta, loc, chan_Z, starttime, endtime
)

from obspy.signal import PPSD

ppsd = PPSD(my_stream[0].stats, metadata=st_inv, ppsd_length=60)
ppsd.add(my_stream)

print("Number of PSD segments:", len(ppsd.times_processed))
ppsd.plot()


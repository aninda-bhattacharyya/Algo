from kiteconnect import WebSocket
from kiteconnect import KiteConnect




api_key = "nsidzj2b45zmusml"
api_secret = "7ziwy8gps1mooe9kp5uz11p4cpn9lw2t"



user_id = "RA6906"


# #Trading1
# kite = KiteConnect(api_key=api_key)
# print(kite.login_url())
# print(kite.request_access_token("gm516adxbrz4y9l2elam698udaoo1ssq", api_secret))
#
public_token = "rudmicyvj5ecuql7r5cta0dygffi1ocx"

#Initialize
kws = WebSocket(api_key, public_token,user_id)

def on_tick(tick, ws):
    print(tick,"\n")

#Callback for successful connection
def on_connect(ws):
    # Subscribe to a list of instrument_tokens.

    ws.subscribe([3870465])

    # Set this to tick in full mode
    ws.set_mode(ws.MODE_FULL, [3870465])

# Assign the callbacks
kws.on_tick = on_tick
kws.on_connect = on_connect

#Infinite loop on the main thread. Nothing after this will run.
#You have to use pre-defined callbacks to manage subscriptions.

kws.connect()
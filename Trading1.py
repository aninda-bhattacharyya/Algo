from kiteconnect import KiteConnect
api_key = "nsidzj2b45zmusml"
api_secret = "7ziwy8gps1mooe9kp5uz11p4cpn9lw2t"

kite = KiteConnect(api_key=api_key)

print(kite.login_url())

print(kite.request_access_token("tffv1st17mk1wyc2s63rkf9ipa9tjrq2", api_secret))

kite.order_place(tradingsymbol="UNITECH", quantity=1, exchange="NSE", transaction_type="BUY", order_type="MARKET", product="CNC")
import  os
from datetime import datetime
import base64

class LipanaMpesaPpassword:
  lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
  Business_short_code = "174379"
  passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'

  data_to_encode = Business_short_code + passkey + lipa_time

  online_password = base64.b64encode(data_to_encode.encode()).decode("utf-8")

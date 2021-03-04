#!/usr/bin/env python
from datetime import datetime
import veml6070

ALL_INTEGRATION_TIMES = [
    veml6070.INTEGRATIONTIME_1_2T, veml6070.INTEGRATIONTIME_1T, veml6070.INTEGRATIONTIME_2T, veml6070.INTEGRATIONTIME_4T
]

veml = veml6070.Veml6070()
while True :
  for i in ALL_INTEGRATION_TIMES:
      veml.set_integration_time(i)
      uv_raw = veml.get_uva_light_intensity_raw()
      uv = veml.get_uva_light_intensity()
        
        
      tim = '"timestamp":"'+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+'"'
      time_setting = '"' + "Time_setting" + '"' + ":" + '"' + str(v_raw) + '"'
      uv = '"' + "UV[W/(m*m)]" + '"' + ":" + '"' + str(round(uv,5)) + '"'
      mylist = [tim,time_setting,uv]
      mystr = '{' + ','.join(map(str,mylist))+'}'
      print(mystr)  

# -*- coding=utf-8 -*-
import os
from base import initDriver

driver = initDriver()


print( driver.device_time )

# 将当前手机屏幕保存，然后存放在当前项目的根的下面，名字是01.png
driver.get_screenshot_as_file( "./01.png" )

print( os.getcwd() )




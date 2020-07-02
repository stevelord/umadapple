#!/usr/bin/env python

print("/* png convert */")
for i in range(1,6573):
	print("ADDRESS command 'png2ilbm pngs/ba_320_240_30fps_%04u.png iffs/ba_320_240_30fps.%04u -d -bp=4';" % (i,i))
#!/usr/bin/env python
class ModelParams:
	def __init__(self, vp=7.92, vs=4.4, vs_crust=3.2, deg=23):
		from numpy import pi, sin
		phase=raw_input('Direct wave type? (P or S) ')
		self.vp=vp
		self.vs=vs
		self.phase=phase
		self.vs_crust=vs_crust
		self.deg=deg
		if phase=='S':
			self.tscat=90
			self.vapp_main=vs/sin(deg*pi/180.0)
		elif phase=='P':
			self.tscat=40
			self.vapp_main=vp/sin(deg*pi/180.0)
		return

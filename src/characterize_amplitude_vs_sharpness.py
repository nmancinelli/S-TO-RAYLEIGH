#!/usr/bin/env python
#
#
def main():
	#Get list of directories
	Files=GetListOfFiles()
	RelativeAmps=GetRelativeAmps(Files)
	SharpnessParams=GetSharpnessParams(Files)

	for File in Files:
		print SharpnessParams[File], RelativeAmps[File]

	#list relative amp versus dz,dx
	return

def GetRelativeAmps(Files):
	RelativeAmps={}
	for File in Files:
		RelAmp=CalculateRelativeAmp(File)
		RelativeAmps[File]=RelAmp

	return RelativeAmps

def CalculateRelativeAmp(filename):
	from moveout import calculateMoveout
	from rotate import readxy
	from numpy import max, array, pi, sin
		
	def window(ts,xs,tmin,tmax):
		tnew,xnew=[],[]
		for ii in range(len(ts)):
			t=ts[ii]
			x=xs[ii]
			if t>=tmin and t<=tmax:
				tnew.append(t)
				xnew.append(x)

		tnew=array(tnew)
		xnew=array(xnew)
		return tnew, xnew

	def getXforStation(StationNumber):
		fin=open('%s/OUTPUT_FILES/STATIONS' % (filename))
		lines=fin.readlines()
		nfo=lines[StationNumber-1].strip('\n').split()
		x=float(nfo[2])/1000. - 1000.
		return x

	StationNumber=30

	FullFileName='%s/OUTPUT_FILES/AA.S%04d.BXZ.semd' % (filename, StationNumber)
	
	try:
		t,uz=readxy(FullFileName)
	except:
		print '***Warning: Problem reading %s' % (FullFileName)
		return float('nan')


	tscat=90.0
	t=t-tscat

	xorig,torig=0.,0.
	xSta=getXforStation(StationNumber)
	dtwin=15.
	PhaseAmps={}
	vs=4.050
	deg=23.0

	for Phase in ['S', 'Ra']:
		if Phase=='S':
			vapp=vs/sin(deg*pi/180.0)
		elif Phase=='Ra':
			vapp=0.89*vs
		ttarg=calculateMoveout(vapp,xorig,torig,xSta)
		tsWin,xsWin=window(t,uz,ttarg-dtwin,ttarg+dtwin)
		PhaseAmps[Phase]=max(abs(xsWin))

        #import matplotlib as mpl
        #mpl.use('PS')
        #import pylab as plt
	#plt.plot(t,uz,'black')
	#plt.plot(tsWin,xsWin,'red')
	#plt.savefig('debug.eps')

	return PhaseAmps['Ra']/PhaseAmps['S']

def GetSharpnessParams(Files):
	SharpnessParams={}
	for File in Files:
		nfo=File.split('_')
		params=nfo[2]
		nfo2=params.split('-')
		param1=int(nfo2[1])
		param2=int(nfo2[2])

		SharpnessParams[File]=(param1,param2)

	return SharpnessParams

def GetListOfFiles():
	import os
	files=os.listdir('.')
	FilesToConsider=[]
	for filename in files:
		if filename[:7]=='OUTPUT_':
			FilesToConsider.append(filename)

	return FilesToConsider


main()

#!/usr/bin/env python
#
#
from ModelParams import ModelParams
MP=ModelParams()

def main():
	#Get list of directories
	Files=GetListOfFiles()
	RelativeAmps=GetRelativeAmps(Files)
	SharpnessParams=GetSharpnessParams(Files)

	#print RelativeAmps

	print '%8s %8s %8s %8s' % ('DZ (km)', 'DX (km)', 'SLOPE', 'AMP')

	for DZ in [5000]:
		for DX in [5000, 10000, 15000, 20000, 25000]:
			File='OUTPUT_FILES_23-%d-%d' % (DZ,DX)
			#print SharpnessParams[File], RelativeAmps[File]
			try:
				aspect=float(SharpnessParams[File][0])/float(SharpnessParams[File][1])
			except:
				aspect=float('nan')
	
			string='%8.2f %8.2f %8.4f %8.4f' % (SharpnessParams[File][0]/1000., SharpnessParams[File][1]/1000., aspect, RelativeAmps[File])
			print string
	
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

	RelativeAmplitudes=[]

	Stations=range(1,150)

	for StationNumber in Stations:
		FullFileName='%s/OUTPUT_FILES/AA.S%04d.BXZ.semd' % (filename, StationNumber)
	
		try:
			t,uz=readxy(FullFileName)
		except:
			print '***Warning: Problem reading %s' % (FullFileName)
			return float('nan')

		tscat=90.0
		t=t-MP.tscat

		xorig,torig=0.,0.
		xSta=getXforStation(StationNumber)
		dtwin=30.
		PhaseAmps={}
		Windows={}

		for Phase in ['Main', 'Ra']:
			if Phase=='Main':
				vapp=MP.vapp_main
			elif Phase=='Ra':
				vapp=0.89*MP.vs_crust
			ttarg=calculateMoveout(vapp,xorig,torig,xSta)
			tsWin,xsWin=window(t,uz,ttarg,ttarg+dtwin)
	
			PhaseAmps[Phase]=max(abs(xsWin))
			Windows[Phase]=[tsWin,xsWin]


		tmp=PhaseAmps['Ra']/PhaseAmps['Main']
		RelativeAmplitudes.append(tmp)

        import matplotlib as mpl
        mpl.use('PS')
        import pylab as plt
	plt.subplot(2,1,1)
	plt.plot(Stations, RelativeAmplitudes)
	plt.subplot(2,1,2)
	plt.plot(t,uz,'black')
	for Phase in ['Main', 'Ra']:
		plt.plot(Windows[Phase][0], Windows[Phase][1], 'red')
	plt.savefig('debug.eps')

	from numpy import mean, median
	
	avg1 = mean(RelativeAmplitudes)
	avg2 = median(RelativeAmplitudes)

	print avg1, avg2, min(RelativeAmplitudes), max(RelativeAmplitudes)

	return avg1

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

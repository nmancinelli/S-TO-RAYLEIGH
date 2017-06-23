#!/usr/bin/env python
#
#
def main():
	import matplotlib as mpl
	mpl.use('PS')
	import pylab as plt
	import os
	make_sub(121,'BXX',title='Radial',scale_factor=30.0)
	make_sub(122,'BXZ',title='Vertical',scale_factor=30.0)
	
	w = extract_source_wavelet('BXS')

	#for trace_number in range(1,31):
		#tmp=str(trace_number).zfill(2)
		#zoff=float(trace_number)
		#os.chdir('TMP')
		#add_raysum_seis_to_plot(121,'raysum_sv.'+tmp+'.xy',scale_factor=0.4,zoff=zoff,wavelet=w)
		#add_raysum_seis_to_plot(122,'raysum_p.'+tmp+'.xy',scale_factor=12.0,zoff=zoff,wavelet=w)
		#os.chdir('..')

	vs=4.050
	deg=23.0

	from numpy import sin,pi
	vAppRayleigh=0.92*vs;
	vAppS=vs/sin(deg*pi/180.0)

	print 'vAppRayleigh, vAppS = %f  %f' % (vAppRayleigh, vAppS)

	plot_moveout(121,vAppRayleigh,0.0,0.0)
	plot_moveout(121,vAppS,0.0,0.0)
	plot_moveout(121,7.28,0.0,0.0)
	plot_moveout(122,vAppRayleigh,0.0,0.0)
	plot_moveout(122,vAppS,0.0,0.0)
	


	plt.savefig('mypost.eps')

def plot_moveout(isub,vapp,xorig,torig,xmin=000.0,xmax=1100.0):
        import matplotlib as mpl
        mpl.use('PS')
        import pylab as plt
	from numpy import arange
	b=xorig-vapp*torig
	xs=arange(xmin,xmax)
	
	ts=(xs-b)/vapp

	plt.subplot(isub)
	plt.plot(ts,xs,'-r')
	return

def add_raysum_seis_to_plot(subplot,filename,scale_factor,zoff=0.,wavelet=[1.]):
	import matplotlib as mpl
	mpl.use('PS')
	import pylab as plt
	from rotate import readxy
	from scipy.signal import convolve

	plt.subplot(subplot)

	t,u=readxy(filename)
	
	u2 = convolve(u,wavelet,mode='same')

	u3=u2*scale_factor + zoff

	plt.plot(t,u3,'--',color='red')

	return

def make_sub(subplot,channel,title='',scale_factor=1.0):
	import matplotlib as mpl
	mpl.use('PS')
	import pylab as plt
	from numpy import array
	from scipy.signal import correlate
	from numpy import argmax

	plt.subplot(subplot)

	#fin1=open('_station_info.txt','r')
	fin1=open('OUTPUT_FILES/STATIONS','r')

	x=0 #init
	seismos=[]
	tscat=90.0

	for line in fin1.readlines():
		nfo=line.strip('\n').split()
		sta_name = nfo[0]
		#tt_S = float(nfo[1])
		delkm = float(nfo[2])/1000.0 - 1000.0	

		fname='OUTPUT_FILES/AA.'+sta_name+'.'+channel+'.semd'
	
		fin2=open(fname,'r')
		u=[]
		t=[]
		for line2 in fin2.readlines():
			nfo=line2.strip('\n').split()
			#t.append(float(nfo[0]) - tt_S )
			t.append(float(nfo[0]) - tscat)
			u.append(float(nfo[1]))

		#x=x+1
		u=array(u)*scale_factor + delkm		

		trace=[t,u]
		seismos.append(trace)
	
	trace_master = seismos[0]
	
	for trace in seismos:
		t = trace[0]
		u = trace[1]
	
		plt.plot(t,u,color='black')

	plt.title(title)
	if subplot==121:
		plt.ylabel('Topography-to-Receiver Distance (km)')
	
	plt.xlabel('Time after Conversion (s)')

	plt.xlim([0,300])
	#plt.ylim([-1,32])

def write_data_xy(x,y,fname):
	fout=open(fname,'w')

	for i,dum in enumerate(x):
		fout.write('%7.4e   %7.4e\n' % (x[i],y[i]))

	return
	
def extract_source_wavelet(channel):

	fin1=open('_station_info.txt','r')
	
	x=0 #init
	seismos=[]

	
	for line in fin1.readlines():
		nfo=line.strip('\n').split()
	
		sta_name = nfo[0]
		tt_S = float(nfo[1])
		
		if sta_name == 'S0015':
			break
	fin1.close()

	fname='OUTPUT_FILES/AA.'+sta_name+'.'+channel+'.semd'
	
	fin2=open(fname,'r')
	u=[]
	t=[]
	for line2 in fin2.readlines():
		nfo=line2.strip('\n').split()
		t.append(float(nfo[0]) - tt_S )
		u.append(float(nfo[1]))

	w=[] #wavelet
	w_t=[]
	for i in range(len(t)):
		if t[i] >= -3. and t[i] <= 3.:
			w.append(u[i])
			w_t.append(t[i])

	fin2.close()


	write_data_xy(w_t,w,'_source_wavelet.txt')
	
	#import pylab as plt
	#plt.figure(999)
	#plt.plot(w_t,w)
	#plt.savefig('_source_wavelet.eps')
	
	return w
	
def convolve_raysum_syn_with_source(a):
	from scipy.signal import convolve
	
	

main()

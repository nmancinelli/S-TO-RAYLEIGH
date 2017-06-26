#!/usr/bin/env python
#
def main():
	DX=12.
	DZ=5.
	def read_profile():
		fin=open('OUTPUT_FILES_23-%d-%d/interfaces.dat' % (DZ*1000,DX*1000),'r')
		lines=fin.readlines()
		x,z=[],[]
		for line in lines[11:-5]:
			nfo=line.strip('\n').split()
			x.append(float(nfo[0]))
			z.append(float(nfo[1]))
		return x,z

	def plot_profile(x,z):
	        import matplotlib as mpl
        	mpl.use('PS')
        	import pylab as plt
		from numpy import array

		x=array(x)/1000.0
		z=array(z)/1000.0

		plt.ylabel('Height (km)')
		plt.xlabel('Distance (km)')

		plt.xlim(1000-DX/2,1000+DX/2)


		plt.title('DX,DZ = %d %d' % (DX,DZ))
        	plt.plot(x,z,'black')
        	plt.savefig('topo_profile.eps')	
		return

	x,z=read_profile()	
	plot_profile(x,z)
	return

main()

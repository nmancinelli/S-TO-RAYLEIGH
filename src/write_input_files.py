#/usr/bin/env python
#
def write_Par_file(NPROC,H,N_ELEM_VERT,N_ELEM_HORIZ,LAB_WIDTH,W,**params):
	fout=open('Par_file.in','w')
	fout.write('#-----------------------------------------------------------------------------\n')
	fout.write('#\n')
	fout.write('# simulation input parameters\n')
	fout.write('#\n')
	fout.write('#-----------------------------------------------------------------------------\n')
	fout.write('\n')
	fout.write('# title of job\n')
	fout.write('title                           = Slave Craton\n')
	fout.write('\n')
	fout.write('# forward or adjoint simulation\n')
	fout.write('# 1 = forward, 2 = adjoint, 3 = both simultaneously\n')
	fout.write('# note: 2 is purposely UNUSED (for compatibility with the numbering of our 3D codes)\n')
	fout.write('SIMULATION_TYPE                 = 1\n')
	fout.write('# 0 = regular wave propagation simulation, 1/2/3 = noise simulation\n')
	fout.write('NOISE_TOMOGRAPHY                = 0\n')
	fout.write('# save the last frame, needed for adjoint simulation\n')
	fout.write('SAVE_FORWARD                    = .false.\n')
	fout.write('\n')
	fout.write('# parameters concerning partitioning\n')
	fout.write('NPROC                           = %d             # number of processes\n' % (NPROC))
	fout.write('partitioning_method             = 3              # SCOTCH = 3, ascending order (very bad idea) = 1\n')
	fout.write('\n')
	fout.write('# number of control nodes per element (4 or 9)\n')
	fout.write('ngnod                           = 9\n')
	fout.write('\n')
	fout.write('# time step parameters\n')
	fout.write('# total number of time steps\n')
	fout.write('NSTEP                           = %d\n' %(params["NTSTEP"]))
	fout.write('# duration of a time step (see section "How to choose the time step" of the manual for how to do this)\n')
	fout.write('DT                              = %E\n' %(params["DELTA_T"]) )
	fout.write('\n')
	fout.write('# time stepping\n')
	fout.write('# 1 = Newmark (2nd order), 2 = LDDRK4-6 (4th-order 6-stage low storage Runge-Kutta), 3 = classical RK4 4th-order 4-stage Runge-Kutta\n')
	fout.write('time_stepping_scheme            = 1\n')
	fout.write('\n')
	fout.write('# axisymmetric (2.5D) or Cartesian planar (2D) simulation\n')
	fout.write('AXISYM                          = .false.\n')
	fout.write('\n')
	fout.write('# set the type of calculation (P-SV or SH/membrane waves)\n')
	fout.write('P_SV                            = .true.\n')
	fout.write('\n')
	fout.write('# set to true to use GPUs\n')
	fout.write('GPU_MODE                        = .false.\n')
	fout.write('\n')
	fout.write('# available models\n')
	fout.write('#   default: define model using nbmodels below\n')
	fout.write('#   ascii: read model from ascii database file\n')
	fout.write('#   binary: read model from binary databse file\n')
	fout.write('#   external: define model using define_external_model subroutine\n')
	fout.write('#   legacy: read model from model_velocity.dat_input\n')
	fout.write('MODEL                           = default\n')
	fout.write('\n')
	fout.write('# Output the model with the requested type, does not save if turn to default\n')
	fout.write('SAVE_MODEL                      = default\n')
	fout.write('\n')
	fout.write('\n')
	fout.write('#-----------------------------------------------------------------------------\n')
	fout.write('#\n')
	fout.write('# attenuation\n')
	fout.write('#\n')
	fout.write('#-----------------------------------------------------------------------------\n')
	fout.write('\n')
	fout.write('# attenuation parameters\n')
	fout.write('ATTENUATION_VISCOELASTIC_SOLID  = .false.        # turn attenuation (viscoelasticity) on or off for non-poroelastic solid parts of the model\n')
	fout.write('ATTENUATION_PORO_FLUID_PART     = .false.        # turn viscous attenuation on or off for the fluid part of poroelastic parts of the model\n')
	fout.write('Q0                              = 1              # quality factor for viscous attenuation\n')
	fout.write('freq0                           = 10             # frequency for viscous attenuation\n')
	fout.write('\n')
	fout.write('# for viscoelastic attenuation\n')
	fout.write('N_SLS                           = 2              # number of standard linear solids for attenuation (3 is usually the minimum)\n')
	fout.write('f0_attenuation                  = 5.196152422706633 # (Hz) relevant only if source is a Dirac or a Heaviside, otherwise it is f0 the dominant frequency of the source in the CMTSOLUTION file\n')
	fout.write('READ_VELOCITIES_AT_f0           = .false.        # shift velocities to account for physical dispersion (see user manual for more information)\n')
	fout.write('\n')
	fout.write('# to undo attenuation for sensitivity kernel calculations or forward runs with SAVE_FORWARD\n')
	fout.write('# use the flag below. It performs undoing of attenuation in an exact way for sensitivity kernel calculations\n')
	fout.write('# but requires disk space for temporary storage, and uses a significant amount of memory used as buffers for temporary storage.\n')
	fout.write('# When that option is on the second parameter indicates how often the code dumps restart files to disk (if in doubt, use something between 100 and 1000).\n')
	fout.write('UNDO_ATTENUATION                = .false.\n')
	fout.write('NT_DUMP_ATTENUATION             = 500\n')
	fout.write('\n')
	fout.write('\n')
	fout.write('#-----------------------------------------------------------------------------\n')
	fout.write('#\n')
	fout.write('# sources\n')
	fout.write('#\n')
	fout.write('#-----------------------------------------------------------------------------\n')
	fout.write('\n')
	fout.write('# source parameters\n')
	fout.write('NSOURCES                        = 1              # number of sources (source information is then read from the DATA/SOURCE file)\n')
	fout.write('force_normal_to_surface         = .false.        # angleforce normal to surface (external mesh and curve file needed)\n')
	fout.write('\n')
	fout.write('# use an existing initial wave field as source or start from zero (medium initially at rest)\n')
	fout.write('initialfield                    = .true.\n')
	fout.write('add_Bielak_conditions_bottom    = .true.        # add Bielak conditions or not if initial plane wave\n')
	fout.write('add_Bielak_conditions_right     = .true.\n')
	fout.write('add_Bielak_conditions_top       = .false.\n')
	fout.write('add_Bielak_conditions_left      = .true.\n')
	fout.write('\n')
	fout.write('# acoustic forcing\n')
	fout.write('ACOUSTIC_FORCING                = .false.        # acoustic forcing of an acoustic medium with a rigid interface\n')
	fout.write('\n')
	fout.write('\n')
	fout.write('#-----------------------------------------------------------------------------\n')
	fout.write('#\n')
	fout.write('# receivers\n')
	fout.write('#\n')
	fout.write('#-----------------------------------------------------------------------------\n')
	fout.write('\n')
	fout.write('# receiver set parameters for recording stations (i.e. recording points)\n')
	fout.write('seismotype                      = 1              # record 1=displ 2=veloc 3=accel 4=pressure 5=curl of displ 6=the fluid potential\n')
	fout.write('\n')
	fout.write('# subsampling of the seismograms to create smaller files (but less accurately sampled in time)\n')
	fout.write('subsamp_seismos                 = 1\n')
	fout.write('\n')
	fout.write('# so far, this option can only be used if all the receivers are in acoustic elements\n')
	fout.write('USE_TRICK_FOR_BETTER_PRESSURE   = .false.\n')
	fout.write('\n')
	fout.write('# every how many time steps we save the seismograms\n')
	fout.write('# (costly, do not use a very small value; if you use a very large value that is larger than the total number\n')
	fout.write('#  of time steps of the run, the seismograms will automatically be saved once at the end of the run anyway)\n')
	fout.write('NSTEP_BETWEEN_OUTPUT_SEISMOS    = 5000\n')
	fout.write('\n')
	fout.write('# Compute the field int_0^t v^2 dt for a set of GLL points and write it to file. Use\n')
	fout.write('# the script utils/visualisation/plotIntegratedEnergyFile.py to watch. It is refreshed at the same time than the seismograms\n')
	fout.write('COMPUTE_INTEGRATED_ENERGY_FIELD = .false.\n')
	fout.write('\n')
	fout.write('# use this t0 as earliest starting time rather than the automatically calculated one\n')
	fout.write('USER_T0                         = 0.0d0\n')
	fout.write('\n')
	fout.write('# seismogram formats\n')
	fout.write('save_ASCII_seismograms          = .true.         # save seismograms in ASCII format or not\n')
	fout.write('save_binary_seismograms_single  = .true.         # save seismograms in single precision binary format or not (can be used jointly with ASCII above to save both)\n')
	fout.write('save_binary_seismograms_double  = .false.        # save seismograms in double precision binary format or not (can be used jointly with both flags above to save all)\n')
	fout.write('SU_FORMAT                       = .false.        # output single precision binary seismograms in Seismic Unix format (adjoint traces will be read in the same format)\n')
	fout.write('\n')
	fout.write('# use an existing STATION file found in ./DATA or create a new one from the receiver positions below in this Par_file\n')
	fout.write('use_existing_STATIONS           = .false.\n')
	fout.write('\n')
	fout.write('# number of receiver sets (i.e. number of receiver lines to create below)\n')
	fout.write('nreceiversets                   = 1\n')
	fout.write('\n')
	fout.write('# orientation\n')
	fout.write('anglerec                        = 0.d0           # angle to rotate components at receivers\n')
	fout.write('rec_normal_to_surface           = .false.        # base anglerec normal to surface (external mesh and curve file needed)\n')
	fout.write('\n')
	fout.write('# first receiver set (repeat these 6 lines and adjust nreceiversets accordingly)\n')
	fout.write('nrec                            = %d             # number of receivers\n' % (params["N_STATIONS"]))
	fout.write('xdeb                            = %7.0f        # first receiver x in meters\n' % (W*0.36) )
	fout.write('zdeb                            = %7.0f        # first receiver z in meters\n' % (H))
	fout.write('xfin                            = %7.0f        # last receiver x in meters (ignored if only one receiver)\n' % (W*0.70) )
	fout.write('zfin                            = %7.0f        # last receiver z in meters (ignored if only one receiver)\n' % (H))
	fout.write('record_at_surface_same_vertical = .false.        # receivers inside the medium or at the surface\n')
	fout.write('\n')
	fout.write('#-----------------------------------------------------------------------------\n')
	fout.write('#\n')
	fout.write('# adjoint kernel outputs\n')
	fout.write('#\n')
	fout.write('#-----------------------------------------------------------------------------\n')
	fout.write('\n')
	fout.write('# save sensitivity kernels in ASCII format (much bigger files, but compatible with current GMT scripts) or in binary format\n')
	fout.write('save_ASCII_kernels              = .true.\n')
	fout.write('\n')
	fout.write('\n')
	fout.write('#-----------------------------------------------------------------------------\n')
	fout.write('#\n')
	fout.write('# boundary conditions\n')
	fout.write('#\n')
	fout.write('#-----------------------------------------------------------------------------\n')
	fout.write('\n')
	fout.write('# Perfectly Matched Layer (PML) boundaries\n')
	fout.write('# absorbing boundary active or not\n')
	fout.write('PML_BOUNDARY_CONDITIONS         = .false.\n')
	fout.write('NELEM_PML_THICKNESS             = 3\n')
	fout.write('ROTATE_PML_ACTIVATE             = .false.\n')
	fout.write('ROTATE_PML_ANGLE                = 30.\n')
	fout.write('\n')
	fout.write('# Stacey ABC\n')
	fout.write('STACEY_ABSORBING_CONDITIONS     = .true.\n')
	fout.write('ADD_SPRING_TO_STACEY            = .false.\n')
	fout.write('\n')
	fout.write('# periodic boundaries\n')
	fout.write('ADD_PERIODIC_CONDITIONS         = .false.\n')
	fout.write('PERIODIC_HORIZ_DIST             = 0.3597d0\n')
	fout.write('\n')
	fout.write('\n')
	fout.write('#-----------------------------------------------------------------------------\n')
	fout.write('#\n')
	fout.write('# velocity and density models\n')
	fout.write('#\n')
	fout.write('#-----------------------------------------------------------------------------\n')
#
#
	fout.write('nbmodels                        = %d\n' % (2))
	fout.write('# available material types (see user manual for more information)\n')
	fout.write('#   acoustic:    model_number 1 rho Vp 0  0 0 QKappa Qmu 0 0 0 0 0 0\n')
	fout.write('#   elastic:     model_number 1 rho Vp Vs 0 0 QKappa Qmu 0 0 0 0 0 0\n')
	fout.write('#   anistoropic: model_number 2 rho c11 c13 c15 c33 c35 c55 c12 c23 c25 0 0 0\n')
	fout.write('#   poroelastic: model_number 3 rhos rhof phi c kxx kxz kzz Ks Kf Kfr etaf mufr Qmu\n')
	fout.write('#   tomo:        model_number -1 0 0 A 0 0 0 0 0 0 0 0 0 0\n')
#
#
	fout.write('%d 1 %6.1f   %6.1f %6.1f 0 0 10.0 10.0 0 0 0 0 0 0\n' % (2,2800,5660,3200))
	fout.write('%d 1 %6.1f   %6.1f %6.1f 0 0 10.0 10.0 0 0 0 0 0 0\n' % (1,3300,7920,4400))
	#fout.write('%d 1 %6.1f   %6.1f %6.1f 0 0 10.0 10.0 0 0 0 0 0 0\n' % (1,3300,7280,4050))

	fout.write('\n')
	fout.write('# external tomography file\n')
	fout.write('TOMOGRAPHY_FILE                 = ./DATA/tomo.dummy\n')
	fout.write('\n')
	fout.write('# use an external mesh created by an external meshing tool or use the internal mesher\n')
	fout.write('read_external_mesh              = .false.\n')
	#fout.write('assign_external_model           = .true.\n')
	fout.write('\n')
	fout.write('#-----------------------------------------------------------------------------\n')
	fout.write('#\n')
	fout.write('# PARAMETERS FOR EXTERNAL MESHING\n')
	fout.write('#\n')
	fout.write('#-----------------------------------------------------------------------------\n')
	fout.write('\n')
	fout.write('# data concerning mesh, when generated using third-party app (more info in README)\n')
	fout.write('# (see also absorbing_conditions above)\n')
	fout.write('mesh_file                       = ./GMSH/Mesh_SqrCirc          # file containing the mesh\n')
	fout.write('nodes_coords_file               = ./GMSH/Nodes_SqrCirc         # file containing the nodes coordinates\n')
	fout.write('materials_file                  = ./GMSH/Material_SqrCirc      # file containing the material number for each element\n')
	fout.write('free_surface_file               = ./GMSH/Surf_free_SqrCirc     # file containing the free surface\n')
	fout.write('axial_elements_file             = ./DATA/axial_elements_file   # file containing the axial elements if AXISYM is true\n')
	fout.write('absorbing_surface_file          = ./GMSH/Surf_abs_SqrCirc      # file containing the absorbing surface\n')
	fout.write('acoustic_forcing_surface_file   = ./DATA/MSH/Surf_acforcing_Bottom_enforcing_mesh   # file containing the acoustic forcing surface\n')
	fout.write('CPML_element_file               = Elements_CPML_list           # file containing the CPML element numbers\n')
	fout.write('tangential_detection_curve_file = ./DATA/courbe_eros_nodes     # file containing the curve delimiting the velocity model\n')
	fout.write('\n')
	fout.write('#-----------------------------------------------------------------------------\n')
	fout.write('#\n')
	fout.write('# PARAMETERS FOR INTERNAL MESHING\n')
	fout.write('#\n')
	fout.write('#-----------------------------------------------------------------------------\n')
	fout.write('\n')
	fout.write('# file containing interfaces for internal mesh\n')
	fout.write('interfacesfile                  = ../interfaces.dat\n')
	fout.write('\n')
	fout.write('# geometry of the model (origin lower-left corner = 0,0) and mesh description\n')
	fout.write('xmin                            = 0.d0           # abscissa of left side of the model\n')
	fout.write('xmax                            = %E      # abscissa of right side of the model\n' % (W))
	fout.write('nx                              = %d            # number of elements along X\n' % (N_ELEM_HORIZ))
	fout.write('\n')
	fout.write('# absorbing boundary parameters (see absorbing_conditions above)\n')
	fout.write('absorbbottom                    = .true.\n')
	fout.write('absorbright                     = .true.\n')
	fout.write('absorbtop                       = .false.\n')
	fout.write('absorbleft                      = .true.\n')
	fout.write('\n')
	fout.write('# define the different regions of the model in the (nx,nz) spectral-element mesh\n')
	fout.write('nbregions                       = %d              # then set below the different regions and model number for each region\n' % (4) )

	fout.write('  1 200   1  298   1\n')
	fout.write('  1 200 299  301   2\n')
	fout.write('201 601   1  289   1\n')
	fout.write('201 601 290  301   2\n')
	#fout.write('1  %d  692  721   2\n' % (N_ELEM_HORIZ))
	#fout.write('1  %d  722  751   3\n' % (N_ELEM_HORIZ))
#
	fout.write('\n')
	fout.write('#-----------------------------------------------------------------------------\n')
	fout.write('#\n')
	fout.write('# display parameters\n')
	fout.write('#\n')
	fout.write('#-----------------------------------------------------------------------------\n')
	fout.write('\n')
	fout.write('# every how many time steps we display information about the simulation (costly, do not use a very small value)\n')
	fout.write('NSTEP_BETWEEN_OUTPUT_INFO       = 1000\n')
	fout.write('\n')
	fout.write('# meshing output\n')
	fout.write('output_grid_Gnuplot             = .true.        # generate a GNUPLOT file containing the grid, and a script to plot it\n')
	fout.write('output_grid_ASCII               = .false.        # dump the grid in an ASCII text file consisting of a set of X,Y,Z points or not\n')
	fout.write('\n')
	fout.write('# compute and output total acoustic and elastic energy curves (slows down the code significantly)\n')
	fout.write('output_energy                   = .false.\n')
	fout.write('\n')
	fout.write('#-----------------------------------------------------------------------------\n')
	fout.write('#\n')
	fout.write('# movies/images/snaphots\n')
	fout.write('#\n')
	fout.write('#-----------------------------------------------------------------------------\n')
	fout.write('\n')
	fout.write('# every how many time steps we draw JPEG or PostScript pictures of the simulation (costly, do not use a very small value)\n')
	fout.write('NSTEP_BETWEEN_OUTPUT_IMAGES     = 100\n')
	fout.write('\n')
	fout.write('# every how many time steps we dump results of the simulation as ASCII or binary files (costly, do not use a very small value)\n')
	fout.write('NSTEP_BETWEEN_OUTPUT_WAVE_DUMPS = 1000\n')
	fout.write('\n')
	fout.write('# minimum amplitude kept in % for the JPEG and PostScript snapshots; amplitudes below that are muted\n')
	fout.write('cutsnaps                        = 1.\n')
	fout.write('\n')
	fout.write('#### for JPEG color images ####\n')
	fout.write('output_color_image              = .true.         # output JPEG color image of the results every NSTEP_BETWEEN_OUTPUT_IMAGES time steps or not\n')
	fout.write('imagetype_JPEG                  = 3              # display 1=displ_Ux 2=displ_Uz 3=displ_norm 4=veloc_Vx 5=veloc_Vz 6=veloc_norm 7=accel_Ax 8=accel_Az 9=accel_norm 10=pressure\n')
	fout.write('factor_subsample_image          = 1.0d0          # (double precision) factor to subsample color images output by the code (useful for very large models)\n')
	fout.write('USE_CONSTANT_MAX_AMPLITUDE      = .false.        # by default the code normalizes each image independently to its maximum; use this option to use the global maximum below instead\n')
	fout.write('CONSTANT_MAX_AMPLITUDE_TO_USE   = 1.17d4         # constant maximum amplitude to use for all color images if the above USE_CONSTANT_MAX_AMPLITUDE option is true\n')
	fout.write('POWER_DISPLAY_COLOR             = 0.05d0         # non linear display to enhance small amplitudes in JPEG color images\n')
	fout.write('DRAW_SOURCES_AND_RECEIVERS      = .true.         # display sources as orange crosses and receivers as green squares in JPEG images or not\n')
	fout.write('DRAW_WATER_IN_BLUE              = .true.         # display acoustic layers as constant blue in JPEG images, because they likely correspond to water in the case of ocean acoustics or in the case of offshore oil industry experiments (if off, display them as greyscale, as for elastic or poroelastic elements, for instance for acoustic-only oil industry models of solid media)\n')
	fout.write('USE_SNAPSHOT_NUMBER_IN_FILENAME = .false.        # use snapshot number in the file name of JPEG color snapshots instead of the time step (for instance to create movies in an easier way later)\n')
	fout.write('\n')
	fout.write('#### for PostScript snapshots ####\n')
	fout.write('output_postscript_snapshot      = .false.         # output Postscript snapshot of the results every NSTEP_BETWEEN_OUTPUT_IMAGES time steps or not\n')
	fout.write('imagetype_postscript            = 1              # display 1=displ vector 2=veloc vector 3=accel vector; small arrows are displayed for the vectors\n')
	fout.write('meshvect                        = .false.         # display mesh on PostScript plots or not\n')
	fout.write('modelvect                       = .true.        # display velocity model on PostScript plots or not\n')
	fout.write('boundvect                       = .false.         # display boundary conditions on PostScript plots or not\n')
	fout.write('interpol                        = .false.         # interpolation of the PostScript display on a regular grid inside each spectral element, or use the non-evenly spaced GLL points\n')
	fout.write('pointsdisp                      = 6              # number of points in each direction for interpolation of PostScript snapshots (set to 1 for lower-left corner only)\n')
	fout.write('subsamp_postscript              = 1              # subsampling of background velocity model in PostScript snapshots\n')
	fout.write('sizemax_arrows                  = 1.d0           # maximum size of arrows on PostScript plots in centimeters\n')
	fout.write('US_LETTER                       = .true.        # use US letter or European A4 paper for PostScript plots\n')
	fout.write('\n')
	fout.write('#### for wavefield dumps ####\n')
	fout.write('output_wavefield_dumps          = .false.        # output wave field to a text file every NSTEP_BETWEEN_OUTPUT_TEXT_DUMPS time steps (creates very big files)\n')
	fout.write('imagetype_wavefield_dumps       = 1              # display 1=displ vector 2=veloc vector 3=accel vector 4=pressure\n')
	fout.write('use_binary_for_wavefield_dumps  = .false.        # use ASCII or single-precision binary format for the wave field dumps\n')
	fout.close()
#
#
#
def write_SOURCE(H,**params):
	fout=open('SOURCE.in','w')
	fout.write('#source 1.  The components of a moment tensor source must be given in N.m, not in dyne.cm as in the DATA/CMTSOLUTION source file of the 3D version of the code.\n')
	fout.write('source_surf                     = .false.        # source inside the medium or at the surface\n')
	fout.write('xs                              = 000\n')
	fout.write('zs                              = %7.0f         # source location z in meters\n' % (H))
	fout.write('source_type                     = %1d            # 1 for plane P waves, 2 for plane SV waves, 3 for Rayleigh wave\n' % (params["P_OR_S"]))
	fout.write('time_function_type              = 3              # Ricker = 1, first derivative = 2, Gaussian = 3, Dirac = 4, Heaviside = 5\n')
	fout.write('# time function_type == 8 source read from file, if time function_type == 9 : burst\n')
	fout.write('# If time_function_type == 8, enter below the custom source file to read (two columns file with time and amplitude) :\n')
	fout.write('# (For the moment dt must be equal to the dt of the simulation. File name cannot exceed 150 characters)\n')
	fout.write('name_of_source_file             = "/uoigaf/iuagzf/afb" # Only for option 8 : file containing the source wavelet\n')
	fout.write('burst_band_width                = 200.415        # Only for option 9 : band width of the burst\n')
	fout.write('f0                              = 0.10           # dominant source frequency (Hz) if not Dirac or Heaviside\n')
	fout.write('tshift                          = 0.0            # time shift when multi sources (if one source, must be zero)\n')
	fout.write('anglesource                     = %5.0f.\n' % (params["ANGLE_SOURCE"] ))
	fout.write('Mxx                             = 1.             # Mxx component (for a moment tensor source only)\n')
	fout.write('Mzz                             = -1.            # Mzz component (for a moment tensor source only)\n')
	fout.write('Mxz                             = 0.             # Mxz component (for a moment tensor source only)\n')
	fout.write('factor                          = 0.75d10        # amplification factor\n')
	fout.close()

def write_interfaces(H,N_ELEM_VERT,W,AMP_SURF,AMP_MOHO,WAVLEN):

	#MOHO DEPTH
	MD = 60000.0
	LD =120000.0
	#LAB DEPTH

	DZ_Surf=AMP_SURF
	DZ_Moho=AMP_MOHO

	DX=WAVLEN

	#N_ELEM_3 = int(MD/H*N_ELEM_VERT)
	#N_ELEM_2 = int((LD-MD)/H*N_ELEM_VERT)
	#N_ELEM_1 = N_ELEM_VERT - N_ELEM_2 - N_ELEM_3

	def write_flat_iface(ifaceNumber,W,H):
		fout.write('# interface number %d (bottom of the mesh)\n' % (ifaceNumber))
		fout.write(' 2\n')
		fout.write(' %7.0f %7.0f\n' % (0,H))
		fout.write(' %7.0f %7.0f\n' % (W,H))

	def write_oscillating_iface(ifaceNumber,W,H,a,wl):
		from numpy import pi,arange,cos
		fout.write('# interface number %d (bottom of the mesh)\n' % (ifaceNumber))

		x0=1000000.0

		dx=1000.0
		xs=arange(0,W+dx,dx)
		fout.write(' %d\n' % len(xs))
		for x in xs:
			y=H+a*cos(2*pi/wl*(x-x0))
			fout.write(' %7.0f %7.0f\n' % (x,y))

	def write_erf_iface(ifaceNumber,W,H,a,xchar):
                from numpy import pi,arange,cos
		from scipy.special import erf

                fout.write('# interface number %d (bottom of the mesh)\n' % (ifaceNumber))

                x0=1000000.0

                dx=1000.
                xs=arange(0,W+dx,dx)
                fout.write(' %d\n' % len(xs))
                for x in xs:
			y=H+a/2.0*(erf(2.*(x-x0)/xchar)+1.0)
                        fout.write(' %7.0f %7.0f\n' % (x,y))

	fout=open('interfaces.dat','w')
	fout.write('# number of interfaces\n')
	fout.write(' 4\n')
	fout.write('#\n')
	fout.write('# for each interface below, we give the number of points and then x,z for each point\n')
	fout.write('#\n')
	#Build from bottom up
	write_flat_iface(1,W,0) #Bottom
	write_flat_iface(2,W,H-45000) #Moho (continent)
	write_flat_iface(3,W,H-8000-DZ_Surf) #Moho (ocean)
	#write_flat_iface(4,W,H) #Surface
	if DZ_Surf!=0:
		write_erf_iface(4,W,H-DZ_Surf,DZ_Surf,DX)
	else:
		write_flat_iface(4,W,H)
	#write_erf_iface(2,W,H-8000-DZ_Surf,DZ_Moho,DX)
	fout.write('#\n')
	fout.write('# for each layer, we give the number of spectral elements in the vertical direction\n')
	fout.write('#\n')
	fout.write('# layer number 1\n')
	fout.write('%d\n' % (N_ELEM_VERT-12) )
	fout.write('# layer number 2\n')
	fout.write('%d\n' % (9) )
	fout.write('# layer number 2\n')
	fout.write('%d\n' % (3) )
	#fout.write('# layer number 2\n')
	#fout.write('%d\n' % (N_ELEM_2) )
	#fout.write('# layer number 3\n')
	#fout.write('%d\n' % (N_ELEM_3) )

	fout.close()

def linear_interp(x,x0,x1,y0,y1):
	"""
	Wikipedia equation
	"""
	return y0+(y1-y0)*(x-x0)/(x1-x0)
	write_erf_iface(2,W,H,DZ,DX)

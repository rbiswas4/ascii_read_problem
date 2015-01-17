from astropy.io import ascii
from astropy.io import registry
import astropy
import numpy 

print 'Numpy version:', numpy.__version__
print 'astropy version:', astropy.__version__
print astropy.__file__

g = ascii.read('filters/total_g.dat')
print 'loaded g'
r = ascii.read('filters/total_r.dat')
print 'loaded r'
u = ascii.read('filters/total_u.dat')
print 'loaded u'
i = ascii.read('filters/total_i.dat')
# z = ascii.read('filters/total_z.dat')

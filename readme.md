
# Normalization

All the quantity are normalized:
* masses are normalized to the electron mass
* charges are normalized to the electron charge
* magnetic field is normalized to a reference value `B0`
* density are normalized to a reference value `N0`
* frequencies are normalized to the electron plasma frequency
* lengths are normalized to the electron inertial length
* velocities are normalized to the speed of light


# Population

An instance of the `Population` class has to be created for each population. This object stores a `name`, a `charge`, a `mass` and a `distribution`. This last argument is an instance of the class `Distribution` detailed here below. We have 2 subclasses of `Population`, which are `Electron` and `Proton`. Their attributes are obvious.


# Distribution

The class `Distribution` stores 2 attributes : the name (of the distribution) and the density (zeroth order of the distribution function). The `Distribution` class is the support class for 2 subclasses : `Dirac` for a cold plasma and `Maxwell` for an hot itotrop non-drifting maxwellian. The default distribution built by the constructor is `Dirac`.

# Plasma

Finaly, a plasma is a list of `Population` instances with a magnetic field. In addition of these attributes, this class is responsible to compute the plasma frequencies and the cyclotron frequencies for each population, and then store these values in a dict (respectively `wp` and `wc`), which keys are the population name.


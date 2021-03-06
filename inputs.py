### Input file for automated extraction of material properties from indentation data

# define the model: a string linked to a simulation model set up in the simulate module


sample_modulus = 117 # GPa
sample_poisson = 0.33 # unitless
indenter_radius = 1 # mm
exp_filename = 'AnnealedCopper.csv' # experiemntal data filename as a string


# define the constitutive law as detailed in docs

model = 'Ludwick' 
# first guess at material variables as defined by constitutive law
# e.g. Ludwick-holloman [yield_stress, K, n]
material_variables = [400, 400, 0.5]


# optional parameters, will take default values if not defineds
coeff_of_friction = 0.2

# Mesh parameters
# A parameter related to the number of elements under the indenter
# too low a value can lead to artefacts (non-smooth) in the load displacement curve
seeds = 80 

# Number of cores for simulations, default num_cores = 1
num_cores = 1

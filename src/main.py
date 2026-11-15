import pyfluids as pf

"""
Luft i ett kolv-cylindersystem komprimeras långsamt från ett tillstånd med tryck 120 kPa och volym 5 
dm3 till ett tillstånd med volymen V < 5 dm3. Kompressionen sker isotermt vid temperaturen -30 °C. 
Beräkna hur mycket arbete som krävs samt hur mycket värme som förs bort från systemet, som 
funktion av slutvolymen V. 
"""

# Intitial pressure and volume
p_0 = 120e3
v_0 = 5e-3

# Degree in celsius
temp = -30

# Creates a Fluid-object which represents air
air = pf.Fluid(pf.FluidsList.Air)

# Calculates the current temperature for the air
air.update(pf.Input.pressure(p_0), pf.Input.temperature(temp))

print(f"The current volume for the air is: {air.specific_volume} m^3")

"""Demo of telescope thermal."""

import astropy.units as u


def calc_telescope_emission(list_of_warm_components):
	"""Calculate
	Assumes all thermal sources are upstream from the filters.
	"""

	for temp, emissivitty, solid_angle in list_of_stuff:

        bb_fluxes = blackbody_lambda(self.wavelengths, temp)

        total_bb_flux = emissivitty * bb_fluxes * solid_angle * (self.camera.pixel_size)**2 * u.pixel

        total_bb_flux = total_bb_flux.to(u.photons / u.second / u.AA / u.pixel, equivalcinces=u.spectral_density(self.wavelengths))

        self.scope_emissions = {}
        for filter_name in self.filter_names:
            self.scope_emissions[filter_name] = np.trapz(self.filters[filter_name].transmission * self.camera.qe * total_bb_flux, x=self.wavelengths)

            assert self.scope_emissions[filter_name].unit == u.electron / u.second / u.pixel




if __name__ == '__main__':

	f_number_mirror = 1.4
	solid_angle_mirror = np.pi / (f_number_mirror**2 * 4)

	list_of_warm_components = [(140. * u.K, 1, half_sphere), # cold chamber
	(240 * u.K, 0.05, 3 * field_of_view), # logic is that we don't want enterance to obscure the optical path
	(20 * u.K, 0.05, 15) ]

    calc_telescope_emission()

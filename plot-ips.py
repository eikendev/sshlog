#!/usr/bin/env python3

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import matplotlib as mpl

from matplotlib import pyplot as plt


def main():
    cmap = mpl.cm.Blues

    plt.close()

    countries = {"US": 100, "CA": 50, "CN": 10}

    max_value = float(max(countries.values()))

    shpfilename = shpreader.natural_earth(resolution='110m', category='cultural', name='admin_0_countries')
    ax = plt.axes(projection=ccrs.Miller(central_longitude=10))
    ax.set_global()
    ax.outline_patch.set_edgecolor('white')

    ax.add_feature(cfeature.COASTLINE, alpha=0.3)
    ax.add_feature(cfeature.BORDERS, alpha=0.3)

    for country in shpreader.Reader(shpfilename).records():
        name = country.attributes['ISO_A2']

        try:
            value = countries[name]
        except KeyError:
            continue

        ax.add_geometries(country.geometry, ccrs.PlateCarree(), facecolor=cmap(value / max_value, 1))

    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(0, 1))
    plt.colorbar(sm, ax=ax)

    plt.show()


if __name__ == "__main__":
    main()

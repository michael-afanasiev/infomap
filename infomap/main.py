import json
import cartopy.io.shapereader as shpreader
import cartopy.crs as ccrs
import matplotlib.pyplot as plt


def read_json(filename):
    """
    Read and parse a JSON file containing country name / percentage values.
    :param filename: json file.
    :return: List of tuples containing country code / prevalence of use.
    """

    with open(filename) as fh:
        raw = json.load(fh)
    return raw['countries']


def plot():
    ax = plt.axes(projection=ccrs.PlateCarree())
    shpfilename = shpreader.natural_earth(resolution='110m',
                                          category='cultural',
                                          name='admin_0_countries')
    reader = shpreader.Reader(shpfilename)
    countries = reader.records()
    for country in countries:
        if country.attributes['adm0_a3'] == 'USA':
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                              facecolor=(0, 0, 1),
                              label=country.attributes['adm0_a3'])

            # plt.show()


def cli():
    plot()

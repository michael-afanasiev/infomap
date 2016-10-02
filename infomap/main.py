import json

import cartopy
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import click
import matplotlib.patches as mpatch
import matplotlib.pyplot as plt


def get_colour(val):
    val = float(val)
    if 0.0 <= val < 25.0:
        return 'w'
    elif 25.0 <= val < 50.0:
        return 'r'
    elif 50.0 <= val < 75.0:
        return 'y'
    elif 75.0 <= val <= 100.0:
        return 'g'
    raise ValueError("Value for colourmap must be between 0 and 100.")


def read_json(filename):
    """
    Read and parse a JSON file containing country name / percentage values.
    :param filename: json file.
    :return: List of tuples containing country code / prevalence of use.
    """

    with open(filename) as fh:
        raw = json.load(fh)
    return raw['countries']


def get_countries():
    """
    Get the country shapefiles and attributes from the natural_earth database.
    :return: Natural earth records.
    """
    shpfilename = shpreader.natural_earth(resolution='110m',
                                          category='cultural',
                                          name='admin_0_countries')

    # Plot usage data.
    reader = shpreader.Reader(shpfilename)
    return reader.records()


def plot(data, save_filename=None):
    """
    Plot prevalence of use values on the map.
    :param data: Tuple of country name / usage rate (in percent).
    :param save_filename: If specified, write plot to this file.
    """

    # Read geometric data
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.add_feature(cartopy.feature.OCEAN)

    countries = get_countries()
    for country in countries:
        name = country.attributes['adm0_a3']
        if name in data.keys():
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                              facecolor=get_colour(data[name]), label=name,
                              lw=0.5)
        else:
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                              facecolor='w', label=name, lw=0.5)

    # Apply legend
    patches = []
    for val, lab in zip(
            [0, 25, 50, 75],
            ['< 25', '25 - 50', '50 - 75', '> 75']):
        patches.append(mpatch.Patch(color=get_colour(val), label=lab))
    plt.legend(handles=patches, loc=3, fontsize='small')

    if save_filename:
        plt.savefig(save_filename, bbox_inches='tight')
    else:
        plt.show()


@click.group()
def cli():
    pass


@cli.command()
@click.option('--data-file', help="File containing adoption rates")
@click.option('--output-file', help='PDF file to save map')
def make_map(data_file):
    data = read_json(data_file)
    plot(data, save_filename='test.pdf')


@cli.command()
def print_country_codes():
    """
    Print country code : long name, for purposes of creating the data JSON file.
    """
    countries = get_countries()
    for country in countries:
        print(country.attributes['adm0_a3'] + ':',
              country.attributes['name_long'])

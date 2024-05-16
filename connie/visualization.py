import cartopy
import click
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

from geopy.geocoders import Nominatim


def get_lat_lng(city_name):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(city_name)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None


@click.command("net_map")
def net_map():
    data = {
        'City': ['Roma', 'Milano', 'Napoli', 'Roma', 'Torino', 'Milano', 'Napoli', 'Roma', 'Milano'],
        'Latitude': [41.9028, 45.4642, 40.8518, 41.9028, 45.0703, 45.4642, 40.8518, 41.9028, 45.4642],
        'Longitude': [12.4964, 9.1900, 14.2681, 12.4964, 7.6869, 9.1900, 14.2681, 12.4964, 9.1900]
    }

    df = pd.DataFrame(data)

    # Conta il numero di occorrenze di ogni città
    city_counts = df['City'].value_counts()

    # Crea la mappa
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

    # Aggiungi le coste e i confini politici
    ax.coastlines()
    ax.add_feature(cartopy.feature.BORDERS, linestyle=':', linewidth=1)

    # Definisci una scala di colori
    colors = plt.cm.viridis(np.linspace(0, 1, max(city_counts.values) + 1))

    # Aggiungi i punti sulla mappa
    for city, count in city_counts.items():
        city_data = df[df['City'] == city]
        ax.scatter(city_data['Longitude'], city_data['Latitude'], color=colors[count], s=50, label=f'{city} ({count})')

    # Aggiungi una legenda
    ax.legend(loc='upper right')

    # Mostra la mappa
    plt.title('Mappa delle città con punti colorati in base al numero di occorrenze')
    plt.show()




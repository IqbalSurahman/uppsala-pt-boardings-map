import geopandas as gpd
import os

def convert_shp_to_geojson(shp_path, output_dir=None):
    """
    Converts a shapefile to GeoJSON format (WGS84/EPSG:4326) and ensures a 'name' property from 'NAME'.

    Parameters:
    - shp_path: str, path to the input .shp file
    - output_dir: str, optional directory to save the GeoJSON file. Defaults to the same directory as the input file.

    Returns:
    - geojson_path: str, path to the output GeoJSON file
    """
    # Load the shapefile using geopandas
    gdf = gpd.read_file(shp_path)

    # Set CRS to EPSG:3006 (SWEREF99 TM) if missing
    if gdf.crs is None:
        gdf.set_crs("EPSG:3006", inplace=True)

    # Reproject to WGS84 (EPSG:4326) for GeoJSON
    gdf = gdf.to_crs("EPSG:4326")

    # Always create 'name' column from 'NAME'
    if 'NAME' in gdf.columns:
        gdf['name'] = gdf['NAME']
    else:
        gdf['name'] = ''  # fallback: empty string

    # Rename PASSBOAR~1 to Board DY if it exists
    if 'PASSBOAR~1' in gdf.columns:
        gdf = gdf.rename(columns={'PASSBOAR~1': 'Board DY'})

    # Determine output directory
    if output_dir is None:
        output_dir = os.path.dirname(shp_path)

    # Construct output file path
    base_name = os.path.splitext(os.path.basename(shp_path))[0]
    geojson_path = os.path.join(output_dir, f"{base_name}.geojson")

    # Save to GeoJSON
    gdf.to_file(geojson_path, driver='GeoJSON')

    return geojson_path

# Run the conversion:
shp_path = "shp/Hållplatser_UA2034_stop.shp"
output_dir = "data/"
os.makedirs(output_dir, exist_ok=True)

geojson_file = convert_shp_to_geojson(shp_path, output_dir)
print(f"GeoJSON file saved to: {geojson_file}")
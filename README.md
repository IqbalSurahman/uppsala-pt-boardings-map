# Uppsala Public Transport Boardings Map

This project provides an interactive map visualizing public transport boarding data in Uppsala. The map displays various stops and allows users to explore boarding scenarios.

## Project Structure

- **index.html**: The main webpage that embeds the interactive map.
- **data/**: Contains GeoJSON files for stops and boarding scenarios.
  - **stops.geojson**: Locations of transport stops.
  - **boardings_scenario_a.geojson**: Boarding data for Scenario A.
  - **boardings_scenario_b.geojson**: Boarding data for Scenario B.
- **js/**: Contains JavaScript files for map rendering.
  - **map.js**: Code to load and render the map using a mapping library.
- **css/**: Contains styles for the map and webpage.
  - **style.css**: Custom styles for visual elements.
- **assets/**: Directory for optional custom icons for stops/stations.
- **README.md**: Project overview and instructions.
- **.gitignore**: Specifies files to ignore in version control.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Open `index.html` in a web browser to view the interactive map.

3. Ensure that the GeoJSON files in the `data/` directory are correctly formatted and accessible.

## Usage

- The map will display transport stops and allow users to switch between different boarding scenarios.
- Customize the styles in `css/style.css` to change the appearance of the map and webpage.
- Modify `js/map.js` to add additional functionality or features to the map.

## Contributing

Feel free to submit issues or pull requests to improve the project. 

## License

This project is licensed under the MIT License.
// JavaScript code to load and render the map using Leaflet

// Initialize the Leaflet map centered on Uppsala
const map = L.map('map').setView([59.8586, 17.6389], 12);

// Add OpenStreetMap tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Function to style each stop as a circle marker
function pointToCircleMarker(feature, latlng) {
    return L.circleMarker(latlng, {
        radius: 5,
        fillColor: '#0078A8',
        color: '#000',
        weight: 1,
        opacity: 1,
        fillOpacity: 0.8
    });
}

// Function to bind popup with stop name
function onEachStop(feature, layer) {
    const stopName = feature.properties && feature.properties.name ? feature.properties.name : 'No name';
    layer.bindPopup(`<strong>Stop:</strong> ${stopName}`);
}

// Load stops GeoJSON and add to map
fetch('data/Hållplatser_UA2034_stop.geojson')
    .then(response => response.json())
    .then(data => {
        L.geoJSON(data, {
            pointToLayer: pointToCircleMarker,
            onEachFeature: onEachStop
        }).addTo(map);
    })
    .catch(error => console.error('Error loading stops GeoJSON:', error));

// TODO: Add boarding data layers here in
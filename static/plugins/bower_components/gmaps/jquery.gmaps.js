$(document).ready(function() {
    // Simple map
    map = new GMaps({
        el: '#gmaps-simple',
        lat: 26.8467,
        lng: 80.9462,
        zoom: 20,
        panControl: false,
        streetViewControl: false,
        mapTypeControl: false,
        overviewMapControl: false
    });
});

var map;
var geoXml = new GGeoXml("https://earthquake.usgs.gov/fdsnws/event/1/query?format=kml&starttime={{ past_day }}&endtime={{ time_now }}&kmlanimated=true")
function load() {
    if (GBrowserIsCompatible()) {
        map = new GMap2(document.getElementById("map"));
        map.addControl(new GLargeMapControl());
        map.addControl(new GMapTypeControl());
        map.addControl(new GOverviewMapControl());
        map.addOverlay(geoXml);
        geoXml.gotoDefaultViewport(map)
    }
}
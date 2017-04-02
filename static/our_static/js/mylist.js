$(document).ready(function(){
            $.getJSON("https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={{ past_day }}&endtime={{time_now }}&alertlevel=green", function(result){
                if(result.metadata.count>0) {
                    $.each(result.features, function (i, field) {
                        var d = new Date(result.features[i].properties.time);
                        var formattedDate = d.getDate() + "-" + (d.getMonth() + 1) + "-" + d.getFullYear();
                        var hours = (d.getHours() < 10) ? "0" + d.getHours() : d.getHours();
                        var minutes = (d.getMinutes() < 10) ? "0" + d.getMinutes() : d.getMinutes();
                        var formattedTime = hours + ":" + minutes;
                        formattedDate = formattedDate + " " + formattedTime;
                        $("#green").append('<button type="button" class="list-group-item list-group-item-action"><span class="list-callout" style="font-size: small">' + 'mag: ' + result.features[i].properties.mag + '</span><h1 class="list-header" style="font-size: small">' + 'place :' + result.features[i].properties.place + '</h1><h2 class="list-subheader" style="font-size:small" >' + 'time :' + formattedDate + '</h2><aside class="list-aside">' + result.features[i].geometry.coordinates[2] + 'KM' + '</aside></button>');
                    });
                }
                else{
                 $("#green").append('<h1>'+result.metadata.count+'</h>');
                }
            });
            $.getJSON("https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={{ past_day }}&endtime={{time_now }}&alertlevel=yellow", function(result){
                    if(result.metadata.count>0) {
                    $.each(result.features, function (i, field) {
                        var d = new Date(result.features[i].properties.time);
                        var formattedDate = d.getDate() + "-" + (d.getMonth() + 1) + "-" + d.getFullYear();
                        var hours = (d.getHours() < 10) ? "0" + d.getHours() : d.getHours();
                        var minutes = (d.getMinutes() < 10) ? "0" + d.getMinutes() : d.getMinutes();
                        var formattedTime = hours + ":" + minutes;
                        formattedDate = formattedDate + " " + formattedTime;
                        $("#yellow").append('<button type="button" class="list-group-item list-group-item-action"><span class="list-callout" style="font-size: small">' + 'mag: ' + result.features[i].properties.mag + '</span><h1 class="list-header" style="font-size: small">' + 'place :' + result.features[i].properties.place + '</h1><h2 class="list-subheader" style="font-size:small" >' + 'time :' + formattedDate + '</h2><aside class="list-aside">' + result.features[i].geometry.coordinates[2] + 'KM' + '</aside></button>');
                    });
                }
                else{
                 $("#yellow").append('<button type="button" class="warning list-group-item list-group-item-action">'+"This List is empty"+'</button>');
                }
            });
            $.getJSON("https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={{ past_day }}&endtime={{time_now }}&alertlevel=red", function(result){
                    if(result.metadata.count>0) {
                    $.each(result.features, function (i, field) {
                        var d = new Date(result.features[i].properties.time);
                        var formattedDate = d.getDate() + "-" + (d.getMonth() + 1) + "-" + d.getFullYear();
                        var hours = (d.getHours() < 10) ? "0" + d.getHours() : d.getHours();
                        var minutes = (d.getMinutes() < 10) ? "0" + d.getMinutes() : d.getMinutes();
                        var formattedTime = hours + ":" + minutes;
                        formattedDate = formattedDate + " " + formattedTime;
                        $("#red").append('<button type="button" class="list-group-item list-group-item-action"><span class="list-callout" style="font-size: small">' + 'mag: ' + result.features[i].properties.mag + '</span><h1 class="list-header" style="font-size: small">' + 'place :' + result.features[i].properties.place + '</h1><h2 class="list-subheader" style="font-size:small" >' + 'time :' + formattedDate + '</h2><aside class="list-aside">' + result.features[i].geometry.coordinates[2] + 'KM' + '</aside></button>');
                    });
                }
                else{
                 $("#red").append('<button type="button" class="warning list-group-item list-group-item-action">'+"This List is empty"+'</button>');
                }
            });
        });
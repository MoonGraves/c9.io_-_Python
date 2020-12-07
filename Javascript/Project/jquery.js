$( function () {

	$('.place-types :radio').click( function () {    	
        var plc = $( this ).val();
        clearMarker();
        callService( map, plc);
    });
    
});

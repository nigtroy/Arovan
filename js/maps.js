var autocomplete;

/**
 * Initializes google maps/places api component
 * autocomplete, and sets its initial value
 */
var initMap = () => {
    let input = document.getElementById('city');
    let options = {
        types: ['(cities)'],
    };

    autocomplete = new google.maps.places.Autocomplete(input,options);
    autocomplete.addListener('place_changed', getPlace);

    firstRun(input);
}

/**
 * callback function to be called when the 
 * autocomplete input element changes its value
 */
var getPlace = () => {
    let place = autocomplete.getPlace();
    if(!place.formatted_address){
        alert('Invalid Place!');
        return;
    }
    getForecast(place.formatted_address);
}

/**
 * Sets the initial value of the city, and gets the forecast
 * @param {!HTMLObjectElement} input 
 */
var firstRun = (input) => {
    let place = "Salvador, Bahia, Brasil";
    $(input).val(place);
    getForecast(place);
}

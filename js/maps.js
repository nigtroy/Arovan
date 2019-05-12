var autocomplete;
var today;
var forecasts;

/**
 * Calls yahoo weather api with the given
 * string correspongind to the city, and 
 * calls the updatePage function
 * @param {string} city 
 */
var getForecast = (city) => {
    var searchtext = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='" + 
        city.replace(/["']/g, "") + "') and u='c'";
    $.ajax({
        url: "https://query.yahooapis.com/v1/public/yql?q=" + searchtext + "&format=json",
        data: {text: city}
    }).then((data) => {
        if(data.query.results == null){
            alert("error");
            return;
        }
        // console.log(data.query.results); //DEBUG
        today = data.query.results.channel.item.condition;
        forecasts = data.query.results.channel.item.forecast.slice(1,5);
        updatePage();
    });
}

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

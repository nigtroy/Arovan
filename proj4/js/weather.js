$(document).ready(function(){
    
var url = "http://api.openweathermap.org/data/2.5/weather?q=";


var appid="&appid=456a2d5e8adb346d23b30eae0b602d6f&units=metric";   

    var weather_img = "http://openweathermap.org/img/w/";
    var ico_png=".png";

function showre(){
    
    $('.results_container').show();
    
    var city = $('.user_in').val();
            
    var together = url+city+appid;
    
if(city==""){
    
    return alert("Please enter a city!");
}
    else{
$.ajax({
	url:together,
	success:function(dat){
		var obj = dat;
        console.log(obj);
        $('.re_city').text(obj.name);
		$('.desc').text(obj.weather[0].description);
        $('.temp').text(obj.main.temp+String.fromCharCode(176)+"C");
        $('.high').text(obj.main.temp_max+String.fromCharCode(176)+"C");
        $('.low').text(+obj.main.temp_min+String.fromCharCode(176)+"C");

        var weather_ico = obj.weather[0].icon;
        
        $(".ico").attr('src', weather_img + weather_ico + ico_png); 
		$('.thermo_hi').attr('src','images/high.png');
        $('.thermo_low').attr('src','images/low.png');
	}
})


    }
      
}

$("#search").on('click',showre);
    
$('.user_in').keydown(function(e) {
    if(e.which == 13) {
        showre();
    }
});
    
});

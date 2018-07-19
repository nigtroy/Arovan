$(document).ready(function(){
    
function showre(){
    var url = "/weather?location=";
    
    $('.results_container').show();
    
    var city = $('.user_in').val();
            
    var together = url+city;
    
    if(city==""){
        alert("Please enter a city!");
    } else {
    $.ajax({
	  url:together,
	  success:function(dat){
		var obj = dat;
        console.log(obj);
        console.log(obj.weather[0]);
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

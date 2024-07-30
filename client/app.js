//so we have to locations in html now how do we get locations from backend
//so in javascript there is call called onload so windows.onload is onpageload function
//which we are going to define 
function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for(var i in uiBathrooms) {
      if(uiBathrooms[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
  
  function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for(var i in uiBHK) {
      if(uiBHK[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
  
  function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("uiSqft");
    var bhk = getBHKValue();//these particular functions will return the value what
    //we have clicked for example getbhk will give the value what we have clicked
    //
    var bathrooms = getBathValue();
    var location = document.getElementById("uiLocations");
    var estPrice = document.getElementById("uiEstimatedPrice");
  
     //var url = "http://127.0.0.1:5000/predict_home_price"; //Use this if you are NOT using nginx which is first 7 tutorials
   var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  //my url for price prediction end point is the above and the way you call it
  //is using jquery post call
    $.post(url, {//so this $. is jquery object and you are making a post call
        total_sqft: parseFloat(sqft.value),
        bhk: bhk,
        bath: bathrooms,
        location: location.value
    },function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
        console.log(status);//so in output we are getting that estimated price
        //and we are printing that data.estimated price 
    });
  }
  
  function onPageLoad() {//this function will call certain routines when html
    //page is loaded so when page is loaded locations has to be loaded 
    console.log( "document loaded" );
    // var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
    var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {//it is making a get call to that url ,in data
        // you will get that response back which you got by making get request to 
        //the url in postman application once you get response you need to do 
        //data.locations and you will iterate through locations and add those locations
        //to the dropdown
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
  }
  
  window.onload = onPageLoad;
  //now here for deployment i have changed url here i am not specifying the specific port it should be dynamic
  //now then how does it know which server to go to we are going to run the server at 5000 port only so we need to configure
  //reverse proxy in enginx webserver so that whenever we go to localhost/predict_home_prices t routes those requests
  //to 5000 port 
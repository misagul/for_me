var index = "index=0"
var skip = 11;
const interval = setInterval(function() {
    var parts = document.location.href.split("&");
    var index2 = parts[parts.length-1];
    if(index != index2){
        index = index2;
        var vid = document.getElementsByTagName("video")[0];
        vid.currentTime = skip;
    }
 }, 1000);

// clearInterval(interval)

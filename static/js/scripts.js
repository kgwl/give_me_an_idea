/*
* Function resizeToFit() has been taken from:
* https://stackoverflow.com/questions/18229230/dynamically-changing-the-size-of-font-size-based-on-text-length-using-css-and-ht
*
* */
$(document).ready(function (){
    resizeToFit();
})

function resizeToFit(){
    var fontSize = $("#description").css("font-size");
    $("#description").css("font-size",parseFloat(fontSize) - 2);
    console.log($("#description").height(),$("#output").height() - $(".container-header").height());
    if ($("#description").height() >= $("#output").height() - $(".container-header").height()){
        resizeToFit();
    }
}

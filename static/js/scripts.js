/*
* Function resizeToFit() has been taken from:
* https://stackoverflow.com/questions/18229230/dynamically-changing-the-size-of-font-size-based-on-text-length-using-css-and-ht
*
* */
$(document).ready(function (){
    resizeToFit();
    marginToFit();

})

function resizeToFit(){
    var fontSize = $("#description").css("font-size");
    $("#description").css("font-size",parseFloat(fontSize) - 2);
    if ($("#description").height() >= $("#output").height() - $(".container-header").height()){
        resizeToFit();
    }
}

function marginToFit(){
    var classItems = $(".container");
    var outputHeight = $("#output").height();

    for (i = 0;i<classItems.length;i++){
        item = $("#"+classItems[i].id);
        itemHeight = item.height();
        itemHeight = parseInt((outputHeight - itemHeight)/3);
        item.css("margin-top",itemHeight);
    }

}


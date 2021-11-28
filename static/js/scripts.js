$(document).ready(function () {
    paddingToFit();

    $("#exit").click(function () {
        exitPopup();
    });

});

$(window).resize(function () {
    paddingToFit();
})


function paddingToFit() {
    var windowWidth = $(window).width();

    if (windowWidth >= 992) {
        switchHeight(1);
    } else {
        if (item.css("margin-top") != "0px") {
            switchHeight(0)
        }
    }
}

function switchHeight(value) {
    var outputItems = $(".output");
    var outputHeight = $(".output-row").height();

    for (i = 0; i < outputItems.length; i++) {
        item = $("#" + outputItems [i].id);
        var itemHeight = item.height();
        if (value == 1) {
            itemHeight = parseInt((outputHeight - itemHeight) / 4);
        } else {
            itemHeight = "auto";
        }
        item.css("margin-top", itemHeight);
    }
}

function exitPopup() {
    var item = $("#popup-content");
    item.css('display', 'none');
}

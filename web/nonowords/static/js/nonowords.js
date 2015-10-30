function getUserWordList() {
    var userWordList = $("#userWordList").val();
    userWordList = userWordList.replace(/\n/g,','); //Create CSV 
    return userWordList;
}
function fetchWordList() {
    console.log("fetching word list");
    $("#no-no-list-group").text("");
    var userWordList = getUserWordList();

    if(userWordList.length == 0) {
        $("#errormessage").text("Please enter a list of words");
        $("#errordiv").removeClass("fade");
        return;
    } else {
        $("#errordiv").addClass("fade");
    }

    $.getJSON("/words?words=" + userWordList, function(jsondata) {
        var badwords = jsondata.badwords;
        for(i=0; i < badwords.length; i++) {
            $("#no-no-list-group").append('<li class="list-group-item">'+badwords[i]+'</li>');
        }
    });

    $('html, body').animate({
        scrollTop: $("#no-no-list-group").offset().top
    }, 1000);
}

function downloadWordList() {
    console.log("Downloading file");
    var userWordList = getUserWordList();

    if(userWordList.length == 0) {
        $("#errormessage").text("Please enter a list of words");
        $("#errordiv").removeClass("fade");
        return;
    } else {
        window.location="download?words="+userWordList;
    }
}

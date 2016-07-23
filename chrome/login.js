/**
 * Created by wishket_yg on 2016. 7. 23..
 */

$(document).on('click', '.cancel', function() {
    window.close();
});

$(document).on('click', '.submit', function() {
    var params = {'username': $('#username').val(), 'password': $('#password').val()};
    data = JSON.stringify(params);
    $.ajax({
        type: "POST",
        url: 'http://linknote.yonggari.net/api-token-auth/',
        data: data,
        beforeSend: function (request)
            {
                request.setRequestHeader("Content-Type", 'application/json');
            },
        success: function(data){
            chrome.storage.local.set({'token_linknote': data.token});

            chrome.browserAction.setPopup({"popup": "add.html"});
            window.location.href = 'add.html';
            // setTimeout(
            //     function() {
            //         window.close();
            //     },
            //     1000
            // )
        },
        error: function(data) {
            console.log(data);
        }
    });
});
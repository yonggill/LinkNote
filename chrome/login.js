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
        url: 'http://localhost:8000/api-token-auth/',
        data: data,
        beforeSend: function (request)
            {
                request.setRequestHeader("Content-Type", 'application/json');
            },
        success: function(data){
            chrome.storage.local.set(data);

            chrome.browserAction.setPopup({"popup": "add.html"});
            // setTimeout(
            //     function() {
            //         window.close();
            //     },
            //     1000
            // )
        }
    });
});
/**
 * Created by wishket_yg on 2016. 7. 23..
 */

function get_urls(){
    var url = '';

    chrome.storage.local.get('token_linknote', function (result) {
        if (result.token == undefined) {
            chrome.browserAction.setPopup({"popup": "login.html"});
            window.location.href = 'login.html';
        }
    });

    chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
        $('#url').html(tabs[0].url);
    });
}




$(document).on('click', '.cancel', function() {
    window.close();
});

$(document).on('click', '.submit', function() {
    chrome.storage.local.get('token_linknote', function(result) {
        var token = result.token_linknote;
        var params = {'url': $('#url').text(), 'note': $('textarea').val()};
        data = JSON.stringify(params);
        $.ajax({
            type: "POST",
            url: 'http://linknote.yonggari.net/link/add/',
            data: data,
            beforeSend: function (request)
            {
                request.setRequestHeader("Authorization", 'Bearer '+token);
            },
            success: function(data){
                if (data.error) {
                    chrome.browserAction.setPopup({"popup": "login.html"});
                    window.location.href = 'login.html';
                }
                else {
                    document.body.innerHTML = '<h2 style="margin-top: 100px;"> 페이지 저장이 성공적으로 마무리되었습니다.</h2>';
                    setTimeout(
                        function() {
                            window.close();
                        },
                        1000
                    );
                }
            },
            error: function(data) {
                console.log(data);
                chrome.browserAction.setPopup({"popup": "login.html"});
                window.location.href = 'login.html';
            }
        });    
    });
});

window.onload = get_urls;
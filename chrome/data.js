/**
 * Created by yonggill on 2016. 7. 26..
 */


$(document).on('click', '.cancel-data', function() {
    window.close();
});

$(document).on('click', '.submit-data', function() {
    chrome.storage.local.get('token_linknote', function(result) {
        var token = result.token_linknote;
        var params = {'url': $('#url').text(), 'note': $('#data_view').html()};
        data = JSON.stringify(params);
        $.ajax({
            type: "POST",
            url: 'http://linknote.yonggari.net/link/data/',
            data: data,
            beforeSend: function (request)
            {
                request.setRequestHeader("Authorization", 'Bearer '+token);
            },
            success: function(data){
                if (data.error) {
                    $('#login_section').css('display', 'block');
                    $('#add_section').css('display', 'none');
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
                $('#login_section').css('display', 'block');
                $('#add_section').css('display', 'none');
            }
        });    
    });
});
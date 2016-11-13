$('#button1').click(function() {
    $.ajax({
        url: "fetchvid.html",
        method: 'GET', // or another (GET), whatever you need
        data: {
            name: value, // data you need to pass to your function
            click: True
        },
        success: function (data) {
            // success callback
            // you can process data returned by function from views.py
        }
    });
});
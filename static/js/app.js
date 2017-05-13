'use strict';   // See note about 'use strict'; below

$(document).ready(function(){
    $("#s").click(function()
    {
        $(".IndexPage").hide();
        $(".SignUpPage .container").show();
    });
    $("#l").click(function()
    {
        $(".IndexPage").hide();
        $(".SignInPage .container").show();
    });

    $(".SignUpPage #loginbtn").click(function()
    {
        $(".SignUpPage .container").hide();
        $(".SignInPage .container").show();
    });
     $(".SignInPage #-signupbtn").click(function()
    {
        $(".SignInPage .container").hide();
        $(".SignUpPage .container").show();
    });

});
$(document).ready(function(){
    var gethomescreen = function(){
    $("#browsingWindow").hidel();
    $("#signUpOption").show();
    $("#signInOption").show();
    $("#userInfo").hide();
    $(".userlabel").hide();
    $("#signup").hide();
    $("#signin").hide();
    $("#uploadArtwork").hide();
    };
    gethomescreen();


    $("#signUpOption").on("click",function(){
        $("#browsingWindow").hide();
        $(".userlabel").hide();
        $("#signin").hide();
        $("#uploadArtwork").hide();
        $("#signup").show();
        $("#signUpOption").hide();
        $("#signInOption").hide();

    });
    $("#signInOption").on("click",function(){
        $("#browsingWindow").hide();
        $(".userlabel").hide();
        $("#uploadArtwork").hide();
        $("#signup").hide();
        $("#signin").show();
        $("#signUpOption").hide();
        $("#signInOption").hide();
    });
    $("#signinbtn").on("click",function(){

    });
    $("#signupbtnfromSignInPage").on("click",function(){
        $("#browsingWindow").hide();
        $(".userlabel").hide();
        $("#uploadArtwork").hide();
        $("#signup").show();
        $("#signin").hide();
    });
    $("#signupbtn").on("click",function(){

    });
    $("#signinbtnfromSignUpPage").on("click",function(){
        $("#browsingWindow").hide();
        $(".userlabel").hide();
        $("#uploadArtwork").hide();
        $("#signup").hide();
        $("#signin").show();
    });
    $(".cancelbtn").on("click",function(){
         gethomescreen();
    });


});
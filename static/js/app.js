'use strict';   // See note about 'use strict'; below

var myApp = angular.module('myApp', [
 'ngRoute',
]);

myApp.config(['$routeProvider',
     function($routeProvider) {
         $routeProvider.
             when('/', {
                 templateUrl: '/static/partials/index.html',
             }).
             when('/signup', {
                 templateUrl: '/static/partials/signup.html',
             }).
             when('/signin', {
                 templateUrl: '/static/partials/signin.html',
             }).
             when('/upload', {
                 templateUrl: '/static/partials/upload.html',
             })
             otherwise({
                 redirectTo: '/'
             })

             ;
    }]);
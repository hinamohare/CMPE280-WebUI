'use strict';
var myApp = angular.module('myApp', [ 'ngRoute' ]);


myApp.config(['$routeProvider',     function($routeProvider) {
         $routeProvider.
             when('/', {
                 templateUrl: '../static/partials/index.html',
                 controller: 'IndexCtrl'
             }).
             when('/signup', {
                 templateUrl: '../static/partials/signup.html',
                 controller: 'SignUpCtrl'
             }).
             when('/signin', {
                 templateUrl: '../static/partials/signin.html',
                 controller: 'SignInCtrl'
             }).
             when('/upload', {
                 templateUrl: '../static/partials/upload.html',
                 controller: 'UploadCtrl'
             }).
             otherwise({
                 redirectTo: '/'
             });
    }]);


myApp.controller('SignUpCtrl', ['$scope', '$location', '$http', function($scope, $location, $http) {
    // Add user function

    $scope.addUser = function(user) {
        $scope.new_user = angular.copy(user);

        // Clear out form
        $scope.user = {};

        // Send user info to signup endpoint
        $http({
            url: "/api/signup/",
            method: "POST",
            data: $scope.new_user
        }).success(function (data) {
            // Redirect to login upon success
            $location.path('/login/');
        });
    };
}]);

myApp.controller('IndexCtrl', ['$scope', '$location', '$http', function($scope, $location, $http) {
    // Add user function

    $scope.addUser = function(user) {
        $scope.new_user = angular.copy(user);

        // Clear out form
        $scope.user = {};

        // Send user info to signup endpoint
        $http({
            url: "/api/signup/",
            method: "POST",
            data: $scope.new_user
        }).success(function (data) {
            // Redirect to login upon success
            $location.path('/login/');
        });
    };
}]);

myApp.controller('SignInCtrl', ['$scope', '$location', '$http', function($scope, $location, $http) {
    // Add user function

    $scope.addUser = function(user) {
        $scope.new_user = angular.copy(user);

        // Clear out form
        $scope.user = {};

        // Send user info to signup endpoint
        $http({
            url: "/api/signup/",
            method: "POST",
            data: $scope.new_user
        }).success(function (data) {
            // Redirect to login upon success
            $location.path('/login/');
        });
    };
}]);

myApp.controller('UploadCtrl', ['$scope', '$location', '$http', function($scope, $location, $http) {
    // Add user function

    $scope.addUser = function(user) {
        $scope.new_user = angular.copy(user);

        // Clear out form
        $scope.user = {};

        // Send user info to signup endpoint
        $http({
            url: "/api/signup/",
            method: "POST",
            data: $scope.new_user
        }).success(function (data) {
            // Redirect to login upon success
            $location.path('/login/');
        });
    };
}]);

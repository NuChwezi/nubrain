var app = angular.module('nubrain', []);

app.controller('MainController', [
'$scope',
function($scope){
    $scope.events = [{
            name: 'NuBrain',
            category: 'Hacking',
            timestamp: new Date(),
            tags: ['programming', 'javascript', 'data'],
            detail: 'This is the first event in the Nu Brain!'
        }
    ];

    $scope.addEvent = function(){
        if(!$scope.name || $scope.name === '') { return; }
        if(!$scope.category || $scope.category === '') { return; }

        $scope.events.push({
            name: $scope.name,
            category: $scope.category,
            timestamp: new Date(),
            tags: $scope.tags ? $scope.tags.split(',') : null,
            detail: $scope.detail
        });

        $scope.name = '';
        $scope.category = '';
        $scope.tags = '';
        $scope.detail = '';
    }

    $scope.cloneEvent = function(ev){

        $scope.events.push({
            name: ev.name,
            category: ev.category,
            timestamp: new Date(),
            tags: ev.tags,
            detail: ev.detail
        });

    }

}]);

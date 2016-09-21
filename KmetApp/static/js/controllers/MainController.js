app.controller('MainController', ['$scope' ,'$http', '$route',   function($scope, $http,$route ){

	$scope.search = {};	
	

	$scope.iskanjeOglasa=function(){
		$http.post("http://localhost:8000/app/iskanje_O/", $scope.search)
		.then(function(response) {

           	$scope.oglasi = response.data.oglasi;
           	
	    }, function(response){

	        console.log("shit went wrong");

        });
	};


    $scope.iskanjeKosarice=function(){
        $http.post("http://localhost:8000/app/iskanje_K/", $scope.search)
        .then(function(response) {

            $scope.kosarice = response.data.kosarice;
            
        }, function(response){

            console.log("shit went wrong");

        });
    };

    $scope.kosarica=function(){
         $http.post("http://localhost:8000/app/kosarica_M/")
        .then(function(response) {

            $scope.kosarice = response.data.kosarice;
            
        }, function(response){

            console.log("shit went wrong");

        });
    };



	$scope.oglas_gumb = function(e){

        var oglas_id = angular.element(e.target).attr('data-oglas');
        $scope.oglasID = parseInt(oglas_id);
       				
              };

    $scope.zakljuci_O = function(e){
        var oglas_id = angular.element(e.target).attr('data-oglas');

          $http.post("http://localhost:8000/app/zakljuci_O/", oglas_id)
        .then(function(response){
            
        window.location.reload();
        
        }, function(response){

            console.log("shit went wrong");

        });
    };

   

    $scope.narocilo_I=function(){
    	var kolicina = parseInt(angular.element(document.querySelector('#kolicina')).val());
    	
       	var narocilo = {
	    	id : $scope.oglasID,
	    	kolicina  : kolicina
    	};

        $http.post("http://localhost:8000/app/narocilo_O/", narocilo)
        .then(function(response){

        	
        	$scope.status = response.data.status;
        	console.log($scope.status);

        }, function(response){

        	console.log("shit went wrong");

        });

              	};

$scope.narocilo_K=function(){
        var stevilo_K = parseInt(angular.element(document.querySelector('#stevilo_K')).val());
        var pogostost = angular.element(document.querySelector('#pogostost')).val();

        var narocilo_K = {
            id : $scope.oglasID,
            stevilo_K  : stevilo_K,
            pogostost : pogostost
        };

        $http.post("http://localhost:8000/app/narocilo_K_O/", narocilo_K)
        .then(function(response){

            $scope.status = response.data.status;
            console.log($scope.status);

        }, function(response){

            console.log("shit went wrong");

        });

                };


    $scope.oglas = function(){
    	$scope.oglase = {};
		
    	
    	$http.post("http://localhost:8000/app/oglas_Edit/")
    	.then(function(response){
    		
	    		$scope.oglase = response.data.oglase;
	    		console.log($scope.oglase);


    	}, function(response){
    		console.log("Shit went wrong1");
    	
    	});

    };

   

    $scope.oglas_E = function(){
    	var kolicina = parseInt(angular.element(document.querySelector('#kolicina_O')).val());
    	var ime =angular.element(document.querySelector('#ime_O')).val();
    	var cena = parseInt(angular.element(document.querySelector('#cena_O')).val());
    	var opis  = angular.element(document.querySelector('#opis_O')).val();

    	var edit_O = {
    		ime_O : ime,
    		cena_O : cena,
    		kolicina_O : kolicina,
    		opis_O : opis,
    		id : $scope.oglasID
    	};
    	
    	$http.post("http://localhost:8000/app/oglas_E/", edit_O)
        .then(function(response){
        	
        	$scope.status = response.data.status;
        	console.log($scope.status);

        }, function(response){

        	console.log("shit went wrong");

        });
    };

   

    $scope.narocilo_N= function(){
    	$scope.narocila = {};
    	$http.post("http://localhost:8000/app/narocila_N/")
    	.then(function(response){

    		$scope.narocila = response.data.narocila;
    		console.log($scope.narocila);
    	}, function(response){
    			console.log("shit");
    		});
    };


    $scope.narocilo_K_N = function(){
        $scope.narocila = {};
        $http.post("http://localhost:8000/app/narocila_K_NE/")
        .then(function(response){

            $scope.narocila = response.data.narocila;
            console.log($scope.narocila);
        }, function(response){
                console.log("shit");
            });


    };


	$scope.narocilo_gumb = function(e){

        var narocilo_id = angular.element(e.target).attr('data-narocilo');
        $scope.narociloID = parseInt(narocilo_id);
        

        $http.post("http://localhost:8000/app/obdelaj_N/" , $scope.narociloID)
        .then(function(response){
            window.location.reload();        

        }, function(response){
                console.log("shit");
            });
       				
              };

    $scope.narocilo_gumb_K= function(e){
        var narocilo_id = angular.element(e.target).attr('data-narocilo');
        $scope.narociloID = parseInt(narocilo_id);
        

        $http.post("http://localhost:8000/app/obdelaj_K_N/" , $scope.narociloID)
        .then(function(response){
            window.location.reload();        

        }, function(response){
                console.log("shit");
            });
                    
              };

    

    
    $scope.narocilo_M= function(){
        $scope.narocila = {};
        
        $http.post("http://localhost:8000/app/narocila_M/")
        .then(function(response){

            $scope.narocila = response.data.narocila;
            console.log($scope.narocila);

        }, function(response){
                console.log("shit");
            });
    };


    $scope.narocilo_Obdelano = function(){

        $http.post("http://localhost:8000/app/narocilo_Obdelano/")
        .then(function(response){

            $scope.narocila = response.data.narocila;
            console.log($scope.narocila);

        }, function(response){
                console.log("shit");
            });


    };
   $scope.narocilo_K_Moja= function(){
        $scope.narocila = {};
        
        $http.post("http://localhost:8000/app/narocila_K_Moja/")
        .then(function(response){

            $scope.narocila = response.data.narocila;
            console.log($scope.narocila);

        }, function(response){
                console.log("shit");
            });
    };


    $scope.narocila_K_obdelana = function(){

         $scope.narocila = {};
        
        $http.post("http://localhost:8000/app/narocila_K_obdelana/")
        .then(function(response){

            $scope.narocila = response.data.narocila;
            console.log($scope.narocila);

        }, function(response){
                console.log("shit");
            });

    };


}]);







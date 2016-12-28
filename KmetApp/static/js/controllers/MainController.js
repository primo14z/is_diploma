app.controller('MainController', ['$scope' ,'$http', '$route', '$window', '$rootScope',   function($scope, $http,$route, $window, $rootScope){

	$scope.search = {};	
	
	$scope.iskanjeOglasa=function(){ //funkcija ki pošlje AJAX request s iskalno besedo in dobi nazaj spisek oglasov
		$http.post("http://localhost:8000/app/iskanje_O/", $scope.search)
		.then(function(response) {

           	$scope.oglasi = response.data.oglasi;
           	
	    }, function(response){

	        console.log("shit went wrong");

        });
	};


    $scope.iskanjeKosarice=function(){//funkcija pošlje AJAX request s iskalno besedo in dobi nazaj JSON spisek košaric
        $http.post("http://localhost:8000/app/iskanje_K/", $scope.search)
        .then(function(response) {
           
            $scope.kosarice = response.data.kosarice;
            
        }, function(response){

            console.log("shit went wrong");

        });
    };

    $scope.oglas_view = function(e){/* za ogled oglasa v novem oknu */
        var oglas_id = parseInt(e);
        $rootScope.oglasID =parseInt(oglas_id);
        if($window.location.pathname == "/app/view_oglas/"){
            $window.location.reload();
        }else{
            $window.open('http://localhost:8000/app/view_oglas?oglasID=' + $scope.oglasID);
        }
        
    };
   

    $scope.kosarica=function(){//pošlje AJAX request za vse košarice katere je oddal user in niso bile še zaključene
         $http.post("http://localhost:8000/app/kosarica_M/")
        .then(function(response) {

            $scope.kosarice = response.data.kosarice;
            
        }, function(response){

            console.log("shit went wrong");

        });
    };



	$scope.oglas_gumb = function(e){//funkcija pridobi ID oglasa za katerega smo hoteli oddati naročilo

        var oglas_id = angular.element(e.target).attr('data-oglas');
        $rootScope.oglasID = parseInt(oglas_id);      				
        console.log($scope.oglasID);
              };

    $scope.zakljuci_O = function(e){/*funkcija pridobi ID oglasa katerega želimo zaključiti, ter pošlje AJAX request v katerem 
                                    posreduje ID oglasa in ga zaključi */
        var oglas_id = angular.element(e.target).attr('data-oglas');

          $http.post("http://localhost:8000/app/zakljuci_O/", oglas_id)
        .then(function(response){
            
        window.location.reload();
        
        }, function(response){

            console.log("shit went wrong");

        });
    };

   

    $scope.narocilo_I=function(e){/*funkcija pridobi ID oglasa ter količino katero smo vnesli ob oddaji naročila, ter posreduje view
                                 kateri vnese v bazo*/
    	var kolicina = parseInt(angular.element(document.querySelector('#kolicina')).val());
       	var narocilo = {
	    	id : $rootScope.oglasID,
	    	kolicina  : kolicina
    	};
        console.log(narocilo);
        $http.post("http://localhost:8000/app/narocilo_O/", narocilo)
        .then(function(response){

        	
        	$scope.status = response.data.status;
        	console.log($scope.status);
            if($window.location.pathname == "/app/view_oglas/"){
                $scope.oglas_view($scope.oglasID);
            }
           
        }, function(response){

        	console.log("shit went wrong");

        });

              	};

$scope.narocilo_K=function(){/*funkcija dobi ID ter količino katero smo vnesli ob oddaji naročila za košarico, ter posreduje view kateri 
                            vnese v bazo */
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


    $scope.oglas = function(){/*pošlje AJAX request za pridobitev oglasov oddanih od uporabnika, prejme jih v JSON formatu */
      	$scope.oglase = {};
	  	
    	$http.post("http://localhost:8000/app/oglas_Edit/")
    	.then(function(response){
    		
	    		$scope.oglasi = response.data.oglasi;
	    		console.log($scope.oglasi);


    	}, function(response){
    		console.log("Shit went wrong1");
    	
    	});

    };

   

    $scope.oglas_E = function(){/* prejme podatke s katerimi želi uporabnik popraviti obstoječi oglas
                                jih shrani spremenljivke ter posreduje v vie, kateri jih shrani v bazo */

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

   

    $scope.narocilo_N= function(){//funckija pošlje AJAX request s katerim dobi podatke v JSON formatu, podatki 
                                //so vsa neobdelana naročila na obstoječi oglas, kjer je uporabnik prodajalec
    	$scope.narocila = {};
    	$http.post("http://localhost:8000/app/narocila_N/")
    	.then(function(response){

    		$scope.narocila = response.data.narocila;
    		console.log($scope.narocila);
    	}, function(response){
    			console.log("shit");
    		});
    };


    $scope.narocilo_K_N = function(){//funckija pošlje AJAX request s katerim dobi podatke v JSON formatu, podatki 
                                //so vsa neobdelana naročila na obstoječo košarico, kjer je uporabnik prodajalec
        $scope.narocila = {};
        $http.post("http://localhost:8000/app/narocila_K_NE/")
        .then(function(response){

            $scope.narocila = response.data.narocila;
            console.log($scope.narocila);
        }, function(response){
                console.log("shit");
            });


    };


	$scope.narocilo_gumb = function(e){/*funkcija pridobi ID naročila, katerega uporabnik želi zaključiti, S AJAX requestom ta ID 
                                        posreduje View kateri na podlagi tega ID spremeni vrednost v bazi */

        var narocilo_id = angular.element(e.target).attr('data-narocilo');
        $scope.narociloID = parseInt(narocilo_id);
        

        $http.post("http://localhost:8000/app/obdelaj_N/" , $scope.narociloID)
        .then(function(response){
            window.location.reload();        

        }, function(response){
                console.log("shit");
            });
       				
              };

    $scope.narocilo_gumb_K= function(e){/*funkcija pridobi ID naročila, katerega uporabnik želi zaključiti, S AJAX requestom ta ID 
                                        posreduje View kateri na podlagi tega ID spremeni vrednost v bazi */
        var narocilo_id = angular.element(e.target).attr('data-narocilo');
        $scope.narociloID = parseInt(narocilo_id);
        

        $http.post("http://localhost:8000/app/obdelaj_K_N/" , $scope.narociloID)
        .then(function(response){
            window.location.reload();        

        }, function(response){
                console.log("shit");
            });
                    
              };    

    
    $scope.narocilo_M= function(){//Ajax Request za spisek vseh naročil katere je uporabnik oddal za oglas
        $scope.narocila = {};
        
        $http.post("http://localhost:8000/app/narocila_M/")
        .then(function(response){

            $scope.narocila = response.data.narocila;
            console.log($scope.narocila);

        }, function(response){
                console.log("shit");
            });
    };


    $scope.narocilo_Obdelano = function(){//Ajax request za spisek vseh naročil katera so bila obdelana in je user prodajalec

        $http.post("http://localhost:8000/app/narocilo_Obdelano/")
        .then(function(response){

            $scope.narocila = response.data.narocila;
            console.log($scope.narocila);

        }, function(response){
                console.log("shit");
            });
    };

   $scope.narocilo_K_Moja= function(){//Ajax Request za spisek vseh naročil katere je uporabnik oddal za košarico
        $scope.narocila = {};
        
        $http.post("http://localhost:8000/app/narocila_K_Moja/")
        .then(function(response){

            $scope.narocila = response.data.narocila;
            console.log($scope.narocila);

        }, function(response){
                console.log("shit");
            });
    };


    $scope.narocila_K_obdelana = function(){//Ajax request za spisek vseh naročil katera so bila obdelana in je user prodajalec-->Košarica

         $scope.narocila = {};
        
        $http.post("http://localhost:8000/app/narocila_K_obdelana/")
        .then(function(response){

            $scope.narocila = response.data.narocila;
            console.log($scope.narocila);

        }, function(response){
                console.log("shit");
            });
    };//narocila_K_obdelana

 
}]);

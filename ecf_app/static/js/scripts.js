//  --- OFFER ---

// CREATE
$('#btn-save').click(function () { 

    let output = "";

    let sid = $('#stuid').val() // hidden input for EDIT
    // take the value of all input in the form (information 'NAME' in the browser)
    let name = $('#id_name').val();
    let description = $('#id_description').val();
    let nbPers = $('#id_nbPers').val();
    let discount = $('#id_discount').val();
    
    // CREATE - take the value of the input data typed by the user
    // EDIT - take the value of the input data to be edited 
    mydata = {
        stuid: sid, // hidden input for EDIT
        name: name,
        description: description,
        nbPers: nbPers,
        discount:discount
    }

    // appel AJAX
    $.ajax({
        url: 'http://127.0.0.1:8000/data-save',        
        type: "POST",
        data: mydata,

        success: function(data) {
            
            // prendre les données de data afin de refaire le tableau de la liste des offres --> pas de rechargement de la page
            x = data.offer_data
            // trier par id les data               
            x.sort((a, b) => parseInt(a.id) - parseInt(b.id));
            if(data.status == 'Data saved'){
                for (let i = 0; i < x.length; i++) {
                    // construire le contenu du tableau en fonction de données reçues en AJAX
                    output += "<tr><td>" + x[i].id +
                        "</td><td>" + x[i].name +
                        "</td><td>" + x[i].description +
                        "</td><td>" + x[i].nbPers +
                        "</td><td>" + x[i].discount +
                        "</td><td> <input type='button' value='Edit' class='btn btn-outline-warning btn-edit btn-sm' data-sid=" + 
                            x[i].id + ">" + " " +
                            "<input type='button' value='Delete' class='btn btn-outline-danger btn-del btn-sm' data-sid=" +
                            x[i].id + ">"+
                            "</td></tr>"
                }   

                
                // mettre les données de l'appel ajax sur le body du tableau
                $('#tbody').html(output);

                // reset le formulaire une fois soumis
                $('form')[0].reset();

            }
            if(data.status == 'Unable to save'){
                console.log('Unable to save')
            }

        },
    });
});



// DELETE
$('#tbody').on("click", ".btn-del", function() {

    // récuperer le id de l'offre à partir du 'data-sid'
    let id = $(this).attr("data-sid")

    mydata = {
        sid:id,
    };

    mythis = $(this);
    // <input type="button" value="Delete" class="btn btn-outline-danger btn-del btn-sm" data-sid="52"></input>


    // appel AJAX
    $.ajax({
        method: "POST",
        url: 'http://127.0.0.1:8000/data-delete',        
        data: mydata,
        success: function(data) {
            console.log(data.status)

            if(data.status == 1){
                console.log('Data deleted')
                // prendre et fadeOut le this (input...) le plus proche du tr
                $(mythis).closest("tr").fadeOut();
               
            } 

            if(data.status == 0){
                console.log('Unable to delete data')
            } 
        },
    });
})


// EDIT
$('#tbody').on("click", ".btn-edit", function() {
    
    // récuperer le id de l'offre à partir du 'data-sid'
    let id = $(this).attr("data-sid")
    
    mydata = {
        sid:id,
    };
    
    mythis = $(this);
    console.log(mydata);
    // {sid: '13'}
    // le reste ne change pas: description, nbPers, discount

    // appel AJAX
    $.ajax({
        method: "POST",
        url: 'http://127.0.0.1:8000/data-edit', 
        data: mydata,
        success: function(data) {
            // Prépopuler avec data les données du formulaire sur le browser
            // a partir du id de chaque propriété dans le formulaire
            
            console.log(data)
            // {id: 13, name: 'famille', description: 'valable pour 4 peronnes', nbPers: 1, discount: 30}
            $('#stuid').val(data.id);
            $('#id_name').val(data.name);
            $('#id_description').val(data.description);
            $('#id_nbPers').val(data.nbPers)
            $('#id_discount').val(data.discount)
        },
    });
})


// --- CHOIX DE L'OFFRE ---

$('#btn-choisir').click(function (e) { 

    e.preventDefault();

    // récuperer la valeur du select selectionné dans le formulaire
    var selectElmt = document.getElementById("target-select");
    var valeurselectionnee = selectElmt.options[selectElmt.selectedIndex].value;
    var textselectionne = selectElmt.options[selectElmt.selectedIndex].text;

    //  mettre dans cet input hidden le id de l'offre selectionée qui sera récupéré dans le view ultérieurement
    $('#offer_id').val(valeurselectionnee)

    // récupérer le csrf tokent dans le formulaire
    token = $("#offer-form").find('input[name=csrfmiddlewaretoken]').val()


     $.ajax({
        type: "post",
        url: 'http://127.0.0.1:8000/cart', 
        data: {
            offer_id : valeurselectionnee,
            csrfmiddlewaretoken: token,
            
            // sera récupéré dans le view
            action: 'post'
        },

        

        success: function (response) {
        // mettre a jour l'offre choisie dans le panier en fonction du choix de l'utilisateur
          let offer = response.offer_values[0]
          let cart = response.cart_values[0]
          let orders = response.order_values
          $('#selected-offer-name').text(offer.name)
          $('.selected-offer-nbPers').text(offer.nbPers)
          $('.selected-offer-remise').text(offer.discount)


            let prices = offer.price
            let total = cart.total

            $('#total').text(total)
        }
    });
});

// --- ADD TO CART  ---

$('#btn-panier').click(function (e) { 

    e.preventDefault();

    competition_id = $('#btn-panier').val()

    // récupérer le csrf tokent dans le formulaire
    token = $("#form-panier").find('input[name=csrfmiddlewaretoken]').val()


     $.ajax({
        type: "POST",
        url: 'competition/'+ competition_id + '/add-to-cart/', 
        data: {
            competition_id: competition_id,
            csrfmiddlewaretoken: token,
            
            // sera récupéré dans le view
            action: 'post-add-to-cart'
        },

        success: function (response) {
            let output = "<div class='alert alert-success role='alert'>" + response['status'] + "</div>"
            $('#message-content-ajax').html(output)
            $('#total').text('')
        }
    });
});

// DELETE FROM CART
$('#tbody-ajax').on("click", ".btn-del-ajax", function() {

    // récuperer le id de l'offre à partir du 'data-sid'
    let order_id = $(this).attr("data-id")

    mydata = 

    mythis = $(this);
    // <input type="button" value="remove" class=" btn-del-ajax btn btn-sm btn-outline-danger rounded-4 text-danger" data-id="38">

    token = $("#remove-form").find('input[name=csrfmiddlewaretoken]').val()

    // appel AJAX
    $.ajax({
        method: "POST",
        url: 'http://127.0.0.1:8000/remove-from-cart/'+ order_id,        
        data: {
            order_id:order_id,
            csrfmiddlewaretoken: token,
            action: 'remove-from-cart-ajax'
        },

        success: function (response) {
            $(mythis).closest("tr").fadeOut();
            let output = "<div class='alert alert-success role='alert'>" + response['status'] + "</div>"
            $('#message-content-ajax').html(output)
            $('#total').text('')


        }
    });
});


$('#rafraichir-btn').click(function () { 
    $('#total').text('')
});



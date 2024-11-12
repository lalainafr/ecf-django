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
            
            // prendre les données du data afin de refaire le tableau de la liste des offres --> pas de rechargement de la page
            x = data.offer_data               

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
    // <input type="button" value="Delete" class="btn btn-outline-danger btn-del btn-sm" data-sid="52"></input>


    // appel AJAX
    $.ajax({
        method: "POST",
        url: 'http://127.0.0.1:8000/data-edit', 
        data: mydata,
        success: function(data) {
            // Prépopuler avec data les données du formulaire sur le browser
            // a partir du id de chaque propriété dans le formulaire
            $('#stuid').val(data.id);
            $('#id_name').val(data.name);
            $('#id_description').val(data.description);
            $('#id_nbPers').val(data.nbPers)
            $('#id_discount').val(data.discount)
        },
    });
})

// CREATE
$('#btn-save').click(function () { 

    let output = "";

    let sid = $('#stuid').val() // hidden input for EDIT
    // take the value of all input in the form (information 'NAME' in the browser)
    let name = $('#id_name').val();
    let description = $('#descritpion').val();
    let nbPers = $('#id_nbPers').val();
    let discount = $('#id_discount').val();

   
    console.log(name);
    console.log(description);
    console.log(nbPers);
    console.log(discount);

        // CREATE - take the value of the input data typed by the user
        // EDIT - take the value of the input data to be edited 
        mydata = {
            stuid: sid, // hidden input for EDIT
            name: name,
            email: email,
            course: course
        }

        // appl AJAX
        $.ajax({
            // url: "{% url 'save-data' %}",
            url: "save/",
            method: "POST",
            data: mydata,

            success: function(data) {
                // console.log(data.status)
                console.log('Data submitted')
              
                // --> put in the content of the table in the right side the data content
                x = data.student_data               

                if(data.status == 'Data saved'){
                    for (let i = 0; i < x.length; i++) {
                        // recomposer le contenu tu tableau en fonction de données recues en AJAX
                       output += "<tr><td>" + x[i].id +
                            "</td><td>" + x[i].name +
                            "</td><td>" + x[i].email +
                            "</td><td>" + x[i].course +
                            "</td><td> <input type='button' value='Edit' class='btn btn-outline-warning btn-edit btn-sm' data-sid=" + 
                             x[i].id + ">" + " " +
                             "<input type='button' value='Delete' class='btn btn-outline-danger btn-del btn-sm' data-sid=" +
                             x[i].id + ">"
                    }   

                    
                    // load ajax data in the table body
                    $('#tbody').html(output);

                    // reset form once submitted
                    $('form')[0].reset();

                }
                if(data.status == 'Unable to save'){
                    console.log('Unable to save')
                }

            },
        });
    }

});


// DELETE
$('#tbody').on("click", ".btn-del", function() {
    // console.log('Del button clicked on the TBODY ');

    // récuperer le id du student à partir du 'data-sid'
    let id = $(this).attr("data-sid")

    mydata = {
        sid:id,
    };

    mythis = $(this);
    // <input type="button" value="Delete" class="btn btn-outline-danger btn-del btn-sm" data-sid="52"></input>


    // appel AJAX
    $.ajax({
        method: "POST",
        url: "delete/",
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
    
    // récuperer le id du student à partir du 'data-sid'
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
        url: "edit/",
        data: mydata,
        success: function(data) {
            // NAME du formulaire sur le browser
            $('#stuid').val(data.id);
            $('#id_name').val(data.name);
            $('#id_email').val(data.email);
            $('#id_course').val(data.course)
        },
    });
})
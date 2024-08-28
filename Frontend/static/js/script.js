$(document).ready(function() {
    $('#add-algorithm-form').on('submit', function(event) {
        event.preventDefault();
        var algorithm = $('#algorithm').val();

        $.ajax({
            url: '/add_algorithm',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({algorithm: algorithm}),
            success: function(response) {
                $('#selected-algorithms').append(response.html);
            }
        });
    });
    
    $('#file-upload').on('change', function() {
        if (this.files.length > 0) {
            $('#algorithm').prop('disabled', false);
            $('.btn-add').prop('disabled', false);
            $('#selected-algorithms-container').show(); // Mostra a div de algoritmos selecionados
        }
    });

    $(document).on('click', '.remove-algorithm', function() {
        var algorithmName = $(this).data('name');
        var elementToRemove = $('#' + algorithmName);

        $.ajax({
            url: '/remove_algorithm',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({algorithm: algorithmName}),
            success: function(response) {
                if (response.success) {
                    elementToRemove.remove();
                }
            }
        });
    });

    $('#file-upload').on('change', function() {
        if (this.files.length > 0) {
            $('#algorithm').prop('disabled', false);
            $('.btn-add').prop('disabled', false);
        }
    });
});


function SubmitAlgorithims(){

    const options    = document.querySelector(".data-options").querySelectorAll("input");
    const file       = document.getElementById("file-upload");
    const algorithmsBlock = document.querySelectorAll(".algorithm-block");

    const processing = {};
    options.forEach(input => {
        switch (input.type){
            case 'range':
                processing[input.id] = input.value;
                break;
            case 'checkbox':
                processing[input.id] = input.checked;
                break;

            default:
                console.log("Input não reconhecido.")
        }
    });

    const algorithms = {};
    algorithmsBlock.forEach(block => {
        
        const algorithmName = block.id;

        const parametros = {};

        const inputs = block.querySelectorAll("input, select");

        inputs.forEach(input => parametros[input.id] = input.value);


        algorithms[algorithmName] = parametros;
    })

    console.log(algorithms)

    const data = {
        processing:processing,
        algorithms: algorithms
    }

    const formData = new FormData();
    formData.append('file', file.files[0]);
    formData.append('data', JSON.stringify(data));

    fetch(url_submit, {
        method: 'POST',
        body: formData
    }).then(response => response.json())
    .then(data => {
        console.log("Sucesso:", data)
    })
    .catch((error) => {
        console.log("erro:" + error)
    }); 
}

function updateValue(val) {
    document.getElementById('trainValue').textContent = val + '%';
}
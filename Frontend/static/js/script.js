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


async function SubmitAlgorithims(url){

    const file            = document.getElementById("file-upload");
    const label           = document.getElementById("data_labels");
    const options         = document.querySelectorAll(".data-options input");
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
        label: label.value,
        processing:processing,
        algorithms: algorithms
    }

    const formData = new FormData();
    formData.append('file', file.files[0]);
    formData.append('data', JSON.stringify(data));

    try {
        const response = await fetch('/submit', {
            method: 'POST',
            body: formData  // Envia os dados e o arquivo
        });

        if (!response.ok) {
            throw new Error('Erro ao enviar os dados');
        }

        // Trata a resposta como texto ou HTML
        const result = await response.text();
        
        // Renderiza o HTML recebido na página
        document.body.innerHTML = result;

    } catch (error) {
        console.error('Erro:', error);
    }
};

function updateValue(val) {
    document.getElementById('trainValue').textContent = val + '%';
}


async function include_labels(event){
    const select = document.getElementById("data_labels");

    file = event.target;

    const formData = new FormData();
    formData.append('file', file.files[0]);
    
    try {
        const response = await fetch('/file', {
            method: 'POST',
            body: formData  // Envia os dados e o arquivo
        });

        if (!response.ok) {
            throw new Error('Erro ao enviar os dados');
        }

        // Trata a resposta como texto ou HTML
        const result = await response.json();
        console.log(result.columns);
        select.innerHTML = ""
        result.columns.forEach(column => {

            const option = document.createElement("option");

            option.id = column;
            option.textContent = column;
            select.appendChild(option);
        });

    } catch (error) {
        console.error('Erro:', error);
    }
}
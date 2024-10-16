$(document).ready(function() {
    $('#add-algorithm-form').on('submit', function(event) {
        event.preventDefault();
        var algorithm = $('#algorithm').val();

        $.ajax({
            url: '/algorithm/add_algorithm',
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
            url: '/algorithm/remove_algorithm',
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
            $('#btn-add-algorithm').prop('disabled', false);
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

    const algorithms = [];
    algorithmsBlock.forEach(block => {
        
        
        const parametros = {};
        parametros["algorithm"] =  block.id;

        const inputs = block.querySelectorAll("input, select");

        inputs.forEach(input => parametros[input.id] = input.value);


        algorithms.push(parametros)
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
        const response = await fetch(url, {
            method: 'POST',
            body: formData  // Envia os dados e o arquivo
        });

        if (!response.ok) {
            throw new Error('Erro ao enviar os dados');
        }

        // Trata a resposta como texto ou HTML
        const result = await response.text();
        
        // Renderiza o HTML recebido na página
        document.open();  // Abre o documento para escrita
        document.write(result);  // Substitui todo o HTML da página
        document.close();
        
    } catch (error) {
        console.error('Erro:', error);
    }
};

function updateValue(val) {
    document.getElementById('trainValue').textContent = val + '%';
}

function include_labels(event) {
    var file = event.target.files[0];
    var formData = new FormData();
    formData.append('file', file);

    $.ajax({
        url: '/algorithm/file',
        type: 'POST',
        data: formData,
        processData: false,  // Impede que o jQuery processe os dados
        contentType: false,  // Define o tipo de conteúdo como falso
        success: function(response) {
            // Limpa as opções anteriores
            $('#data_labels').empty();

            // Verifica se a resposta contém colunas
            if (response.columns) {
                // Preenche o dropdown com as colunas
                response.columns.forEach(function(column) {
                    $('#data_labels').append(new Option(column, column));
                });
            } else {
                // Exibe uma mensagem de erro se algo estiver errado
                $('#data_labels').append(new Option('Erro ao carregar colunas', ''));
            }
        },
        error: function() {
            // Exibe uma mensagem de erro caso a requisição falhe
            alert('Erro ao carregar o arquivo.');
        }
    });
}
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



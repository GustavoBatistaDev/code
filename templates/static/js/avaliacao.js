function avaliacao_form(action) {
    let action_split = action.split('/')
    let end_action = action_split[action_split.length - 1]
    let url = ''
    if (/^\d+$/.test(end_action)){
        url = '/form_avaliacao?' + new URLSearchParams({
            id: end_action,
        })
    }else{
        url = '/form_avaliacao/'
    }
    fetch(url).then(function (response) {
        return response.text();
    }).then(function (html) {
        let formElement = $('#avaliacao_form')
        formElement.attr('action', action)
        let formElementContent = formElement.find('.content-form')
        formElementContent.html(html)
        jquery_formset()
        let myModal = new bootstrap.Modal('#avaliacao_modal');
        myModal.show()
    }).catch(function (err) {
        console.warn('Something went wrong.', err);
    });
}

function get_edit_avaliacao(id) {
    fetch('/form_avaliacao/'+ new URLSearchParams({
        id: id,
    })).then(function (response) {
        return response.text();
    }).then(function (html) {
        console.log(html);

    }).catch(function (err) {
        console.warn('Something went wrong.', err);
    });
}

function jquery_formset() {
    $(function () {
        $(".inlineform").formset({
            prefix: "anotacao_set",
            addText: "Adicionar anotação",
            deleteText: "Remover",
            deleteCssClass: "btn btn-danger mt-2 delete-row",
            addCssClass: "btn btn-primary mt-3 add-row",
            hideLastAddForm: true,
        });
    });
}
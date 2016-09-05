// # on click of the add-to-suicase button I want it to add the item to the Suitcase Items table....
"use strict";

$('.add-to-suitcase-btn').click(function(){

    console.log('got here')

    var suitcaseId = $('#suitcase.suitcase_id').val()
    var itemId = $('#item.item_id').val()

    $.ajax({
        type: "post",
        url: "add",
        data: {'suitcase_id': 'suitcaseId', 'item_id': 'itemId', 'action': 'addToSuitcase'},
        })
    })

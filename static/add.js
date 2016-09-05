// # on click of the add-to-suicase button I want it to add the item to the Suitcase Items table....
"use strict";

$(document).on('click', '.add-to-suitcase-btn', function(){
    // listen to all current and future buttons with this class 

    var suitcaseId = $(this).attr('suitcaseid')
    var itemId = $(this).attr('itemid')

    console.log('got here', suitcaseId, itemId)

    $.ajax({
        type: "post",
        url: "add",
        data: {'suitcase_id': suitcaseId, 'item_id': itemId, 'action': 'addToSuitcase'},
        })
    })

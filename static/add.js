// # on click of the add-to-suicase button I want it to add the item to the Suitcase Items table....
"use strict";

$(document).on('click', '.add-to-suitcase-btn', function(){
    // listen to all current and future buttons with this class 

    var suitcaseId = $(this).attr('suitcaseid')
    var itemId = $(this).attr('itemid')

    console.log('got here', suitcaseId, itemId)

    $.ajax({
        type: "post",
        url: "http://localhost:5000/add",
        data: {'suitcase_id': suitcaseId, 'item_id': itemId, 'action': 'addToToday'},
        })
    })

$(document).on('click', '.today-btn', function(){
    // listen to all current and future buttons with this class 

    var todayId = $(this).attr('todayid')
    var itemId = $(this).attr('itemid')

    console.log('got here', todayId, itemId)

    $.ajax({
        type: "post",
        url: "http://localhost:5000/add",
        data: {'today_id': todayId, 'item_id': itemId, 'action': 'addToToday'},
        })
    })


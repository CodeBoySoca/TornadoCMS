$(() => {

    $('#add-column').on('click', (e) => {
        var count = 3
        $(`<input type="text" name="columnname#{count++}" placeholder="Column Name" required>`).insertBefore('#project-container form input[type="button"]')
    })

    $('#dashboard-add-project').on('click', (e) => {
        e.preventDefault()
        $('body').append('<div class="overlay">\
        <div id="message-popup">\
            <h3>Saved</h3>\
            <p>Project has been saved</p>\
            <button id="send-button">send</button>\
            </div></div>').fadeIn(1500)

        $('#send-button').on('click', (e) => {
            $('.overlay').remove()
        })    

    })

    $('#remove').on('click', (e) => {
        e.preventDefault()
        $('body').append('<div class="overlay">\
        <div id="message-popup">\
            <h3>Deleted</h3>\
            <p>Project has been deleted/p>\
            <button id="send-button">send</button>\
            </div></div>').fadeIn(1500)

        $('#send-button').on('click', (e) => {
            $('.overlay').remove()
        }) 
    })

})
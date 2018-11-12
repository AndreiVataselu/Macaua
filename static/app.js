$(function(){

    var element = document.getElementById("console");
    function scroll(){
        element.scrollTop = element.scrollHeight;
    }

    var modal = document.getElementById("pickSuit");

   $('.drawCard').on('click', function(){
      req = $.ajax({
         url: '/drawCard',
         type: 'POST'
      });

      req.done(function(resp) {
         $('.playerDeck').html(resp.player_cards);
         $('#console').append(resp.console_text);
         scroll();

      });
   });

   $(document).on('click', 'div.playerDeck' ,function(e){
      req = $.ajax({
          url : '/chosenCard',
          type : 'POST',
          data: JSON.stringify(e.target.id, null, '\t'),
          contentType: 'application/json;charset=UTF-8'

      });

      req.done(function(resp){
        $('.playerDeck').html(resp.player_cards);
        $('.tableCard').html(resp.table_card);
        $('#console').append(resp.console_text);
         scroll();
         if(resp.ace==true){
             console.log("ace-true");
             modal.style.display = "block";
         }
      });
   });

   $(document).on('click', 'span.suit', function(e){
       console.log(e.target.id);
       req = $.ajax({
           url: '/changeSuit',
           type: 'POST',
           data: JSON.stringify(e.target.id, null, '\t'),
           contentType: 'application/json;charset=UTF-8'
       });

       req.done(function(resp){
           $('#console').append(resp.console_text);
           scroll();
           modal.style.display = "none";
       });
   });
});
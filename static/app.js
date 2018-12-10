$(function(){

    var element = document.getElementById("console");
    function scroll(){
        element.scrollTop = element.scrollHeight;
    }

    var modal = document.getElementById("pickSuit");

   $('.drawCard').on('click', function(){
      req = $.ajax({
            url: '/drawCard',
            type: 'POST',
            async: false
      });

      req.done(function(resp) {
         $('.playerDeck').html(resp.player_cards);
         $('#console').html(resp.console_text);
         scroll();
         aiMove(resp.turnsToMake);


      });
   });

   $(document).on('click', 'div.playerDeck' ,function(e){
      req = $.ajax({
          url : '/chosenCard',
          type : 'POST',
          data: JSON.stringify(e.target.id, null, '\t'),
          contentType: 'application/json;charset=UTF-8',
          async: false

      });

      req.done(function(resp){
        $('.playerDeck').html(resp.player_cards);
        $('.tableCard').html(resp.table_card);
        $('#console').html(resp.console_text);
         scroll();
         if(resp.ace===true){
             console.log("ace-true");
             modal.style.display = "block";
         } else {
             checkEndGame();
             aiMove(resp.turnsToMake);
         }
      });
   });

   $(document).on('click', 'span.suit', function(e){
       req = $.ajax({
           url: '/changeSuit',
           type: 'POST',
           data: JSON.stringify(e.target.id, null, '\t'),
           contentType: 'application/json;charset=UTF-8',
           async: false
       });

       req.done(function(resp){
           $('#console').html(resp.console_text);
           scroll();
           modal.style.display = "none";
           aiMove(resp.turnsToMake);
       });
   });

   function checkSkipTurn(){
       req = $.ajax({
           url: '/playerWaitTurn',
           type: 'POST',
           async: false
       });

       req.done(function(resp){
          $('#console').html(resp.console_text);
          scroll();

          console.log(resp.skipPlayer);
          if(resp.skipPlayer){
              console.log(resp.skipPlayer);
              aiMove(resp.turnsToMake);
          }
       });
   }

   function checkEndGame(){
       req = $.ajax({
           url: '/checkEndGame',
           type: 'POST',
           async: false
       });

   }

   function aiMove(turnsToMake){
       for (i=0; i < turnsToMake; i++) {
           req = $.ajax({
                url: '/AImove',
                type: 'POST',
                async: false
           });

           req.done(function(resp){
              $('#console').html(resp.console_text);
              scroll();
              $('.tableCard').html(resp.table_card);
              $('.aiPlayers').html(resp.aiPlayers);
              checkEndGame();
           });
       }

       req = $.ajax({
           url: '/playerTakeCards',
           type: 'POST',
           async: false
       });

       req.done(function(resp){
           $('#console').html(resp.console_text);
           scroll();
           $('.playerDeck').html(resp.player_cards);
           checkEndGame();
           checkSkipTurn();
       });
   }
});
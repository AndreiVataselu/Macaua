$(function(){
   $('.drawCard').on('click', function(){
      req = $.ajax({
         url: '/drawCard',
         type: 'POST'
      });

      req.done(function(resp) {
         $('.playerDeck').html(resp.player_cards);

      });
   });

   $(document).on('click', function(e){
      req = $.ajax({
          url : '/chosenCard',
          type : 'POST',
          data: JSON.stringify(e.target.id, null, '\t'),
          contentType: 'application/json;charset=UTF-8'

      });

      req.done(function(resp){
        $('.playerDeck').html(resp.player_cards);
        $('.tableCard').html(resp.table_card);
      });
   });
});
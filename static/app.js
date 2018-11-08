$(function(){
   $('.drawCard').on('click', function(){
      req = $.ajax({
         url: '/drawCard',
         type: 'POST'
      });

      req.done(function(resp) {
         $('.playerDeck').append(resp.data);

      });

   });

   $('.playerCard').on('click', function(){
      req = $.ajax({
          url : '/cardChose',
          type : 'POST'
      });
   });
});
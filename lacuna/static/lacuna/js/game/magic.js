function magicinit(){

var values = [
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0],
];
var success_value = 6;
var diceOptions={
	revert: "invalid",
	stop: function(){
        // Make it properly draggable again
        $(this).draggable('option','revert','invalid');
    },
};
initMagicSumGame();
function initMagicSumGame(){
	var ele="";
	for(var i=0;i<7;i++){
		for(var j=i;j<7;j++){
			ele += '<div class="dice_cont"> <div class="top_val" data-val="'+i+'">'+i+'</div> <div class="bottom_val" data-val="'+j+'">'+j+'</div> </div>';
		}
	}
	$('#dice_wrapper').html(ele);
	$('.dice_cont').draggable(diceOptions);
	$('.drop_dice').droppable({
		drop: function(event,ui){
	        var $this = $(this);
	        
	        // Check number of elements already in
	        if($this.find('.dice_cont').length >= 1){
	            // Cancel drag operation (make it always revert)
	            ui.draggable.draggable('option','revert',true);
	            return;
	        }

	        // Put dragged item into container
	        ui.draggable.appendTo($this).css({
	            top: '0px',
	            left: '0px'
	        });
	        calculateScore();
	    }
	});
	$('.dice_cont').click(function(){
		var top = $(this).find('.top_val');
		var bot = $(this).find('.bottom_val');
		var temp = bot.data('val');
		bot.data('val',top.data('val'));
		bot.text(top.data('val'));
		top.data('val',temp);
		top.text(temp);
	});
	$('#place_dice').on('click','.dice_cont',function(){
		calculateScore();
	});
}
$('#dice_wrapper').droppable({
	drop: function(event,ui){
        var $this = $(this);

        // Put dragged item into container
        ui.draggable.appendTo($this).css({
            top: '0px',
            left: '0px'
        });
        
        calculateScore();
    }
});
function calculateScore(){
	var success=true;
	var s = [0,0,0,0,0,0,0,0,0,0];
	$('.drop_dice').each(function(){
        var $dc = $(this).find('.dice_cont');
        if($dc.length!=0)
        {
        	values[$(this).data('i')][$(this).data('j')] = $dc.find('.top_val').data('val');
        	values[($(this).data('i')+1)][$(this).data('j')] = $dc.find('.bottom_val').data('val');
        }
        else{
        	success = false;
        	values[$(this).data('i')][$(this).data('j')] = 0;
        	values[($(this).data('i')+1)][$(this).data('j')] = 0;
        }
    });
    
    for(var i=0;i<values.length;i++){
    	for(var j=0;j<values[i].length;j++){
    		s[i+6] += values[i][j];
    		s[j+1] += values[i][j];
    	}
    	s[0] += values[i][i];
    	s[5] += values[i][3-i];
    }
    for(var i=0;i<s.length;i++){
    	$('#sum'+(i+1)).html(s[i]);
    	if(s[i]!=success_value)
    	{
    		success = false;
    	}
    }
    if(success){
    	alert('You did it');
    }
}
}
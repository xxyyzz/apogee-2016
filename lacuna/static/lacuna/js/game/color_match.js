var colorOptions={
	revert: "invalid",
	stop: function(){
        // Make it properly draggable again
        $(this).draggable('option','revert','invalid');
    },
};
function colorinit(){

	// red = 1;
	// green = 2;
	// blue = 3;
	// black = 4
	var data_color = [
		[2,4,1,1],
		[3,4,3,1],
		[2,3,2,2],
		[1,4,3,3],
		[1,1,3,1],
		[1,4,2,2],
		[4,4,1,1],
		[1,3,1,3],
		[2,3,3,1],
		[3,3,4,2],
		[3,2,3,3],
		[1,3,4,4],
	];
	createColorEle(data_color);
	
	$('.drop_dice').droppable({
		drop: function(event,ui){
	        var $this = $(this);
	        // Check number of elements already in
	        if($this.find('.color_cont').length >= 1){
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
	$('#dice_wrapper').droppable({
		drop: function(event,ui){
	        var $this = $(this);

	        // Put dragged item into container
	        ui.draggable.appendTo($this).css({
	            top: '0px',
	            left: '0px'
	        });
	    }
	});
	$('#dice_wrapper').on('click','.color_cont',function(){
		rotate_color_box($(this));
	});
	$('#place_dice').on('click','.color_cont',function(){
		rotate_color_box($(this));
		calculateScore();
	});

	function rotate_color_box(box){
		var x = [
			box.find('.top_left_val'),
			box.find('.top_right_val'),
			box.find('.bottom_right_val'),
			box.find('.bottom_left_val')
		];
		var temp = x[0].css('background'),val = x[0].data('val');
		x[0].css('background',x[1].css('background'));
		x[0].data('val',x[1].data('val'));
		x[1].css('background',x[2].css('background'));
		x[1].data('val',x[2].data('val'));
		x[2].css('background',x[3].css('background'));
		x[2].data('val',x[3].data('val'));
		x[3].css('background',temp);
		x[3].data('val',val);
	}
	function createColorEle(d){
		var map = [0,'red','green','blue','purple'];
		var ele="";
		for(var i=0;i<d.length;i++){
				ele += '<div class="color_cont"> <div class="top_left_val" style="background:url(/2016/static/lacuna/img/puzzle/magic/'+map[d[i][0]]+'.png);" data-val="'+d[i][0]+'"></div> <div class="top_right_val" style="background:url(/2016/static/lacuna/img/puzzle/magic/'+map[d[i][1]]+'.png);" data-val="'+d[i][1]+'"></div> <div class="bottom_left_val" style="background:url(/2016/static/lacuna/img/puzzle/magic/'+map[d[i][2]]+'.png);" data-val="'+d[i][2]+'"></div> <div class="bottom_right_val" style="background:url(/2016/static/lacuna/img/puzzle/magic/'+map[d[i][3]]+'.png);" data-val="'+d[i][3]+'"></div> </div>';
		}
		$('#dice_wrapper').html(ele);
		$('.color_cont').draggable(colorOptions);
	}
	function calculateScore(){
		if($('.drop_dice>.color_cont').length==$('.color_cont').length){
			checkSuccess();
		}
	}
	function checkSuccess(){
		var v = [
			[0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0],
		];
		var s = true,a,b;
		$('.drop_dice').each(function(){
	        var $dc = $(this).find('.color_cont');
	        var x = $(this).data('x')*2;
	        var y = $(this).data('y')*2;
        	v[x][y] = $dc.find('.top_left_val').data('val');
        	v[x][y+1] = $dc.find('.top_right_val').data('val');
        	v[x+1][y] = $dc.find('.bottom_left_val').data('val');
        	v[x+1][y+1] = $dc.find('.bottom_right_val').data('val');
	    });
		for(var i=0;i<v.length/2;i++){
			for(var j=0;j<v[i].length/2;j++){
				a = 2*i;
				b= 2*j;
				//check with hor above and left ver
				if(v[a][b]!=0 && ((a!=0 && v[a-1][b]!=0 && (v[a][b] != v[a-1][b] || v[a][b+1] != v[a-1][b+1])) || (b!=0 && v[a][b-1]!=0 && (v[a][b] != v[a][b-1] || v[a+1][b] != v[a+1][b-1])))){
					s = false;
				}
			}
		}
		if(s)
		{
			submit_ans(v,11);
			// alert("you won");
		}
	}
}
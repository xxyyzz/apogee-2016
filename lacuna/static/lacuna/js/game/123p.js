function level5init()
{
	var grid= [
		[3,2,1,3,2,1,3,1,3],
		[1,2,3,3,1,2,2,2,2],
		[3,2,1,2,1,3,1,3,1],
		[3,1,2,2,3,1,1,2,3],
		[2,1,3,1,1,2,3,2,1],
		[2,3,1,3,2,3,1,2,3],
		[1,3,2,2,3,1,2,3,1],
		[1,2,3,1,1,3,3,2,2],
		[3,2,1,3,2,2,1,1,3],
	];
	var row=grid.length,col=grid[0].length;
	var count=0;


	function GenerateGrid()
	{
		var html = '<div class="level5grid abs_center">';
		for(i=0;i<grid.length;++i)
		{
			for(j=0;j<grid[i].length;++j)
			{
				
				html+='<div class="level5box" data-x="'+i+'" data-y="'+j+'">'+grid[i][j]+'</div>';
			}
		}
		html+='</div>';
		$('#level5').html(html);
	}		
	GenerateGrid();
	function CheckSurrounding()
	{
		var box=$('.level5box.sel');
		var x=box.data('x'),y=box.data('y');
		var arr = [
					$('.level5box[data-x="'+x+'"][data-y="'+(y-1)+'"]')[0],
					$('.level5box[data-x="'+(x+1)+'"][data-y="'+y+'"]')[0],
					$('.level5box[data-x="'+x+'"][data-y="'+(y+1)+'"]')[0],
					$('.level5box[data-x="'+(x-1)+'"][data-y="'+y+'"]')[0],
				];
		// console.log(pos,arr);
		for(i=0;i<arr.length;++i)
		{
			if( !($(arr[i]).hasClass('visited')) && (((count+1)%3)==(parseInt($(arr[i]).html()))%3))
			{
				return true;
			}
		}
		return false;
	}
	function CheckMovePossible()
	{
		if(!CheckSurrounding())
		{
			if($('.level5box:not(.visited)')[0]==undefined)
				win();
			else
				lost();
		}
	}

	function CheckIsNeighbor(prev,cur)
	{
		var dx=Math.abs($(prev).data('x') - $(cur).data('x')),  dy=Math.abs($(prev).data('y') - $(cur).data('y'));
		if((dx==1 && dy==0) || (dx==0 && dy==1))
		{
			$(prev).removeClass('sel');
			$(cur).addClass('visited sel');
			CheckMovePossible();
		}
		else
		{
			--count;
			alert('not neightbor');
		}	
	}

	$('.level5box').click(function(){
		++count;
		// console.log(count);
		if((count%3) == (parseInt($(this).html())%3) &&  !($(this).hasClass('visited'))  )
		{
			if(count>1)
				CheckIsNeighbor($('.level5box.sel')[0],this);
			else
			{
				$('.level5box.sel').removeClass('sel');
				$(this).addClass('visited sel');
			}
		}
		else
		{
			alert('can only click in order 1..2...3 or it is already selected');
			--count;
		}	
	});

	function  lost()
	{
		alert('You lost. Try Again!');
		level5init();
	}
	function win()
	{
		if(count==row*col)
			submit_ans('win',9);
			alert('win');
	}

}
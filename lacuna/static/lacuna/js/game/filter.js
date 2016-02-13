function lvl1init()
{
	var saogridinit = 	[2,1,0,1,1,1,1,2,2];
				    //0-blank 1-red 2-blue [index - color]
				    // [0 - 2] [1 - 1] [2 - 2]
				    // [3 - 2] [4 - 0] [5 - 1]
				    // [6 - 2] [7 - 1] [8 - 1]

	var change = [
					[0,1,3],
					[0,1,2,],
					[1,2,5],
					[0,3,6],
					[1,3,4,5,7],
					[2,5,8],
					[3,6,7],
					[6,7,8],
					[7,8,5],
				 ];
	var win = null;	
	lvl=$('#level1');
	function randomizeinit()
	{
		t=Math.floor(Math.random()*3);
		for(var i =0;i<=t;++i)
		{
			k= Math.floor(Math.random()*9);
			for(var j=0;j<change[k].length;++j)
			{
				switch(saogridinit[change[k][j]])
				{
					case 0 : saogridinit[change[k][j]]=1;
								break;
					case 1 : saogridinit[change[k][j]]=2;
								break;
					case 2 : saogridinit[change[k][j]]=0;
								break;
				}
			}
		}
		init();
	};
	randomizeinit();

	function init()
	{
		lvl.html("");
		ht=Math.floor((lvl.height())/3.04);
		wt=Math.floor((lvl.width())/3.04);
		var color = 'box';
		for(var i=0;i<9;++i)
		{
			
			if(saogridinit[i]==1)
			{
				color='box red';
			}
			else if(saogridinit[i]==2)
			{
				color='box blue';
			}
			var $div = $("<div>", {class: color});
			$
			lvl.append($div);
			color='box';
		}
	}	
	
	function update(obj)
	{
		var obji = $(obj).index();
		for (i=0;i<change[obji].length;++i)
			{	
				if(saogridinit[change[obji][i]]==0)
				{
					saogridinit[change[obji][i]]=1;
					$(lvl.children()[change[obji][i]]).addClass('red');

				}
				else if(saogridinit[change[obji][i]]==1)
				{
					saogridinit[change[obji][i]]=2;	
					$(lvl.children()[change[obji][i]]).attr('class','box blue');
				}
				else if(saogridinit[change[obji][i]]==2)
				{
					saogridinit[change[obji][i]]=0;
					$(lvl.children()[change[obji][i]]).removeClass('blue');	
				}
			}
		check();
	};
	function check()
	{
		win = 1;
		for(var i =0;i<saogridinit.length;++i)
		{

			if(saogridinit[i]!=0)
				{
					win =0;
					break;
				}	

		}
		if(win)
		{
			submit_ans(saogridinit,3);
			alert('you win');
		}

		return false;
	}
	$('.box').on('click',function(){update(this)}); 

};
lvl1init();

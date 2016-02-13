var win_w=$('body').width(),win_h=$('body').height();
function level4init()
{
	// console.log('hi');
	//7-finish, starts a bottom-left,0 is  empty  space
	var grid= [
				[4,1,5,6,2,6,'fin'],	
				[1,6,4,3,0,2,4],
				[2,5,2,4,1,0,1],
				[1,4,1,6,4,1,5],
				[3,3,2,2,3,6,2],
				[1,2,1,6,5,4,6],
				[4,3,2,5,2,1,3],
			];

		// var grid=[
		// 			[4,1,3,3,5,2],	
		// 			[3,4,1,2,'fin',3],	
		// 			[5,1,5,5,4,2],	
		// 			[1,3,2,5,2,1],	
		// 			[6,2,4,1,5,4],	
		// 			[6,2,1,6,6,3],	
		// 		];
	//
	var row=grid.length,col=grid[0].length;
	var dirmap = [
				{
					dir:'n',
					num:null,
					div_data : '<div data-index="0" class="n hor_center">|</div>',
					allow:true,
					dc:-col,
				},
				{
					dir:'ne',
					num:null,
					div_data : '<div data-index="1" class="n e">|</div>',
					allow:true,
					dc: -col + 1,
				},
				{
					dir:'e',
					num:null,
					div_data : '<div data-index="2" class="e ver_center">|</div>',
					allow:true,
					dc: +1,
				},
				{
					dir:'se',
					num:null,
					div_data : '<div data-index="3" class="s e">|</div>',
					allow:true,
					dc: col + 1,
				},
				{
					dir:'s',
					num:null,
					div_data : '<div data-index="4" class="s hor_center">|</div>',
					allow:true,
					dc: col,
				},
				{
					dir:'sw',
					num:null,
					div_data : '<div data-index="5" class="s w">|</div>',
					allow:true,
					dc: col - 1,
				},
				{
					dir:'w',
					num:null,
					div_data : '<div data-index="6" class="w ver_center">|</div>',
					allow:true,
					dc: -1,
				},
				{
					dir:'nw',
					num:null,
					div_data : '<div data-index="7" class="n w">|</div>',
					allow:true,
					dc: -col - 1,
				},
			];	

	function generategrid()
	{
		var html = '<div class="level4grid abs_center">';
		for(i=0;i<grid.length;++i)
		{
			for(j=0;j<grid[i].length;++j)
			{
				
				if(grid[i][j]==0)
				{
					html+='<div class="level4box nocolor" data-x="'+i+'" data-y="'+j+'"><div class="valcont" data-val="'+grid[i][j]+'" style="background:url(/2016/static/lacuna/img/puzzle/white/w'+grid[i][j]+'.svg);"></div></div>';
				}
				else if(grid[i][j]=='fin')
				{
					html+='<div class="level4box fin" data-x="'+i+'" data-y="'+j+'"><div class="valcont" data-val="'+grid[i][j]+'" style="background:url(/2016/static/lacuna/img/puzzle/white/w'+grid[i][j]+'.svg);"></div></div>';	
				}
				else if((i==(row - 1) && j==0))
				{
					html+='<div class="level4box sel" data-x="'+i+'" data-y="'+j+'"><div class="valcont" data-val="'+grid[i][j]+'" style="background:url(/2016/static/lacuna/img/puzzle/red/r'+grid[i][j]+'.svg);"></div></div>';	
				}
				else
				{
					html+='<div class="level4box" data-x="'+i+'" data-y="'+j+'"><div class="valcont" data-val="'+grid[i][j]+'" style="background:url(/2016/static/lacuna/img/puzzle/white/w'+grid[i][j]+'.svg);"></div></div>';

				}
			}
		}
		html+='</div>';
		$('#level4').html(html);
		var initbox = ((row - 1) * col) + 1;
		// $('.level4box:nth-child('+initbox+')').trigger("click");
		setTimeout(function(){
			$('.level4grid').css({height:row*70,width:col*70});
			$('.level4box:nth-child('+initbox+')>.valcont').trigger("click");
		},200);
		
	}		
	generategrid();

	

	function showdir(t)
	{
		var flag=0; //not found
		var x=$(t).data('x'),y=$(t).data('y'),val=parseInt($(t).find('.valcont').data('val'));

		function getalloweddir()
		{
			for(i=0;i<dirmap.length;++i)
			{dirmap[i].allow=true;}

			if(x==0)
			{dirmap[0].allow=false;dirmap[1].allow=false;dirmap[7].allow=false;}
			else if(x==(row - 1))
			{dirmap[3].allow=false;dirmap[4].allow=false;dirmap[5].allow=false;}	

			if(y==0)
			{dirmap[5].allow=false;dirmap[6].allow=false;dirmap[7].allow=false;}
			else if(y==(col - 1))
			{dirmap[1].allow=false;dirmap[2].allow=false;dirmap[3].allow=false;}	

			// for(i=0;i<dirmap.length;++i)
			// {console.log(dirmap[i].dir,dirmap[i].allow)}
		}

		// console.log(x,y,val);
		getalloweddir();
		var dir_box = '<div class="dir_box">';
		// $(t).append('<div class="dir_box"><div  class="w ver_center">|</div></div>');
		for(i=0;i<dirmap.length;++i)
		{
			if(dirmap[i].num==val) 
			{	
				flag=1;
				break;
			} // found
			
		}
		if(flag==1 )
		{
			// console.log(i,dirmap[i].num);
			if(dirmap[i].allow)
			{
				dir_box += dirmap[i].div_data + '</div>';
				$(t).append(dir_box);
				$('.level4box.sel .dir_box>div').trigger("click");
			}
			else
				lost();
		}
		else
		{
			var count=0;
			for(j=0;j<dirmap.length;++j)
			{
				if(dirmap[j].allow && dirmap[j].num==null)
				{dir_box += dirmap[j].div_data;++count;}
			}
			dir_box += '</div>';
			$(t).append(dir_box);
			if(count==1)
				$('.level4box.sel .dir_box>div').trigger("click");
		}	
	}

	$('.level4box').on("click",'.dir_box>div',function(){
		// console.log('yo',this);
		t=$(this).parent().parent();
		// var x=$(t).data('x'),y=$(t).data('y'),val=parseInt($(t).find('.valcont').html());
		// console.log($(t).index(),dirmap[$(this).data('index')].dc,parseInt($(t).find('.valcont').html()));
		$(this).siblings().hide();
		// console.log($(this).siblings());
		var $box = $(t).find('.valcont');
		dirmap[$(this).data('index')].num = parseInt($box.data('val')) ;
		$(t).addClass('visited').removeClass('sel');
		$box.css('background','url(/2016/static/lacuna/img/puzzle/blue/b'+$box.data("val")+'.svg)');

		var initbox = ($(t).index() + 1) + dirmap[$(this).data('index')].dc;
		// console.log(initbox);
		
		
		if($('.level4box:nth-child('+initbox+')').hasClass('visited') || (parseInt($('.level4box:nth-child('+initbox+') .valcont').data("val")) ==0))
			lost();
		else{
			$('.level4box:nth-child('+initbox+')').addClass('sel');
			var $box = $('.level4box:nth-child('+initbox+')').find('.valcont');
			$box.css('background','url(/2016/static/lacuna/img/puzzle/red/r'+$box.data("val")+'.svg)');
			$('.level4box:nth-child('+initbox+')>.valcont').trigger("click");
		}

		
	});

	$('.level4box>.valcont').click(function(){
		if($(this).parent().hasClass('sel'))
		{
			if( grid[$(this).parent().data('x')][$(this).parent().data('y')]=='fin' )
				win();
			else
				showdir($(this).parent());
		}
		else
			alert('You can only choose direction for selected class.');
	});
	
	function lost()
	{
		alert('lost');
	}
	function win()
	{
		console.log(dirmap);
		submit_ans(,5);
		alert('win');
	}
}
function qrcodeinit()
{
	var game=[];

	for (i=0;i<21;i++) {
		game[i] = [];
		for (j=0;j<21;j++) {
			game[i][j]=Math.floor(Math.random() * 2);
		}
	}

	var items="";
	for (i=0;i<21;++i) {
		for (j=0;j<21;++j) {
			if (game[i][j]==0) {
				var col='white';
			}
			else {
				var col='black'
			}
			items = items+'<div class="item '+col+'"></div>';
		}
	};
	// console.log(items);
		$('.cont').html(items);

	$('.item').click(function(){
		var x=parseInt($(this).index()/21);
		var y=$(this).index()%21;
		if ($(this).hasClass("white")==1) {
			$(this).removeClass('white').addClass('black');
			game[x][y]=1;
		}
		else {
			$(this).removeClass('black').addClass('white');
			game[x][y]=0;
		}
	});
	$('#qrsubmit').click(function(){
		var tp1 = $('#qrinput').val();
		var tp2 = tp1.toLowerCase();
		var tp3 = tp2.replace(/ /g, '');
		submit_ans(tp3,2);
	});
};
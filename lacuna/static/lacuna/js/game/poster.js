function posterinit(){
	$('#poster_submit').click(function(){
		var tp=$('#poster_input').val();
		submit_ans(tp,10);
	});
}
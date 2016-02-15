function redfortinit(){
	$('#rfort_submit').click(function(){
		var tp=$('#rfort_input').val();
		var x = tp.split(",");
		x[0]=parseFloat(x[0]).toFixed(2);
		x[1]=parseFloat(x[1]).toFixed(2);
		tp=x[0]+","+x[1];
		submit_ans(tp,6);
	});
}
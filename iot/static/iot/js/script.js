var obj;
var curr;
var prev=0;
var divHeight;

$(document).ready(function()
{
	$('.content').each(function(){
		divHeight=$(this).height();
		$(this).css("top",-divHeight + "px");
	});
	$("#head0").css("background-color","gray");

	$("#hideToggle").delay(500).fadeIn(500);
});
window.onresize= function(){
	$('.content').each(function(){
		divHeight=$(this).height();
		$(this).css("top",-divHeight + "px");
	});
	if(prev!=0)
		$('#content' + curr).css("top","0px");
}
function headexp() {
	$("#hideToggle").fadeOut(600);
	$("#head" + prev).css("background-color", "");
	var z=$("#description" + curr).css("background-color")
	$("#head" + curr).css("background-color",z)
	if(prev!=curr)
	{
		divHeight = $('#content' + prev).height();
		$('#content' + prev).animate({top: -divHeight + "px"}, 300);
		obj=$('#content' + curr);
		obj.css('display','block');
		obj.animate({top: "0px"}, 500);
		obj.animate({top: "-20px"}, 100);
		obj.animate({top: "0px"}, 100);
	}
	prev=curr;
}
function home() {
	obj.animate({top: -obj.height() + "px"}, 300);
	$("#head" + prev).css("background-color", "");
	$("#head0").css("background-color","gray");
	prev=0;
	$("#hideToggle").fadeIn(600);
}


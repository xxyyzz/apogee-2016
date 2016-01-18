// ------------------------MAP INIT + SELF FUNCTION-----------------------------
var mapinit,win_h = $('body').height(),win_w=$('body').width();
function mapstart() {
	var beforePan,svg_w=16;svg_h=9,initzoom=1.5;

	beforePan = function(oldPan, newPan){
		var stopHorizontal = false
		, stopVertical = false
		, gutterWidth = win_w
		, gutterHeight = win_h
		  // Computed variables
		  , sizes = this.getSizes()
		  , leftLimit = -((sizes.viewBox.x + sizes.viewBox.width) * sizes.realZoom) + gutterWidth
		  , rightLimit = sizes.width - gutterWidth - (sizes.viewBox.x * sizes.realZoom)
		  , topLimit = -((sizes.viewBox.y + sizes.viewBox.height) * sizes.realZoom) + gutterHeight
		  , bottomLimit = sizes.height - gutterHeight - (sizes.viewBox.y * sizes.realZoom)

		  customPan = {}
		  customPan.x = Math.max(leftLimit, Math.min(rightLimit, newPan.x))
		  customPan.y = Math.max(topLimit, Math.min(bottomLimit, newPan.y))

		  return customPan
		}
		onZoom = function(){
			$('#zoomslid').val(parseFloat(mapinit.getZoom()));
		}


		mapinit = svgPanZoom(document.getElementById('map'), {
			viewportSelector: '.svg-pan-zoom_viewport',
			panEnabled: true,
			controlIconsEnabled: false,
			zoomEnabled: true,
			dblClickZoomEnabled: false,
			mouseWheelZoomEnabled: true,
			preventMouseEventsDefault: true,
			zoomScaleSensitivity: 0.2,
			minZoom: 1.2,
			maxZoom: 6,
			fit: false,
			contain: true,
			center: true,
			refreshRate: 'auto',
			beforeZoom: function(){},
			onZoom: onZoom,
			beforePan: beforePan,
			onPan: function(){},
	  // customEventsHandler: {},
	  eventsListenerElement: null,
	});
	// mapinit.zoomAtPointBy(1.3, {x: 5000, y: 500});
	// mapinit.zoomAtPointBy(1.3, {x: 5000, y: 500});
	// mapinit.zoomAtPointBy(1.3, {x: 5000, y: 500});
	$('#zoomslid').val('2.2');
	zoom_slider(2.2);
	mapinit.panBy({x: -(win_w/2)-200, y: -(win_h/2)-100 });
	// mapinit.zoomAtPointBy(2, {x: (win_w/2), y: (win_h/2)});
	// panZoom.setBeforePan(beforePan)
};
mapstart();
function zoom_pan_reset()
{
	// mapinit.resetZoom();
	// mapinit.zoomAtPointBy(1.3, {x: 5000, y: 500});
	// mapinit.zoomAtPointBy(1.3, {x: 5000, y: 500});
	// mapinit.zoomAtPointBy(1.3, {x: 5000, y: 500});
	$('#zoomslid').val('2.2');
	zoom_slider(2.2);
	mapinit.resetPan();
	mapinit.panBy({x: -(win_w/2)-200, y: -(win_h/2)-100 });
}

function zoom_slider(v) {
	mapinit.zoom(v);
}
var zoomtrig=null;
function zoom_trig(t)
{ 
	var z=$('#zoomslid').val();
	$('#zoomslid').val(parseFloat(z) + parseFloat(t));
	zoom_slider((parseFloat(z) + parseFloat(t)));
	zoomtrig = setInterval(
		function(){var z=$('#zoomslid').val();
		$('#zoomslid').val(parseFloat(z) + parseFloat(t));
		zoom_slider((parseFloat(z) + parseFloat(t)));
	},200);
}
function zoom_stop()
{
	clearInterval(zoomtrig);
}

var pantrig=null;
function pan_trig(xin,yin)
{
	mapinit.panBy({x: xin, y: yin});
	pantrig = setInterval(function(){mapinit.panBy({x: xin, y: yin});},200);;
}
function pan_stop()
{
	clearInterval(pantrig);
}

// -------------------------BUILDING Hover-------------------------------------
$(function() {
	var moveLeft = 10;
	var moveDown = -50;
	$('.blah').hover(function(e) {
		$('#building_info>div').html($(this).data('name'));
		$('#building_info').fadeIn(100).css('top', e.pageY + moveDown).css('left', e.pageX + moveLeft);
	}, function() {
		$('#building_info>div').html('');
		$('#building_info').fadeOut(100);
	});

	$('.blah').mousemove(function(e) {
		$("#building_info").css('top', e.pageY + moveDown).css('left', e.pageX + moveLeft);
	});
});

// ------------------------MENU-------------------------------------------
var sideOpen = 0;

$('#overlay').click(function(){
	killOverlay();
	if(sideOpen == 1) {
		$('nav').animate({left:"-370px"},300,"linear");
		sideOpen = 0;
	}
});

$("#burgernav").click(function(){
	$('nav').animate({left:"0px"},300,"linear");
	fireOverlay();
	sideOpen = 1;
});

$(".closeside").click(function() {
	$('nav').animate({left:"-370px"},300,"linear");
	killOverlay();
	sideOpen = 0;
});

// ------------------------OVERLAY-------------------------------------------
function fireOverlay() {
	$("#overlay").fadeIn(400);
}

function killOverlay() {
	$("#overlay").fadeOut(400);
}
//--------------------------GET COOKIE------------------------------------
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

//------------------------LOGIN/REGISTER API---------------------------------
$('#login-form').submit(function(e){
	e.preventDefault();
	$('#login-form .error_box').html('').fadeOut();
	$('#submit_l').prop('disabled', true);
	$('#submit_r').prop('disabled', true);
	var login_data = {
						'useremail_l':$('#useremail_l').val(),
						'userpassword_l':$('#userpassword_l').val()
					};
	console.log(login_data);
	$.ajax({
		url:'http://bits-apogee.org/api/login/',
		method:'POST',
        crossDomain: true,
		data:login_data,
		headers : { "X-CSRFToken" : getCookie('csrftoken') },
		datatype: 'jsonp',
		success:function(response){
			console.log(response);	
			if(response.status)
			{

			}	
			else
			{
				$('#login-form .error_box').html(error).fadeIn();
				$('#submit_l').prop('disabled',false);
				$('#submit_r').prop('disabled',false);
			}
		}
	});
});

$('#reg-form').submit(function(e){
	e.preventDefault();
	var error="Incorrect E-mail or Phone number.";
	var test_email = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
	var test_phone = /^([0-9]{10})$/i;

	var reg_data = {
						'name':$('#username_r').val(),
						'college':$('#usercollege_r').val(),
						'phone_one':$('#userphone_r').val(),
						'gender':$('#usergender_r > input:checked').val(),
						'email_id':$('#useremail_r').val(),
					};
	console.log(reg_data);		
	if( (test_email.test(reg_data.email_id)) && (test_phone.test(reg_data.phone_one)) )
	{
		$('#submit_l').prop('disabled', true);
		$('#submit_r').prop('disabled', true);
		$.ajax({
			url:'http://bits-apogee.org/2016/api/register/',
			method:"POST",
			crossDomain: true,
			datatype: 'jsonp',
			data:reg_data,
			headers : { "X-CSRFToken" : Cookie.get('csrftoken') },
			success:function(response){
				console.log(response);		
			}
		});
	}
	else
	{
		$('#reg-form .error_box').html(error).fadeIn();
	}
});
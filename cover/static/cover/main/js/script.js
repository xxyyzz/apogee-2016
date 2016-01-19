// ------------------------MAP INIT + SELF FUNCTION-----------------------------
var mapinit;

var win_h = $('body').height();
var win_w = $('body').width();

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
			minZoom: 1,
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
	$('.struct').hover(function(e) {
		$('#building_info>div').html($(this).data('name'));
		$('#building_info').removeClass('left down_left down_right');
		if(e.pageX > $(window).width()/2){
			if(e.pageY < 150){
				$('#building_info').addClass('down_left');
			}
			else{
				$('#building_info').addClass('left');
			}
		}
		else{
			if(e.pageY < 150){
				$('#building_info').addClass('down_right');
			}
		}
		$('#building_info').css('top', e.pageY).css('left', e.pageX).css('display','block');
	}, function() {
		$('#building_info>div').html('');
		$('#building_info').css('display','none');
	});

	$('.struct').mousemove(function(e) {
		$("#building_info").css('top', e.pageY).css('left', e.pageX);
	});

	$('.struct').mousedown(function(e) {
		$("#building_info").css('display','none');
	});

	$('.struct').mouseup(function(e) {
		$("#building_info").css('display','block');
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

$("div#login").click(function() {
	fireOverlay();
	$("#login-reg-box").delay(200).fadeIn(200);
});


// ------------------------OVERLAY-------------------------------------------
function closeLightBox() {
	$(".light-box").fadeOut(200);
}

function fireOverlay() {
	$("#overlay").fadeIn(400);
}

function killOverlay() {
	closeLightBox();
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
						'username':$('#useremail_l').val(),
						'password':$('#userpassword_l').val()
					};
	// console.log(login_data);
	$.ajax({
		url:'http://bits-apogee.org/2016/api/login/',
		method:'POST',
        crossDomain: true,
		data:login_data,
		headers : { "X-CSRFToken" : getCookie('csrftoken') },
		datatype: 'jsonp',
		success:function(response){
			// console.log(response);
			if(response.status == 1)
			{
				$('#user-sign-cont>div:nth-child(1)>span').html('Hi, '+response.firstname);
				$('div#login').css({'display':'none'});
				killOverlay();
				$('#user-sign-cont').fadeIn();
				$('#view_profile').fadeIn();
				setTimeout(function(){
					$('#view_profile').fadeOut();
				},5000);
			}
			else
				$('#login-form .error_box').html(response.message).fadeIn();
		}
	});
});

$('#reg-form').submit(function(e){
	e.preventDefault();
	$('#reg-form .error_box').html('').fadeOut();
	var error="Incorrect E-mail  or Phone number.";
	var test_email = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
	var test_phone = /^([0-9]{10})$/i;

	var reg_data = {
						'name':$('#username_r').val(),
						'college':$('#usercollege_r').val(),
						'phone_one':$('#userphone_r').val(),
						'gender':$('#usergender_r > input:checked').val(),
						'email_id':$('#useremail_r').val(),
					};
	// console.log(reg_data);
	if( (test_email.test(reg_data.email_id)) && (test_phone.test(reg_data.phone_one)) )
	{
		$('#submit_l').prop('disabled', true);
		$('#submit_r').prop('disabled', true);
		$.ajax({
			url:'http://bits-apogee.org/2016/api/register/',
			method:"POST",
			// crossDomain: true,
			// datatype: 'jsonp',
			data:reg_data,
			headers : { "X-CSRFToken" : getCookie('csrftoken') },
			success:function(response){
				// console.log(response);
				if(response.status == 1)
				{
					$('#reg-form').html(response.message);
				}
				else
				{
					$('#reg-form .error_box').html(response.message).fadeIn();
				}	
				
			}
		});
	}
	else
	{
		$('#reg-form .error_box').html(error).fadeIn();
	}
});


window.onload = function() {

	//startGuide();

	$("#loader").delay(2000).fadeOut(500);

	//TWITTER 
		
	!function(d,s,id){
		var js,fjs=d.getElementsByTagName(s)[0];
		if(!d.getElementById(id)){
			js=d.createElement(s);
			js.id=id;js.src="http://platform.twitter.com/widgets.js";
			fjs.parentNode.insertBefore(js,fjs);
		}
	}(document,"script","twitter-wjs");

	//FACEBOOK 
	(function(d, s, id) {
		var js, fjs = d.getElementsByTagName(s)[0];
		if (d.getElementById(id))
			return;
		js = d.createElement(s);
		js.id = id;
		js.src = "http://connect.facebook.net/en_US/all.js#xfbml=1";
		fjs.parentNode.insertBefore(js, fjs);
	}(document, 'script', 'facebook-jssdk'));
}


// -----------------------------------Online Events---------------------------------------
var events_list,event_data=[];
var cur_cat = 0,cur_event=0;
var keyallow = false;
var disp,lh;

$(window).load(function(){
	disp = $('#event_prev').width();
	lh = parseInt($('.event_cont').css('line-height'));
	summaryGet();
	$('.close_gen_lb').click(function(){
		close_gen_lb();
	});
	$('#close_events').click(function(){
		$('#events').fadeOut();
	});
	$('#event_top').click(function(){
		prev_eve();
	});
	$('#event_bottom').click(function(){
		next_eve();
	});
	$('#event_left').click(function(){
		prev_strip();
	});
	$('#event_right').click(function(){
		next_strip();
	});
	$('.se_descr').on('click','#show_more',function(){
		get_event_detail(events_list[cur_cat].events[cur_event].id,show_all_det);
	});
	$('.se_ico').on('click','.eve_det_ico',function(){
		var x = $(this).data('eve_id'),
		y = $(this).data('eve_pos'),
		z = $(this).data('eve_type');
		$('.se_descr').html(event_data[x].tabs[y][z]);
	});
	$('#searchResults').on('click','.searchResult',function(){
		go_to_location($(this).data('cat'),$(this).data('eve'));
		closeSearch();
	});

});
$(window).keydown(function(e)
{
    var keycode = e.keyCode || e.which;
    switch(keycode)
    {
    	case 37: 
				prev_strip();
				break;
    	case 38: 
				prev_eve();
    			break;
    	case 39:
				next_strip();
    			break;
    	case 40:
				next_eve();
    			break;
    }
});
function open_gen_lb(){
	$('.gen_lb_cont').fadeIn();
}
function close_gen_lb(){
	$('.gen_lb_cont').fadeOut();
}
function next_strip(){
	if(!keyallow || $("#searchField").is(":focus"))
	{
		return;
	}
	keyallow = false;
	$('.show_event').css('background-color','rgba(0,0,0,0)');
	var c = $('#event_right>.strip').css('background-position');
	$('#event_right>.strip').css('background-position',((parseInt(c)-140) + 'px 0'));
	$('#event_left>.strip').css('background-position',c);
	$('#event_prev').css('background-position',((parseInt($('#event_prev').css('background-position')) - disp)+'px 0'));
	cur_cat++;
	if(cur_cat == events_list.length)
		cur_cat = 0;
	$('.se_ico').html('');
	open_category(cur_cat);
	setTimeout(function() {
		keyallow = true;
	}, 600);
}
function prev_strip(){
	if(!keyallow || $("#searchField").is(":focus"))
	{
		return;
	}
	keyallow = false;
	$('.show_event').css('background-color','rgba(0,0,0,0)');
	var c = $('#event_left>.strip').css('background-position');
	$('#event_left>.strip').css('background-position',((parseInt(c)+140) + 'px 0'));
	$('#event_right>.strip').css('background-position',c);
	$('#event_prev').css('background-position',((parseInt($('#event_prev').css('background-position')) + disp)+'px 0'));
	cur_cat--;
	if(cur_cat<0)
		cur_cat = events_list.length - 1;
	$('.se_ico').html('');
	open_category(cur_cat);
	setTimeout(function() {
		keyallow = true;
	}, 550);
}
function next_eve(){
	if(!keyallow || $("#searchField").is(":focus"))
	{
		return;
	}
	keyallow = false;
	$('.show_event').css('background-color','rgba(0,0,0,0.5)');
	$('#event_top>.e_strip').animate({top:(parseInt($('#event_top>.e_strip').css('top')) - lh) + 'px'},500);
	$('#event_bottom>.e_strip').animate({top:(parseInt($('#event_bottom>.e_strip').css('top')) - lh) + 'px'},500);
	$('.show_event>.se_head').animate({'top':'-50px','opacity':0},200);
	$('.show_event>.se_head').css('font-size','1em');
	$('.show_event>.se_descr').animate({'top':'-100px','opacity':0},200);
	$('.se_ico').html('');
	setTimeout(function() {
		cur_event++;
		if(cur_event == events_list[cur_cat].events.length){
			cur_event = 0;
		}
		$('.show_event>.se_head').html(events_list[cur_cat].events[cur_event].name);
		$('.show_event>.se_descr').html('<div class="light_large_font">'+events_list[cur_cat].events[cur_event].short_desc + '</div><div id="show_more">Show More</div>');
		$('.show_event>.se_head').css({'top':'100px'});
		$('.show_event>.se_head').css('opacity','1');
		$('.show_event>.se_head').animate({'top':'0px'},250);
		$('.show_event>.se_head').css('font-size','3em');
		$('.show_event>.se_descr').css('top','200px');
		$('.show_event>.se_descr').animate({'top':'0px','opacity':1},250);
	}, 250);
	setTimeout(function() {
		var tt=parseInt($('#event_top>.e_strip').css('top'))*-1;
		var bt=parseInt($('#event_bottom>.e_strip').css('top'))*-1;
		if(tt > ($('#event_top>.e_strip>.event_cont').length-3)*lh)
		{
			$('#event_top>.e_strip').css('top','-100px');
		}
		if(bt > ($('#event_bottom>.e_strip>.event_cont').length-3)*lh)
		{
			$('#event_bottom>.e_strip').css('top','-100px');
		}
		keyallow = true;
	}, 550);
}
function prev_eve(){
	if(!keyallow || $("#searchField").is(":focus"))
	{
		return;
	}
	keyallow = false;
	$('.show_event').css('background-color','rgba(0,0,0,0.5)');
	$('#event_top>.e_strip').animate({top:(parseInt($('#event_top>.e_strip').css('top')) + lh) + 'px'},500);
	$('#event_bottom>.e_strip').animate({top:(parseInt($('#event_bottom>.e_strip').css('top')) + lh) + 'px'},500);
	$('.show_event>.se_head').animate({'top':'100px','opacity':0},200);
	$('.show_event>.se_head').css('font-size','1em');
	$('.show_event>.se_descr').animate({'top':'200px','opacity':0},200);
	$('.se_ico').html('');
	setTimeout(function() {
		cur_event--;
		if(cur_event < 0){
			cur_event = events_list[cur_cat].events.length - 1;
		}
		$('.show_event>.se_head').html(events_list[cur_cat].events[cur_event].name);
		$('.show_event>.se_descr').html('<div class="light_large_font">'+events_list[cur_cat].events[cur_event].short_desc +'</div><div id="show_more">Show More</div>');
		$('.show_event>.se_head').css({'top':'-50px'});
		$('.show_event>.se_head').css('opacity','1');
		$('.show_event>.se_head').animate({'top':'0px'},250);
		$('.show_event>.se_head').css('font-size','3em');
		$('.show_event>.se_descr').css('top','-100px');
		$('.show_event>.se_descr').animate({'top':'0px','opacity':1},250);
	}, 250);
	setTimeout(function() {
		var tt=parseInt($('#event_top>.e_strip').css('top'))*-1;
		var bt=parseInt($('#event_bottom>.e_strip').css('top'))*-1;
		if(tt == 0)
		{
			$('#event_top>.e_strip').css('top',($('#event_top>.e_strip>.event_cont').length-4)*-lh + 'px');
		}
		if(bt == 0)
		{
			$('#event_bottom>.e_strip').css('top',($('#event_bottom>.e_strip>.event_cont').length-4)*-lh + 'px');
		}
		keyallow =true;
	}, 550);
}
function summaryGet(){
	$.ajax({
		url: "http://bits-apogee.org/2016/events/summary/",
		method: "GET",
		success: function(data){
			events_list = data;
			open_category(cur_cat);
			keyallow = true;
			setUpSearchRandom();
		}
	});
}
function open_category(x){
	var data = events_list[x].events,ele="";
	$('#event_top > .e_strip').fadeOut(250);
	$('#event_bottom > .e_strip').fadeOut(250);
	$('.show_event>.se_head').animate({'top':'100px','opacity':0},200);
	$('.show_event>.se_head').css('font-size','1em');
	$('.show_event>.se_descr').animate({'top':'300px','opacity':0},200);

	ele += '<div class="event_cont">'+data[data.length-2].name+'</div><div class="event_cont">'+data[data.length-1].name+'</div>'
	for(var i=0;i<data.length;i++){
		ele += '<div class="event_cont">'+data[i].name+'</div>';
	}
	ele += '<div class="event_cont">'+data[0].name+'</div><div class="event_cont">'+data[1].name+'</div>';
	setTimeout(function() {
		$('.e_strip').html(ele);
		$('#event_top>.e_strip').css('top',-lh + 'px');
		$('#event_bottom>.e_strip').css('top',(-lh*4) + 'px');
		cur_event = 1;
		$('.e_strip').fadeIn(200);
	}, 300);
}
var icon_map = {
	'Sponsors': 'rupee',
	'FAQs': 'question',
	'Resources': 'link',
	'Rules': 'list',
	'Problem Statements': 'file-text',
	'Specifications': 'gear',
	'Materials': 'wrench',
	'Sample Questions': 'check-square-o',
	'Guidelines': 'info',
	'Registration Details': 'database',
	'Judging Criteria': 'gavel',
	'Eligibility': 'check				',
	'Overview ': 'circle-o',
}
function show_all_det(id){
	var tabs = event_data[id].tabs,ele="";
	for(var x=0;x<tabs.length;x++)
	{
		for(var y in tabs[x]){
			ele +='<div class="eve_det_ico" data-eve_id="'+id+'" data-eve_pos="'+x+'" data-eve_type="'+y+'"><div class="ico_name">'+y+'<div></div></div><i class="fa fa-'+icon_map[y]+'"></i></div>';
		}
	}
	$('.se_ico').html(ele);
	$('.se_ico').fadeIn();
	$('.se_descr').html(event_data[id].tabs[0][$('.se_ico>div').data('eve_type')]);
}
function get_event_detail(id,call_back){
	if(typeof event_data[id] !== 'undefined')
	{
		call_back(id);
		return;
	}
	$.ajax({
		url: "http://bits-apogee.org/2016/events/get_event/"+id+"/",
		method: "GET",
		success: function(data){
			event_data[id] = data;
			call_back(id);
		}
	});
}

//=========================================================SEARCH STARTS================================================
events_search_list = [
	// {
	// 	id:"",
	// 	name:"",
	// 	tags:"",
	// 	category: "",
	// 	short_desc:"",
	// },
];
function generate_eve_search(){
	var ptr=0;
	for(var i=0;i<events_list.length;i++){
		for(var j = 0;j<events_list[i].events.length;j++){
			events_search_list[ptr] = events_list[i].events[j];
			events_search_list[ptr].category = events_list[i].category;
			ptr++;
		}
	}
	event_fuse =new Fuse(events_search_list, eve_options);
}

var eve_options = {	keys: ['name','tags','category'],threshold:0.4};
var event_fuse;
function pos_of_event(cat,name){
	var i=0,j=0;
	while(i<events_list.length){
		if(events_list[i].category == cat)
			break;
		i++;
	}
	while(j<events_list[i].events.length){
		if(events_list[i].events[j].name==name)
			break;
		j++;
	}
	return [i,j];
}
function setUpSearchRandom()
{	
	generate_eve_search();
	$('#open_search').click(function(){
		openSearch();
	});
	$('#iconBack').click(function(){
		closeSearch();
	});

	$("#searchField").keyup(function() {
		var ip = $("#searchField").val();
		if(ip!='')
		{	
			found_events = event_fuse.search(ip);
			$("#searchResults").html('');
			var i = 0;
			while(i !=15 && i<found_events.length)
			{
				var x = pos_of_event(found_events[i]["category"],found_events[i]["name"]);
				$("#searchResults").append('<div class="searchResult" data-cat="'+x[0]+'" data-eve="'+x[1]+'">'+found_events[i]["name"]+'</div>');
				i++;
			}
		}
		else{
			found_events = events_search_list;
			document.getElementById("searchResults").innerHTML = "";
		}
	});
}
function openSearch(){
	$('#search').animate({right:"0px"},220);
	setTimeout(function() {
		$('#searchField').focus();
	}, 250);
}
function closeSearch()
{
	$('#search').animate({right:"-290px"},220);
}
function go_to_location(cat,eve){
	keyallow = false;
	var cur_pos = parseInt($('#event_prev').css('background-position'));
	var t = (cur_pos/disp)%events_list.length;
	if(t<=0){
		t = t*-1;
	}
	else{
		t = 8-t;
	}
	t = t - cat;
	$('#event_prev').css('background-position',((parseInt($('#event_prev').css('background-position')) + (t*disp))+'px 0'));
	
	var c = parseInt($('#event_right>.strip').css('background-position'));
	$('#event_right>.strip').css('background-position',((c+(140*t)) + 'px 0'));
	$('#event_left>.strip').css('background-position',((c+(140*(t+1))) + 'px 0'));

	cur_cat = cat;
	open_category(cur_cat);
	setTimeout(function() {
		if(typeof eve !== 'undefined')
		{
			cur_event = eve;
			var pos_top,pos_bot;
			if(eve==0){
				pos_top = -1*lh*events_list[cur_cat].events.length;
			}
			else{
				pos_top = -1*lh*eve;
			}
			if(eve == events_list[cur_cat].events.length-1)
			{
				pos_bot = -2*lh;
			}
			else{
				pos_bot = -1*lh*(eve+3)
			}
			$('.show_event').css('background-color','rgba(0,0,0,0.5)');
			$('#event_top>.e_strip').animate({top: pos_top+ 'px'},500);
			$('#event_bottom>.e_strip').animate({top: pos_bot + 'px'},500);
			$('.show_event>.se_head').animate({'top':'100px','opacity':0},200);
			$('.show_event>.se_head').css('font-size','1em');
			$('.show_event>.se_descr').animate({'top':'200px','opacity':0},200);
			$('.se_ico').html('');
			setTimeout(function() {
				$('.show_event>.se_head').html(events_list[cur_cat].events[cur_event].name);
				$('.show_event>.se_descr').html('<div class="light_large_font">'+events_list[cur_cat].events[cur_event].short_desc + '</div><div id="show_more">Show More</div>');
				$('.show_event>.se_head').css({'top':'100px'});
				$('.show_event>.se_head').css('opacity','1');
				$('.show_event>.se_head').animate({'top':'0px'},250);
				$('.show_event>.se_head').css('font-size','3em');
				$('.show_event>.se_descr').css('top','200px');
				$('.show_event>.se_descr').animate({'top':'0px','opacity':1},250);
				setTimeout(function() {
					keyallow = true;
				}, 250);
			}, 250);
		}
		else{
			keyallow = true;
		}		
	}, 600);
}
// ##################################search end

// On login true
// str.substr(0,str.indexOf(' ')); //str instead of user.name
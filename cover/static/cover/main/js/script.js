var imgpre='/2016';

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
	close_gen_lb();
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


function open_gen_lb(){
	fireOverlay();
	$('.gen_lb').fadeIn();
}

function close_gen_lb(){
	killOverlay();
	$('.gen_lb').fadeOut();
	$('.main_head').html('');
	$("div.lb_icon>img").attr("src", '');
	$('.lb_descr').html('');
}

function closeLightBox() {
	$(".light-box").fadeOut(200);
}

function fireOverlay() {
	$("#overlay").fadeIn(200);
}

function killOverlay() {
	closeLightBox();
	$("#overlay").fadeOut(200);
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
var user = {};
$(window).load(function(){
	$.ajax({
		url:'http://bits-apogee.org'+imgpre+'/api/user/',
		method:'GET',
        crossDomain: true,
        success:function(response){		
				if(response.status==1)
				{
					$('#user-sign-cont>div:nth-child(1)>span').html('Hi, '+response.firstname);
					$('div#login').css({'display':'none'});
					$('#user-sign-cont').fadeIn();
					// $('#view_profile').fadeIn();
					user = {
							'userid':response.email,
							'firstname':response.firstname,
							'name':response.name,
							'loggedin':response.loggedin,
							'id':response.id,
						   };
					// setTimeout(function(){
					// $('#view_profile').css({'display':''});
					// },3000);
				}	
				else
					startHelp();
				},
		error:function(){
					startHelp();
				},		
	});
});
function logout(){
	$.ajax({
		url:'http://bits-apogee.org'+imgpre+'/api/logout/',
		method:'GET',
        crossDomain: true,
        success:function(response){		
				if(response.status==0)
				{
					user = {
							'userid':undefined,
							'firstname':undefined,
							'loggedin':undefined,
						   };
					$('#user-sign-cont>div:nth-child(1)>span').html('');
					$('div#login').fadeIn();
					$('#user-sign-cont').css('display','');
					eve_reg_info();
				}	
				else
					alert('Unsuccessful. Please Try Again!');
        }
	});
};

$(document).on('submit','#create_a_team',function(e){
	e.preventDefault();
	console.log('hey');
    var formData = $(this).serializeArray();
    $('.create_team').text('Creating ...');
    $('.create_team').prop('disabled', true);
    $.ajax({
		url:'http://bits-apogee.org'+imgpre+'/api/events/team/register/'+events_list[cur_cat].events[cur_event].id+'/',
		method:'POST',
        crossDomain: true,
		data:formData,
		headers : { "X-CSRFToken" : getCookie('csrftoken') },
		datatype: 'jsonp',
		success:function(data){
			if(data.status == 1){
	        	$('.lb_descr').html('Team successfully created.');
	        }
	        else{
	        	$('.lb_descr').html('Some error occured. Plaese Try Again.');
	        }
	        eve_reg_info();
		}
	});
});
$('#login-form').submit(function(e){
	e.preventDefault();
	$('#login-form .error_box').html('').fadeOut();
	$('#submit_l').prop('disabled', true);
	$('#submit_r').prop('disabled', true);
	$('#submit_l').html('logging in...');
	var login_data = {
						'username':$('#useremail_l').val(),
						'password':$('#userpassword_l').val()
					};
	// console.log(login_data);
	$.ajax({
		url:'http://bits-apogee.org'+imgpre+'/api/login/',
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
				user ={
					'userid':$('#useremail_l').val(),
					'firstname':response.firstname,
					'loggedin':true,
				};
				$('#submit_l').prop('disabled', false);
				$('#submit_r').prop('disabled', false);
				$('#submit_l').html('login');
				eve_reg_info();
				setTimeout(function(){
					$('#view_profile').css({'display':''});
				},3000);
			}
			else
				{
					$('#login-form .error_box').html(response.message).fadeIn();
					$('#submit_l').prop('disabled', false);
					$('#submit_r').prop('disabled', false);
					$('#submit_l').html('login');
				}			
		},
		error: function(){
							$('#login-form .error_box').html('Try Again!').fadeIn();
							$('#submit_l').prop('disabled', false);
							$('#submit_r').prop('disabled', false);
							$('#submit_l').html('login');
			},
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
		$('#submit_r').html('Registering...');
		$.ajax({
			url:'http://bits-apogee.org'+imgpre+'/api/register/',
			method:"POST",
			// crossDomain: true,
			// datatype: 'jsonp',
			data:reg_data,
			headers : { "X-CSRFToken" : getCookie('csrftoken') },
			success:function(response){
				// console.log(response);
				if(response.status == 1)
				{
					$('#submit_l').prop('disabled', false);
					$('#submit_r').prop('disabled', false);
					$('#submit_r').html('Register');
					$('#reg-form').html(response.message);
				}
				else
				{
					$('#submit_l').prop('disabled', false);
					$('#submit_r').prop('disabled', false);
					$('#submit_r').html('Register');
					$('#reg-form .error_box').html(response.message).fadeIn();
				}	
			},
			error: function(){
				$('#submit_l').prop('disabled', false);
				$('#submit_r').prop('disabled', false);
				$('#submit_r').html('Register');
				$('#reg-form .error_box').html('Try Again!').fadeIn();
			},
		});
	}
	else
	{
		$('#reg-form .error_box').html(error).fadeIn();
	}
});


window.onload = function() {

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
var keyallow = false,eventpageopen=false;
var disp,lh,show_eve_instr=true;

$(window).load(function(){
	disp = $('#event_prev').width();
	lh = parseInt($('.event_cont').css('line-height'));
	summaryGet();
	$('.close_gen_lb').click(function(){
		close_gen_lb();
	});
	$('#close_events').click(function(){
		eventpageopen=false;
		$('#events').fadeOut();
		$('.show_event').css('background','');
		$('.close_more_det').click();
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
	$('.eve_instrs_close').click(function(){
		$(this).parent().fadeOut();
		show_eve_instr=false;
	});
	$('.se_descr').on('click','#show_more',function(){
		get_event_detail(events_list[cur_cat].events[cur_event].id,show_all_det);
	});
	$('.se_descr').on('click','.register_event',function(){
		register_for_event(events_list[cur_cat].events[cur_event].id);
	});
	var wait =0;
	$('.lb_descr').on('keyup','input[name="memberid"]',function(){
		wait++;
		var t =$(this);
		if(wait==1){
			setTimeout(function() {
				create_my_team(t.val(),t.parent().find('.name_mem'));
				wait = 0;
			}, 500);
		}
	});
	$('.se_descr').on('click','.open_create',function(){
		var obj = events_list[cur_cat].events[cur_event];
		var put_it = $('.lb_descr');
		var eve = "";
		$('.main_head').html(obj.name);
		eve += ' <form id="create_a_team"><div>Team Name <input type="text" name="name" required/></div><div><div class="mem_id_label">Leader ID</div> <input type="text" readonly="readonly" name="memberid" value="'+user.id+'" /><span class="name_mem" style="color:rgb(25, 188, 25)">'+user.name+'</span> </div>';
		for(var i=1;i<obj.max_members;i++){
			eve += '<div><div class="mem_id_label">Member'+i+' ID</div> <input type="text" name="memberid" /><span class="name_mem"></span> </div>';
		}
		eve += '<button type="submit" class="create_team" >Create</button></form>';
		put_it.html(eve);
		$('.lb_icon>img').attr('src',imgpre+'/static/cover/main/img/lb-icons/about.svg');
		open_gen_lb();
	});
	$('.se_ico').on('click','.eve_det_ico',function(){
		var x = $(this).data('eve_id'),
		y = $(this).data('eve_pos'),
		z = $(this).data('eve_type');
		$('.se_descr').html(event_data[x].tabs[y][z]);
	});
	$('.se_ico').on('click','.eve_det_ico_register',function(){
		var obj = events_list[cur_cat].events[cur_event];
		var put_it = $('.se_descr');
		if(!obj.reg_enabled)
			put_it.html('Online registration for this event is not active.');
		else if(user.loggedin){
			if(obj.registered){
					put_it.html('You are already registered for this event. To know more visit your profile.');
				}
			else{
				if(obj.team_event){
					put_it.html('This is a team event, you can either create a new team or to join an existing team contact its team leader.<div class="open_create">Create Team</div>'); 
				}
				else{
					put_it.html('Registrations for this event are open.<div class="register_event">Register</div>');
				}	
			}
		}
		else
			put_it.html('Registrations for this event is open. Please login to register in this event');
	});
	$('.close_more_det').click(function(){
		$(this).fadeOut();
		$('.se_ico').html('');
		$('.se_descr').html('<div class="light_large_font">'+events_list[cur_cat].events[cur_event].short_desc + '</div><div class="buttons_center"><div id="show_more">More</div></div>');
	});
	$('#searchResults').on('click','.searchResult',function(){
		go_to_location($(this).data('cat'),$(this).data('eve'));
		closeSearch();
	});

});
var mapkeydown=false;
$(window).keydown(function(e)
{
    var keycode = e.keyCode || e.which;
    // console.log(keycode);
    if(eventpageopen)
    {
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
    }
    else
    {	
    	if(!mapkeydown)
    	{
        	mapkeydown=true;
	    	switch(keycode)
	        {
	        	case 37: 
	    				pan_trig(50,0);
	    				break;
	        	case 38: 
	    				pan_trig(0,50);
	        			break;
	        	case 39:
	    				pan_trig(-50,0);
	        			break;
	        	case 40:
	    				pan_trig(0,-50);
	        			break;
	        	case 219 : zoom_trig(-0.2);
	        				break;
	        	case 221 : zoom_trig(0.2);
	        				break;		        			
	        }
	    }    
    }
});
$(window).keyup(function(e)
{
	if(!eventpageopen)
	{
		mapkeydown=false;
		pan_stop();
		zoom_stop();
	}	
});


function next_strip(){
	if(!keyallow || $("#searchField").is(":focus"))
	{
		return;
	}
	keyallow = false;
	$('.eve_instrs_close').click();
	$('.cat_name').css('bottom','');
	$('.show_event').css('background-color','rgba(0,0,0,0)');
	var c = $('#event_right>.strip').css('background-position');
	$('#event_right>.strip').css('background-position',((parseInt(c)-140) + 'px 0'));
	$('#event_left>.strip').css('background-position',c);
	$('#event_prev').css('background-position',((parseInt($('#event_prev').css('background-position')) - disp)+'px 0'));
	cur_cat++;
	if(cur_cat == events_list.length)
		cur_cat = 0;
	$('.se_ico').html('');
	$('.close_more_det').css('display','none');
	open_category(cur_cat);
	setTimeout(function() {
		keyallow = true;
		$('.cat_name').html(events_list[cur_cat].category);
		$('.cat_name').css('bottom','0px');
	}, 600);
}
function prev_strip(){
	if(!keyallow || $("#searchField").is(":focus"))
	{
		return;
	}
	keyallow = false;
	$('.eve_instrs_close').click();
	$('.cat_name').css('bottom','');
	$('.show_event').css('background-color','rgba(0,0,0,0)');
	var c = $('#event_left>.strip').css('background-position');
	$('#event_left>.strip').css('background-position',((parseInt(c)+140) + 'px 0'));
	$('#event_right>.strip').css('background-position',c);
	$('#event_prev').css('background-position',((parseInt($('#event_prev').css('background-position')) + disp)+'px 0'));
	cur_cat--;
	if(cur_cat<0)
		cur_cat = events_list.length - 1;
	$('.se_ico').html('');
	$('.close_more_det').css('display','none');
	open_category(cur_cat);
	setTimeout(function() {
		keyallow = true;
		$('.cat_name').html(events_list[cur_cat].category);
		$('.cat_name').css('bottom','0px');
	}, 600);
}
function next_eve(){
	if(!keyallow || $("#searchField").is(":focus"))
	{
		return;
	}
	keyallow = false;
	$('.eve_instrs_close').click();
	$('.cat_name').css('bottom','');
	$('.show_event').css('background-color','rgba(0,0,0,0.5)');
	$('#event_top>.e_strip').animate({top:(parseInt($('#event_top>.e_strip').css('top')) - lh) + 'px'},500);
	$('#event_bottom>.e_strip').animate({top:(parseInt($('#event_bottom>.e_strip').css('top')) - lh) + 'px'},500);
	$('.show_event>.se_head').animate({'top':'-50px','opacity':0},200);
	$('.show_event>.se_head').css('font-size','1em');
	$('.show_event>.se_descr').animate({'top':'-100px','opacity':0},200);
	$('.se_ico').html('');
	$('.close_more_det').css('display','none');
	setTimeout(function() {
		cur_event++;
		if(cur_event == events_list[cur_cat].events.length){
			cur_event = 0;
		}
		$('.show_event>.se_head').html(events_list[cur_cat].events[cur_event].name);
		$('.show_event>.se_descr').html('<div class="light_large_font">'+events_list[cur_cat].events[cur_event].short_desc + '</div><div class="buttons_center"><div id="show_more">More</div></div>');
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
	$('.eve_instrs_close').click();
	$('.cat_name').css('bottom','');
	$('.show_event').css('background-color','rgba(0,0,0,0.5)');
	$('#event_top>.e_strip').animate({top:(parseInt($('#event_top>.e_strip').css('top')) + lh) + 'px'},500);
	$('#event_bottom>.e_strip').animate({top:(parseInt($('#event_bottom>.e_strip').css('top')) + lh) + 'px'},500);
	$('.show_event>.se_head').animate({'top':'100px','opacity':0},200);
	$('.show_event>.se_head').css('font-size','1em');
	$('.show_event>.se_descr').animate({'top':'200px','opacity':0},200);
	$('.se_ico').html('');
	$('.close_more_det').css('display','none');
	setTimeout(function() {
		cur_event--;
		if(cur_event < 0){
			cur_event = events_list[cur_cat].events.length - 1;
		}
		$('.show_event>.se_head').html(events_list[cur_cat].events[cur_event].name);
		$('.show_event>.se_descr').html('<div class="light_large_font">'+events_list[cur_cat].events[cur_event].short_desc + '</div><div class="buttons_center"><div id="show_more">More</div></div>');
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
		url: 'http://bits-apogee.org'+imgpre+'/events/summary/',
		method: "GET",
		success: function(data){
			events_list = data;
			eve_reg_info();
			open_category(cur_cat);
			keyallow = true;
			setUpSearchRandom();
		}
	});
}
function eve_reg_info(){
	$.ajax({
		url: 'http://bits-apogee.org'+imgpre+'/api/events/status/',
		method: "GET",
		success: function(data){
			for(var i=0;i<data.data.length;i++){
				for(var j=0;j<data.data[i].events.length;j++){
					events_list[i].events[j].reg_enabled = data.data[i].events[j].reg_enabled;
					events_list[i].events[j].registered = data.data[i].events[j].registered;
					events_list[i].events[j].team_event = data.data[i].events[j].team_event;
					events_list[i].events[j].max_members = data.data[i].events[j].max_members;
				}
			}
		}
	});
}

function create_my_team(id,put){
	if(id==""){
		put.html('');
	}
	else{
		$.ajax({
			url: 'http://bits-apogee.org'+imgpre+'/api/participant/'+id+'/',
			method: "GET",
			success: function(data){
				if(data.status==1)
				{
					put.css('color','rgb(25, 188, 25)');
					put.html(data.name);
				}
				else
				{
					put.css('color','rgb(242, 80, 80)');
					put.html(data.message);
				}
			}
		});
	}
}
function register_for_event(id){
	$.ajax({
		url: 'http://bits-apogee.org'+imgpre+'/api/events/register/'+id+'/',
		method: "GET",
		success: function(data){
			$('.se_descr').html(data.message);
			eve_reg_info();
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
	'Register':'pencil',
}
function show_all_det(id){
	var tabs = event_data[id].tabs,ele="";
	for(var x=0;x<tabs.length;x++)
	{
		for(var y in tabs[x]){
			ele +='<div class="eve_det_ico" data-eve_id="'+id+'" data-eve_pos="'+x+'" data-eve_type="'+y+'"><div class="ico_name">'+y+'<div></div></div><i class="fa fa-'+icon_map[y]+'"></i></div>';
		}
	}
	ele +='<div class="eve_det_ico_register"><div class="ico_name">Register<div></div></div><i class="fa fa-pencil"></i></div>';
	$('.se_ico').html(ele);
	$('.se_ico').fadeIn();
	$('.close_more_det').fadeIn();
	$('.se_descr').html(event_data[id].tabs[0][$('.se_ico>div').data('eve_type')]);
}
function get_event_detail(id,call_back){
	if(typeof event_data[id] !== 'undefined')
	{
		call_back(id);
		return;
	}
	$.ajax({
		url: 'http://bits-apogee.org'+imgpre+'/events/get_event/'+id+'/',
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
	$('.cat_name').css('bottom','');
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
			$('.cat_name').css('bottom','');
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
			$('.close_more_det').css('display','none');
			setTimeout(function() {
				$('.show_event>.se_head').html(events_list[cur_cat].events[cur_event].name);
				$('.show_event>.se_descr').html('<div class="light_large_font">'+events_list[cur_cat].events[cur_event].short_desc + '</div><div class="buttons_center"><div id="show_more">More</div></div>');
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
			$('.cat_name').html(events_list[cur_cat].category);
			$('.cat_name').css('bottom','0px');
			keyallow = true;
		}		
	}, 600);
}
// ##################################search end


// variable to monitor help screens.
var onScreen = 0

function startHelp() {
	fireOverlay();
	$("#map-help-1").css("display", "block");
	onScreen = 1;
}

$("#help-button-1,#map-help-1").click(function() {
	$("#map-help-1").css("display", "none");
	$("#map-help-2").css("display", "block");
	$("#map_control").css("z-index", 500);
	$("#burgernav").css("z-index", 500);
	$("div#login").css("z-index", 500);
	onScreen = 2;
});

$("#help-button-2,#map-help-2").click(function() {
	$("#map-help-2").css("display", "none");
	$("#map_control").css("z-index", 1);
	$("#burgernav").css("z-index", 199);
	$("div#login").css("z-index", 199);
	killOverlay();
	onScreen = 0;
});

// To Trigger element on click only and NOT ON DRAG

$("g.struct").on('mousedown', function (evt) {
	var init_x=evt.pageX,init_y=evt.pageY;
	// console.log(init_x,init_y,evt);
  $("g.struct").on('mouseup', function handler(evt) {
 	var fin_x=evt.pageX,fin_y=evt.pageY;
 	// console.log(init_x,fin_x,init_y,fin_y,evt);
    // if ((evt.type === 'mouseup')) {
    if (init_x==fin_x && init_y==fin_y) {

      // click
		var ele_id=$(this).attr("id");
		for(var key in map_ele_info)
		{
			if(key==ele_id)
			{
				map_ele_info[key]['func'](map_ele_info[key]['icon'],map_ele_info[key]['ename'],map_ele_info[key]['content']);
			}
		}
    }
    else
    {
    	// $("g.struct").on('mouseup', function handler(evt) {
    	// 	// console.log(evt);
    	// 	// if((evt.pag))
    	// });
	}
    $("g.struct").off('mouseup mousemove', handler);
  });
});




var map_ele_info = {
	'thinkAgainConclave'	:		{
										ename:'Think Again Conclave',
										content:'<p>The <b>Think Again conclave</b>, the out of the box guest lecture series of APOGEE, has been an integral component of the fest ever since its inception in 2012. Featuring talks by some of the brightest and most creative minds on the planet, the conclave has always inspired the students and attendees to rediscover and refurbish their minds and ambitions, and quite aptly, to “Think Again”. </p><p>The series, over the years, has showcased a vast number of orators who have left the audience in raptures with their sheer brilliance on stage. Walter Lewin, Ryan Woodward, Jeff Lieberman, Mansoor Khan, David J. Peterson and Walter Bender are just some of the many names, who have instilled a sense of novelty in the minds of the audience and added a different dimension to their thinking. The Think Again Conclave was also the proud host of the first ever Ig Nobel Laureates’ Conference.</p><p style="font-size:25px;font-weight:900">Stay tuned while we reveal present year\'s speakers...</p>',
										icon: imgpre+'/static/cover/main/img/lb-icons/thinkAgain.svg',
										func:content_link,
									},
	'dhiti'					:		{
										ename:'Dhiti',
										content:'<p>We have a population of around 1.2 billion and it is just a matter of time, that we will be the nation with the most number of young and technically sound work forces. Technology has grown in many forms and can be made accessible almost to all. It is just a luxury for some but can ease the life of many and can be the key to solving some of the most pressing issues faced by the country today. We just need some ideas and tinkering to apply it on the field.</p><p>It is only by solving such basic problems that development will occur collectively in every community and not selectively. Dhiti(sanskrit for “An idea”) is a platform for passionate individuals who ideate and aspire for technology to reach the grassroots. Here we will provide you with problems and mentors to form feasible solutions to various issues and provide recognition to your solution. So, let’s put our ideas and knowledge bases to some real use.</p><p><b>For more details,contact</b><br><div style="display:inline-block;padding-right:80px">Sameer<br>+91 7728086695</div><div style="display:inline-block;">Vidyasagar Singh<br>+91 8504066462</div></p><br><a class="lb_a" href="/dhiti/" target="_blank"><b><i class="fa fa-external-link"></i>&nbsp;&nbsp;Click here to know more</b></a>',
										icon: imgpre+'/static/cover/main/img/lb-icons/dhiti.svg',
										func:content_link,
									},

	'startupWeekend'		:		{
										ename:'Startup Weekend',
										content:'<p><b>Startup Weekend</b> is a global grassroots movement of active and empowered entrepreneurs driven by the idea of starting up, that connects them to the right people and resources over the  weekend.  It is the largest community of passionate entrepreneurs with over 3000 past events in 150 countries around the world. </p><p>The goal of Startup Weekend is to provide the time, space, knowledge, and resources to help potential entrepreneurs gain the experience they need to start successful ventures. At a Startup Weekend, one gets a 54 hour frenzy of business model creation, coding, designing, and market validation. Coming in alone with an idea on Friday night and leaving on Sunday evening with a startup company, and a bag full of new network contacts is a unique experience only found at a Startup Weekend.</p><p>Startup Weekend  follows a basic model: anyone is welcome to pitch their startup idea and receive feedback from their peers and then exchange of ideas takes place over 54 hours. The weekends culminate with presentations in front of local entrepreneurial leaders who then provide critical appraisal and feedback. </p><br><a class="lb_a" href="http://in.explara.com/e/swpilani" target="_blank"><b><i class="fa fa-external-link"></i>&nbsp;&nbsp;REGISTER HERE</b></a>',
										icon: imgpre+'/static/cover/main/img/lb-icons/startupWeekend.svg',
										func:content_link,
									},

	'help'					:		{
										ename:'Help',
										content:'Help',
										icon:'',
										func:startHelp,
									},

	'iot'					:		{
										ename:'IoT Challenge',
										content:'<p><b>IoT Challenge 2016</b> is a one-of-a-kind platform where participants will get all the required tools from Texas Instruments to give a real form to their creative IoT solutions.</p><p>The uniqueness and beauty of this challenge is that there will not be a particular problem statement. The teams can ideate an IoT solution in any of the facets of human life to make it simpler, easier, more convenient, or more systematic. The teams can explore their minds in a wide range of fields.</p><p>In the preliminary round, teams will have to submit their solution in a detailed written form on the online portal. The teams whose solutions are innovative and feasible will be selected for the final round. They will be provided a toolkit with all the necessary equipments to build a working prototype of their idea over a period of 25 days. The selected teams will present their prototypes at APOGEE-2016 before a panel of expert judges.</p><p>Each member of the winning team will be given TI’s smartwatch. So along with creating your own IoT prototype you can get one created by the maestros! All the teams presenting their solutions in the final round will get certificates from TI and their own to-be IoT device.</p><br><a class="lb_a" href="/iot/" target="_blank"><b><i class="fa fa-external-link"></i>&nbsp;&nbsp;Click here to know more</b></a>',
										icon: imgpre+'/static/cover/main/img/lb-icons/iotc.svg',
										func:content_link,
									},

	'onlineEvents'			:		{
										ename:'Online Events',
										content:'Online Events',
										icon:'',
										func:function(){eventpageopen=true;$('#events').fadeIn();setTimeout(function(){go_to_location(3),350});},
									},

	'automation'			:		{
										ename:'Automation',
										content:'Automation',
										icon:'',
										func:function(){eventpageopen=true;$('#events').fadeIn();setTimeout(function(){go_to_location(2),350});},
									},

	'developAndDiscover'	:		{
										ename:'Develop and Discover',
										content:'Develop and Discover',
										icon:'',
										func:function(){eventpageopen=true;$('#events').fadeIn();setTimeout(function(){go_to_location(5),350});},
									},

	'login'					:		{
										ename:'Login',
										content:'Login',
										icon:'',
										func:function(){if(user.loggedin==true){alert('You are already logged in!')}else{$('div#login').click();}},
									},

	'buildAndDesign'		:		{
										ename:'Build and Design',
										content:'Build and Design',
										icon:'',
										func:function(){eventpageopen=true;$('#events').fadeIn();setTimeout(function(){go_to_location(0),350});},
									},
		
	'youthCon'				:		{
										ename:'Youth Conference',
										content:'<p><b>Leading Endeavour to Achieve Progress (LEAP) </b>is an initiative for all the student run social volunteer organisations across the country. It is an effort of people who feel that the pace of development has become stagnant with the passage of time. In spite of having all the sources and means, most of the organizations stand at the same place where they were ten years ago. LEAP is not just an initiative to improve the efficiency of organizations but also a way through which creative and good ideas can be shared and used for the betterment of the society.</p><p>Numerous student led societies have enough volunteer strength, funds and team dedication, but they fail to create a significant impact. It is thus the need of the hour to have a society joining hands and working together to convert all the whispers into roars. A common platform for like minded volunteer society, connecting them through the will to bring about a change, is what we are working for. It aims to create a larger impact on the society, that are ultimate beneficiaries of actions, they perform.</p><br><a class="lb_a" href="/youthcon/" target="_blank"><b><i class="fa fa-external-link"></i>&nbsp;&nbsp;Click here to know more</b></a>',
										icon: imgpre+'/static/cover/main/img/lb-icons/youthcon.svg',
										func:content_link,
									},

	'codeAndSimulate'		:		{
										ename:'Code and Simulate',
										content:'Code and Simulate',
										icon:'',
										func:function(){eventpageopen=true;$('#events').fadeIn();setTimeout(function(){go_to_location(1),350});},
									},

	'profShow'				:		{
										ename:'ProfShows',
										content:'<div class="c_soon">Coming soon...</div>',
										icon: imgpre+'/static/cover/main/img/lb-icons/profshows.svg',
										func:content_link,
									},

	'economania'			:		{
										ename:'Economania',
										content:'Economania',
										icon:'',
										func:function(){eventpageopen=true;$('#events').fadeIn();setTimeout(function(){go_to_location(4),350});},
									},

	'miscellaneous'			:		{
										ename:'Miscellaneous',
										content:'Miscellaneous',
										icon:'',
										func:function(){eventpageopen=true;$('#events').fadeIn();setTimeout(function(){go_to_location(7),350});},
									},

	'accomodation'			:		{
										ename:'Accommodation',
										content:'<p>All registered participants that come to Pilani will be provided accommodation on the campus.Colleges will share a dormitory style room with a capacity of 25-30 people.Bedding, buckets and extension cords will be provided.The accommodation is free of cost, but a caution deposit of Rs. 200 per participant will be collected which will be refunded at the time of checkout, provided there is no damage to the room, bedding and so on.No issues regarding change of accommodation will be entertained since all the accommodation centers are pre-checked by us.</p><h3>Hospitality :</h3><p>There will be a Hospitality counter open 24 hours at the "Reception & Accommodation" hut, to help you with further queries once you have arrived on campus.A hospitality number will also be provided for all the queries pertaining to the same.</p>',
										icon: imgpre+'/static/cover/main/img/lb-icons/accomodation.svg',
										func:content_link,
									},

	'projects'				:		{
										ename:'Projects',
										content:'',
										icon: imgpre+'/static/cover/main/img/lb-icons/project.svg',
										func:content_link,
									},

	'aic'					:		{
										ename:'APOGEE Innovation Challenge',
										content:'<p><b>APOGEE Innovation Challenge</b>, an exceptional technical symposium, aims at quenching your thirst for hands-on experience in real life problems plaguing the industrial world.</p><p>Organized in collaboration with various multinational companies, this event presents before you existing challenges faced by these companies who seek their solutions from you. These problems, which happen to be discipline specific (one need not belong to that discipline), are to be solved by participants in teams of 2-4 in a month. After scrutiny by company officials, top 5 teams will be presenting their final solutions during APOGEE ‘16.</p><p>Exciting Internship Offers and Cash Prizes await the winners. Needless to say, you can brag about cracking a professional challenge while still being in college. Participation Certificate shall be given to all members of each team which present solutions during APOGEE ‘16.</p><br><a class="lb_a" href="/aic/" target="_blank"><b><i class="fa fa-external-link"></i>&nbsp;&nbsp;Click here to know more</b></a>',
										icon: imgpre+'/static/cover/main/img/lb-icons/aic.svg',
										func:content_link,
									},

	'archives'				:		{
										ename:'Archives',
										content:'<div class="archive_data"><div class="archive-holder"><img src="'+imgpre+'/static/cover/main/img/archive/ap14.jpg" class="arch-img"/><a class="arch-lnk" href="http://bits-apogee.org/2014/" target="_blank"><i class="fa fa-globe"></i>&nbsp;&nbsp;APOGEE 2014</a></div><div class="archive-holder"><img src="'+imgpre+'/static/cover/main/img/archive/ap15i.jpg" class="arch-img"/><a class="arch-lnk" href="http://bits-apogee.org/u/intro" target="_blank"><i class="fa fa-globe"></i>&nbsp;&nbsp;APOGEE 2015 Intro<a></div><div class="archive-holder"><img src="'+imgpre+'/static/cover/main/img/archive/ap15.jpg" class="arch-img"/><a class="arch-lnk" target="_blank" href="http://bits-apogee.org/u/2015"><i class="fa fa-globe"></i>&nbsp;&nbsp;APOGEE 2015 </a></div><div class="archive-holder"><img src="'+imgpre+'/static/cover/main/img/archive/ap16i.jpg" class="arch-img"/><a class="arch-lnk" target="_blank" href="/intro/"><i class="fa fa-globe"></i>&nbsp;&nbsp;APOGEE 2016 Intro</a></div></div>',
										icon: imgpre+'/static/cover/main/img/lb-icons/archives.svg',
										func:content_link,
									},

	'developers'			:		{
										ename:'Developers',
										content:'<div class="dev_data" id="c_data"> <div class="dev_cont"> <div class="dep_name">Frontend Developers</div> <hr class="sep_dep_name"> <div class="devinfo"> <div style="position:relative"><img src="'+imgpre+'/static/cover/main/img/dev/pranjal.jpg" class="contact_img"> </div> <div class="contact_det"><b>Pranjal Gupta</b> <br></div> </div> <div class="devinfo"> <div style="position:relative"><img src="'+imgpre+'/static/cover/main/img/dev/smit.jpg" class="contact_img"> </div> <div class="contact_det"><b>Smit Patwa</b> <br>smit.patwa@gmail.com</div> </div> <div class="devinfo"> <div style="position:relative"><img src="'+imgpre+'/static/cover/main/img/dev/prateek.jpg" class="contact_img"> </div> <div class="contact_det"><b>Prateek Gupta</b> <br>prateek.g1509@gmail.com</div> </div> <div class="devinfo"> <div style="position:relative"><img src="'+imgpre+'/static/cover/main/img/dev/piyush.jpg" class="contact_img"> </div> <div class="contact_det"><b>Piyush Ranjan</b> <br></div> </div> </div> <div class="dev_cont"> <div class="dep_name">Graphic Designers</div> <hr class="sep_dep_name"> <div class="devinfo"> <div style="position:relative"><img src="'+imgpre+'/static/cover/main/img/dev/amey.jpg" class="contact_img"> </div> <div class="contact_det"><b>Amey Agrawal</b> <br></div> </div> <div class="devinfo"> <div style="position:relative"><img src="'+imgpre+'/static/cover/main/img/dev/abhinav.jpg" class="contact_img"> </div> <div class="contact_det"><b>Abhinav Sharma</b> <br></div> </div> <div class="devinfo"> <div style="position:relative"><img src="'+imgpre+'/static/cover/main/img/dev/rishabh.jpg" class="contact_img"> </div> <div class="contact_det"><b>Rishabh Garg</b> <br></div> </div> </div> <div class="dev_cont"> <div class="dep_name">Backend Developers</div> <hr class="sep_dep_name"> <div class="devinfo"> <div style="position:relative"><img src="'+imgpre+'/static/cover/main/img/dev/nikhil.jpg" class="contact_img"> </div> <div class="contact_det"><b>Nikhil Verma</b> <br>nikhilweee@gmail.com</div> </div> <div class="devinfo"> <div style="position:relative"><img src="'+imgpre+'/static/cover/main/img/dev/satwik.jpg" class="contact_img"> </div> <div class="contact_det"><b>Satwik Bhattamishra</b> <br></div> </div> <div class="devinfo"> <div style="position:relative"><img src="'+imgpre+'/static/cover/main/img/dev/kunal.jpg" class="contact_img"> </div> <div class="contact_det"><b>Kunal Sharma</b> <br>ks05111996@gmail.com</div> </div> </div> </div>',
										icon: imgpre+'/static/cover/main/img/lb-icons/developers.svg',
										func:content_link,
									},

	'literaryFest'			:		{
										ename:'Literary Fest',
										content:'<div class="c_soon">Coming soon...</div>',
										icon: imgpre+'/static/cover/main/img/lb-icons/literaryFest.svg',
										func:content_link,
									},

	'armyExhibition'			:	{
										ename:'Army Exhibtion',
										content:'<div class="c_soon">Coming soon...</div>',
										icon: imgpre+'/static/cover/main/img/lb-icons/army.svg',
										func:content_link,
									},

	'campusAmbassador'		:		{
										ename:'Campus Ambassador',
										content:'<span style="font-size:25px"><b>What is a Campus Ambassador ?</b></span><p>A Campus Ambassador is responsible for publicity for APOGEE, the annual technical extravaganza of BITS Pilani, Pilani Campus, and is responsible for introducing and encouraging student participation in the fest, in his/her area or college.</p><p>To APOGEE he/she is the chief student representative of the college and is the coordinator for any relevant activity conducted in his/her college for publicity through social media, College notice boards, Root-mails etc.</p><span style="font-size:25px"><b>Why be a Campus Ambassador ?</b></span><p>Campus Ambassador Program, this time is powered by YOUTH4WORK, an established talent assessment company. A Campus Ambassador will get an official certificate through BITS-Pilani for pursuing a Marketing Internship Programme for 2 months recognized by YOUTH4WORK.</p><p>Moreover, he/she will be entitled to awards and special incentives like exemptions from registration fees, exclusive merchandise, recommendations etc. based on their performance in the programme.</p><br><a class="lb_a" href="http://bits-apogee.org/campusambassador/" target="_blank"><b><i class="fa fa-external-link"></i>&nbsp;&nbsp;Click here to know more</b></a>',
										icon: imgpre+'/static/cover/main/img/lb-icons/campus.svg',
										func:content_link,
									},

	'papers'				:		{
										ename:'Papers',
										content:'',
										icon: imgpre+'/static/cover/main/img/lb-icons/paper.svg',
										func:content_link,
									},

	'sponsors'				:		{
										ename:'Sponsors',
										content:'<div style="text-align:center;"> <div class="spons_row"> <div class="spons_cont"> <a target="_blank" href="http://www.sap.com/india/ms/sap-labs-india.html"> <div class="spons_title">Associate Title</div> <img class="spons_img" src="'+imgpre+'/static/cover/main/img/spons/Sap.jpg"/> </a> </div> <div class="spons_cont"> <a target="_blank" href="http://jarvisindia.net/"> <div class="spons_title">Outreach Workshops Partner</div> <img class="spons_img" src="'+imgpre+'/static/cover/main/img/spons/Jarvis.jpg"/> </a> </div> </div> <div class="spons_row"> <div class="spons_cont"> <a target="_blank" href="http://www.twenty19.com/"> <div class="spons_title">Workshops Partner</div> <img class="spons_img" src="'+imgpre+'/static/cover/main/img/spons/Twenty19.jpg"/> </a> </div> <div class="spons_cont"> <a target="_blank" href="http://authentictechs.com/"> <div class="spons_title">Workshops Partner</div> <img class="spons_img" src="'+imgpre+'/static/cover/main/img/spons/AuthenticTechs.jpg"/> </a> </div> </div> <div class="spons_row"> <div class="spons_cont"> <a target="_blank" href="http://www.youth4work.com/"> <div class="spons_title">Campus Ambassador Partner</div> <img class="spons_img" src="'+imgpre+'/static/cover/main/img/spons/Youth4work.jpg"/> </a> </div> <div class="spons_cont"> <a target="_blank" href="http://www.campusindia.org/"> <div class="spons_title">Media and Youth Outreach Partner</div> <img class="spons_img" src="'+imgpre+'/static/cover/main/img/spons/CampusGuide.jpg"/> </a> </div> </div> <div class="spons_row"> <div class="spons_cont"> <a target="_blank" href="https://www.instamojo.com/"> <div class="spons_title">Payment Partner</div> <img class="spons_img" src="'+imgpre+'/static/cover/main/img/spons/instamojo.jpg"/> </a> </div> <div class="spons_cont" style="display:none;"> <a target="_blank" href="http://techdefence.com/"> <div class="spons_title">Partner</div> <img class="spons_img" src="'+imgpre+'/static/cover/main/img/spons/Techdefence.jpg"/> </a> </div> </div> </div>',
										icon: imgpre+'/static/cover/main/img/lb-icons/spons.svg',
										func:content_link,
									},

	'ceeriExhibition'		:		{
										ename:'CEERI Exhibition',
										content:'<div class="c_soon">Coming soon...</div>',
										icon: imgpre+'/static/cover/main/img/lb-icons/ceeri.svg',
										func:content_link,
									},

	'contactUs'				:		{
										ename:'Contacts',
										content:'<div class="contact_data" id="c_data"><div class="contactinfo"><div class="contact_dept">President</div><div style="position:relative"><img src="'+imgpre+'/static/cover/main/img/contacts/prez.jpg" class="contact_img"><a href="https://www.facebook.com/akhil.reddy.148" target="_blank"><div class="fb_link"><!--?xml version="1.0" ?--><svg class="confb" enable-background="new 0 0 56.693 56.693" height="30px" id="Layer_1" version="1.1" viewBox="0 0 56.693 56.693" width="30px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><style type="text/css">svg .confb{ cursor: pointer;transition: 150ms;transition-timing-function: ease-in-out;-webkit-transition: 150ms;-webkit-transition-timing-function: ease-in-out;fill:#fff;} .confb:hover{ fill: #3b5998;}</style><path d="M40.43,21.739h-7.645v-5.014c0-1.883,1.248-2.322,2.127-2.322c0.877,0,5.395,0,5.395,0V6.125l-7.43-0.029  c-8.248,0-10.125,6.174-10.125,10.125v5.518h-4.77v8.53h4.77c0,10.947,0,24.137,0,24.137h10.033c0,0,0-13.32,0-24.137h6.77  L40.43,21.739z"></path></svg></div></a></div><div class="contact_det"><b>AKHIL REDDY</b><br>+91-7728835792<br>president[at]pilani.bits-pilani.ac.in</div></div><div class="contactinfo"><div class="contact_dept">General Secretary</div><div style="position:relative"><img src="'+imgpre+'/static/cover/main/img/contacts/gen.jpg" class="contact_img"><a href="https://www.facebook.com/rijul.dutta" target="_blank"><div class="fb_link"><!--?xml version="1.0" ?--><svg class="confb" enable-background="new 0 0 56.693 56.693" height="30px" id="Layer_1" version="1.1" viewBox="0 0 56.693 56.693" width="30px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><style type="text/css">svg .confb{ cursor: pointer;transition: 150ms;transition-timing-function: ease-in-out;-webkit-transition: 150ms;-webkit-transition-timing-function: ease-in-out;fill:#fff;} .confb:hover{ fill: #3b5998;}</style><path d="M40.43,21.739h-7.645v-5.014c0-1.883,1.248-2.322,2.127-2.322c0.877,0,5.395,0,5.395,0V6.125l-7.43-0.029  c-8.248,0-10.125,6.174-10.125,10.125v5.518h-4.77v8.53h4.77c0,10.947,0,24.137,0,24.137h10.033c0,0,0-13.32,0-24.137h6.77  L40.43,21.739z"></path></svg></div></a></div><div class="contact_det"><b>RIJUL DUTTA</b><br>+91-8427686647<br>gensec[at]pilani.bits-pilani.ac.in</div></div><div class="contactinfo"><div class="contact_dept">For sponsorship and marketing</div><div style="position:relative"><img src="'+imgpre+'/static/cover/main/img/contacts/spons.jpg" class="contact_img"><a href="https://www.facebook.com/mohammed.motiwala1" target="_blank"><div class="fb_link"><!--?xml version="1.0" ?--><svg class="confb" enable-background="new 0 0 56.693 56.693" height="30px" id="Layer_1" version="1.1" viewBox="0 0 56.693 56.693" width="30px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><style type="text/css">svg .confb{ cursor: pointer;transition: 150ms;transition-timing-function: ease-in-out;-webkit-transition: 150ms;-webkit-transition-timing-function: ease-in-out;fill:#fff;} .confb:hover{ fill: #3b5998;}</style><path d="M40.43,21.739h-7.645v-5.014c0-1.883,1.248-2.322,2.127-2.322c0.877,0,5.395,0,5.395,0V6.125l-7.43-0.029  c-8.248,0-10.125,6.174-10.125,10.125v5.518h-4.77v8.53h4.77c0,10.947,0,24.137,0,24.137h10.033c0,0,0-13.32,0-24.137h6.77  L40.43,21.739z"></path></svg></div></a></div><div class="contact_det"><b>MOHAMMED MOTIWALA</b><br>+91-7728086752<br>sponsorship[at]bits-apogee[dot]org</div></div><div class="contactinfo"><div class="contact_dept">For invites and correspondence</div><div style="position:relative"><img src="'+imgpre+'/static/cover/main/img/contacts/pcr.jpg" class="contact_img"><a href="https://www.facebook.com/profile.php?id=100006361090120" target="_blank"><div class="fb_link"><!--?xml version="1.0" ?--><svg class="confb" enable-background="new 0 0 56.693 56.693" height="30px" id="Layer_1" version="1.1" viewBox="0 0 56.693 56.693" width="30px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><style type="text/css">svg .confb{ cursor: pointer;transition: 150ms;transition-timing-function: ease-in-out;-webkit-transition: 150ms;-webkit-transition-timing-function: ease-in-out;fill:#fff;} .confb:hover{ fill: #3b5998;}</style><path d="M40.43,21.739h-7.645v-5.014c0-1.883,1.248-2.322,2.127-2.322c0.877,0,5.395,0,5.395,0V6.125l-7.43-0.029  c-8.248,0-10.125,6.174-10.125,10.125v5.518h-4.77v8.53h4.77c0,10.947,0,24.137,0,24.137h10.033c0,0,0-13.32,0-24.137h6.77  L40.43,21.739z"></path></svg></div></a></div><div class="contact_det"><b>ADITYA CHAUHAN</b><br>+91-8239822574<br>pcr[at]bits-apogee[dot]org</div></div><div class="contactinfo"><div class="contact_dept">For paper presentations and Guest Lectures</div><div style="position:relative"><img src="'+imgpre+'/static/cover/main/img/contacts/pep.jpg" class="contact_img"><a href="https://www.facebook.com/adivijaykumar" target="_blank"><div class="fb_link"><!--?xml version="1.0" ?--><svg class="confb" enable-background="new 0 0 56.693 56.693" height="30px" id="Layer_1" version="1.1" viewBox="0 0 56.693 56.693" width="30px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><style type="text/css">svg .confb{ cursor: pointer;transition: 150ms;transition-timing-function: ease-in-out;-webkit-transition: 150ms;-webkit-transition-timing-function: ease-in-out;fill:#fff;} .confb:hover{ fill: #3b5998;}</style><path d="M40.43,21.739h-7.645v-5.014c0-1.883,1.248-2.322,2.127-2.322c0.877,0,5.395,0,5.395,0V6.125l-7.43-0.029  c-8.248,0-10.125,6.174-10.125,10.125v5.518h-4.77v8.53h4.77c0,10.947,0,24.137,0,24.137h10.033c0,0,0-13.32,0-24.137h6.77  L40.43,21.739z"></path></svg></div></a></div><div class="contact_det"><b>ADITYA VIJAYKUMAR</b><br>+91-8385857855, +91-8058722661<br>pep[at]bits-apogee[dot]org, guestlectures[at]bits-apogee[dot]org</div></div><div class="contactinfo"><div class="contact_dept">For website and online registration queries</div><div style="position:relative"><img src="'+imgpre+'/static/cover/main/img/contacts/dvm.jpg" class="contact_img"><a href="https://www.facebook.com/pranjalONfb" target="_blank"><div class="fb_link"><!--?xml version="1.0" ?--><svg class="confb" enable-background="new 0 0 56.693 56.693" height="30px" id="Layer_1" version="1.1" viewBox="0 0 56.693 56.693" width="30px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><style type="text/css">svg .confb{ cursor: pointer;transition: 150ms;transition-timing-function: ease-in-out;-webkit-transition: 150ms;-webkit-transition-timing-function: ease-in-out;fill:#fff;} .confb:hover{ fill: #3b5998;}</style><path d="M40.43,21.739h-7.645v-5.014c0-1.883,1.248-2.322,2.127-2.322c0.877,0,5.395,0,5.395,0V6.125l-7.43-0.029  c-8.248,0-10.125,6.174-10.125,10.125v5.518h-4.77v8.53h4.77c0,10.947,0,24.137,0,24.137h10.033c0,0,0-13.32,0-24.137h6.77  L40.43,21.739z"></path></svg></div></a></div><div class="contact_det"><b>PRANJAL GUPTA</b><br>+91-8094076999<br>webmaster[at]bits-apogee[dot]org</div></div><div class="contactinfo"><div class="contact_dept">For projects, events and registration</div><div style="position:relative"><img src="'+imgpre+'/static/cover/main/img/contacts/controls.jpg" class="contact_img"><a href="https://www.facebook.com/falguni.agrawal.965" target="_blank"><div class="fb_link"><!--?xml version="1.0" ?--><svg class="confb" enable-background="new 0 0 56.693 56.693" height="30px" id="Layer_1" version="1.1" viewBox="0 0 56.693 56.693" width="30px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><style type="text/css">svg .confb{ cursor: pointer;transition: 150ms;transition-timing-function: ease-in-out;-webkit-transition: 150ms;-webkit-transition-timing-function: ease-in-out;fill:#fff;} .confb:hover{ fill: #3b5998;}</style><path d="M40.43,21.739h-7.645v-5.014c0-1.883,1.248-2.322,2.127-2.322c0.877,0,5.395,0,5.395,0V6.125l-7.43-0.029  c-8.248,0-10.125,6.174-10.125,10.125v5.518h-4.77v8.53h4.77c0,10.947,0,24.137,0,24.137h10.033c0,0,0-13.32,0-24.137h6.77  L40.43,21.739z"></path></svg></div></a></div><div class="contact_det"><b>FALGUNI AGRAWAL</b><br>+91-9928089204<br>controls[at]bits-apogee[dot]org</div></div><div class="contactinfo"><div class="contact_dept">For Publicity and Online Partnership</div><div style="position:relative"><img src="'+imgpre+'/static/cover/main/img/contacts/adp.jpg" class="contact_img"><a href="https://www.facebook.com/kunal.barapatre.31" target="_blank"><div class="fb_link"><!--?xml version="1.0" ?--><svg class="confb" enable-background="new 0 0 56.693 56.693" height="30px" id="Layer_1" version="1.1" viewBox="0 0 56.693 56.693" width="30px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><style type="text/css">svg .confb{ cursor: pointer;transition: 150ms;transition-timing-function: ease-in-out;-webkit-transition: 150ms;-webkit-transition-timing-function: ease-in-out;fill:#fff;} .confb:hover{ fill: #3b5998;}</style><path d="M40.43,21.739h-7.645v-5.014c0-1.883,1.248-2.322,2.127-2.322c0.877,0,5.395,0,5.395,0V6.125l-7.43-0.029  c-8.248,0-10.125,6.174-10.125,10.125v5.518h-4.77v8.53h4.77c0,10.947,0,24.137,0,24.137h10.033c0,0,0-13.32,0-24.137h6.77  L40.43,21.739z"></path></svg></div></a></div><div class="contact_det"><b>KUNAL BARAPATRE</b><br>+91-7728095594<br>adp[at]bits-apogee[dot]org</div></div><div class="contactinfo"><div class="contact_dept">For reception and accommodation</div><div style="position:relative"><img src="'+imgpre+'/static/cover/main/img/contacts/recnacc.jpg" class="contact_img"><a href="https://www.facebook.com/aditya.gogri" target="_blank"><div class="fb_link"><!--?xml version="1.0" ?--><svg class="confb" enable-background="new 0 0 56.693 56.693" height="30px" id="Layer_1" version="1.1" viewBox="0 0 56.693 56.693" width="30px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><style type="text/css">svg .confb{ cursor: pointer;transition: 150ms;transition-timing-function: ease-in-out;-webkit-transition: 150ms;-webkit-transition-timing-function: ease-in-out;fill:#fff;} .confb:hover{ fill: #3b5998;}</style><path d="M40.43,21.739h-7.645v-5.014c0-1.883,1.248-2.322,2.127-2.322c0.877,0,5.395,0,5.395,0V6.125l-7.43-0.029  c-8.248,0-10.125,6.174-10.125,10.125v5.518h-4.77v8.53h4.77c0,10.947,0,24.137,0,24.137h10.033c0,0,0-13.32,0-24.137h6.77  L40.43,21.739z"></path></svg></div></a></div><div class="contact_det"><b>ADITYA GOGRI</b><br>+91-9772229698<br>recnacc[at]bits-apogee[dot]org</div></div></div>',
										icon: imgpre+'/static/cover/main/img/lb-icons/contacts.svg',
										func:content_link,
									},

	'howToReach'			:		{
										ename:'Reach 333031',
										content:'<div id="google-map"></div> <h3>Travelling by car/taxi from Delhi</h3> <p>There are four routes to get here, distance is 200 or 220 km depending on route taken and time taken is about 4.5 hours. In preferential order the routes are: Delhi-Jhajjar- Charkhi Dadri-Loharu-Pilani,Delhi-Gurgaon-Dharuheda-Rewari-MahendraGarh- Loharu-Pilani, Delhi-Gurgaon-Dharuheda-Rewari-Narnaul-Singhana-Chirawa- Pilani,Delhi-Rohtak-Bhiwani-Loharu-Pilani.</p> <h3>Travelling by bus from Delhi</h3> <p>In case you prefer to travel by public transport, you need to catch a bus at the Inter State Bus Terminal (ISBT), Kashmiri Gate, Delhi. There are frequent buses to Pilani from Delhi from around 4:55 AM to 10:00 PM by Haryana Roadways and Rajasthan Roadways. Contacts: Haryana Roadways (ISBT, Delhi) – 011 23861262 (Loharu) – 01252 258207, Rajasthan Roadways (ISBT, Delhi) – 011 23864470, 011 23864417 (Pilani) – 01596 242263.</p> <h3>Travelling by train from Delhi</h3> <p>There are three trains which run daily from Sarai Rohilla Railway Station (Delhi) to Loharu, which is only 24 km from Pilani. All of them are express trains and take 3 hours to reach Loharu, from where a bus/taxi can be taken for a 40 min journey to Pilani. <img src="'+imgpre+'/static/cover/main/img/howToReach.jpg" style="width: 90%"> </p> <h3>Travelling by car/taxi from Jaipur</h3> <p>There are three routes to get here, distance is 209 or 214 km depending on the route taken and time taken is about 4 hours. In preferential order, the routes are: Jaipur-Reengus-Khandela-Jhunjhunu-Pilani,Jaipur-Reengus-Sikar-Nawalgarh-Jhunjhunu-Pilani,Jaipur-Reengus-Chala-Khetri-Chirawa-Pilani.</p> <h3>Travelling by bus from Jaipur</h3> <p>In case you prefer to travel by public transport, you need to catch a bus from the State Bus Terminal (Sindhi Camp), Jaipur. There are frequent buses to Pilani starting from Jaipur from around 4:00 AM till mid-night. Contacts: Rajasthan Roadways (Sindhi Camp, Jaipur) – 0141 2207914, (Pilani) – 01596 242263. Private buses also ply on this route: Vijay Travels – 01596 220321.</p> <h3>Travelling by train from Jaipur</h3> <p>Jaipur – Loharu section is undergoing gauge conversion and no direct trains are currently available from Jaipur to Loharu or Chirawa.</p> <script type="text/javascript">function initMap() {var myLatLng = {lat: 28.364, lng: 75.587};var map = new google.maps.Map(document.getElementById("google-map"), {center: myLatLng,scrollwheel: true,zoom: 15});var image ="'+imgpre+'/static/cover/main/img/marker.png";marker = new google.maps.Marker({ position: new google.maps.LatLng(28.364, 75.5871271),map: map ,icon: image });}setTimeout(function() {initMap()	}, 1000);</script>', 
										icon: imgpre+'/static/cover/main/img/lb-icons/map.svg',
										func:content_link,
									},

	'about'					:		{
										ename:'About',
										content:'<p>In the heart of Pilani lies a fest that pushes the boundaries of student performance and creativity every year. From presenting papers and projects, to bringing into reality imaginative designs that the student mind conjures up, to the events that enthrall everyone who attends, APOGEE, BITS Pilani\'s technical fest, has always brought together the brightest minds in technology and engineering over the years, and this year, it promises to be bigger than ever.</p><p>Ever dreamed about establishing civilization in Mars? Ever imagined building exciting vehicles and robots with your own hands? Ever wanted to challenge your mind with mind-bending quizzes, word games, and programming challenges? In the final days of February, APOGEE 2016 returns, with a plethora of classics, and many innovative new events.</p><p>From the town of Pilani, BITS Pilani welcomes you to <b>APOGEE 2016</b>. <br><br><span style="font-weight:900;font-size: 30px">The Future is Now !</span></p>',
										icon: imgpre+'/static/cover/main/img/lb-icons/about.svg',
										func:content_link,
									},

	'quiz'					: 		{
										ename:'Quiz',
										content:'Quiz',
										icon:'',
										func:function(){eventpageopen=true;$('#events').fadeIn();setTimeout(function(){go_to_location(6),350});},
									},

	'workshops'			:		{
										ename:'Workshops',
										content:'<div style="text-align:center;width:100%;"> <div class="workshop-title"><div>OUTREACH Workshop</div></div> <div class="workshop-cont"> <div class="workshop-img"> <img src="'+imgpre+'/static/cover/main/img/workshops/AuthenticTechs.jpg" class="abs_center"> </div> <div class="workshop-desc"> <div>Authentic Techs</div> <div>Presenting the official Outreach Workshop Partner for APOGEE \'16, Authentic Techs. They will be conducting Ethical Hacking workshops all over India, and the winners get to witness APOGEE \'16 in BITS the 25th to 28th February, 2016. To register as a participant or conduct this workshop in your college, follow the link below.</div> <div><b>TOPIC: </b> Ethical Hacking/Cyber Forensic, Surface Computing, Android Development.</div><div> <a class="lb_a" href="http://authentictechs.com/bitsapogee/" target="_blank"><b><i class="fa fa-external-link"></i>&nbsp;&nbsp;Click here to register</b></a></div> </div> </div> <div class="workshop-cont"> <div class="workshop-img"> <img src="'+imgpre+'/static/cover/main/img/workshops/Jarvis.jpg" class="abs_center"> </div> <div class="workshop-desc"> <div>Jarvis India</div> <div>Presenting the official Outreach Workshop Partner for APOGEE \'16, Jarvis India. They will be conducting Internet of Things and Mobile Controlled Robotics workshops all over India, and the winners get to witness APOGEE \'16 in BITS the 25th to 28th February, 2016.</div> <div><b>TOPIC: </b>Internet of Things, Mobile Controlled Robotics.</div><div> <a class="lb_a" href="http://www.jarvisindia.net/outReach.php#68" target="_blank"><b><i class="fa fa-external-link"></i>&nbsp;&nbsp;Click here to register</b></a></div> </div> </div> <div class="workshop-title"><div>ONCAMPUS Workshop</div></div> <div class="workshop-cont"> <div class="workshop-img"> <img src="'+imgpre+'/static/cover/main/img/workshops/AuthenticTechs.jpg" class="abs_center"> </div> <div class="workshop-desc"> <div>Authentic Techs</div> <div>Presenting the official Outreach Workshop Partner for APOGEE \'16, Authentic Techs. They will be conducting Ethical Hacking/Cyber Forensic, Surface Computing, Android Development. workshops in BITS PILANI as well.</div> <div><b>TOPIC: </b> Ethical Hacking/Cyber Forensic, Surface Computing, Android Development.</div><div> <a class="lb_a" href="http://authentictechs.com/bitsapogee/" target="_blank"><b><i class="fa fa-external-link"></i>&nbsp;&nbsp;Click here to register</b></a></div> </div> </div> </div>',
										icon: imgpre+'/static/cover/main/img/lb-icons/workshops.svg',
										func:content_link,
									},

}

function content_link(b_icon,b_name,b_content){
	$('.main_head').html(b_name);
	$("div.lb_icon>img").attr("src", b_icon);
	$('.lb_descr').html(b_content);
	open_gen_lb();
}

$('.htile').click(function(){
	$('.closeside').click();
	var t= $(this);
	setTimeout(function(){
		var key = t.data('name');
		// console.log(t,key);
		map_ele_info[key]['func'](map_ele_info[key]['icon'],map_ele_info[key]['ename'],map_ele_info[key]['content']);
	},350);
});


// profile

var profile_info;
function get_pro_info(){
	$.ajax({
		url: 'http://bits-apogee.org'+imgpre+'/api/profile/',
		method: "GET",
		success: function(data){
			console.log(data);
		}
	});
}
$('.close_lb_profile').click(function(){
	$('.lb_pro_cont').fadeOut();
});
$('.pro_tab_name').click(function(){
	$('.pro_tab').css('display','none');
	$('#'+$(this).data('tab')).css('display','block');
	$('.pro_tab_name').removeClass('tab_active');
	$(this).addClass('tab_active');
});
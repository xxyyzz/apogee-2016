$(document).ready(function(){
	var data = "";
	for(var i=0;i<speaker_data.length;i++)
	{
		data+= '<div class="speaker"><div class="spk_img"><div class="spk_imgc" style="background-color:'+colors[i]+'"></div><div class="spk_imga" style="background-image: url('+speaker_data[i].img+')"></div></div><div class="speakerdet"><a class="color'+i+'" style="background-color:transparent">'+speaker_data[i]["name"]+'</a></div></div>'
	}
	$('#thinkagain .contact_data').html(data);
});
var cur_con = 0; //0-About 7-Contacts
var colors = ['#2E7D32','#F4511E','#C51162','#B71C1C','#0D47A1','#00695C','#00838F','#3E2723','#915986'];
var divname = ['#about','#cam_amb','#events','#thinkagain','#pnp','#spons','#reg','#contacts'];
var currentSpk = 0; //stores current speaker that is displayed

$('#nav_but').click(function(){
	if($(this).hasClass("is-active") == true)
	{
		$(this).removeClass("is-active");
		$('.header').fadeOut(300);
		setTimeout(function() {
			$('.header').css('background-color','');
			$('.head_content').css('display','');
			$('.but_head').css('opacity','');
			$('.but_head').css('top','15px');
			$('.fill').css({
			  '-webkit-transform' : '',
			  '-moz-transform'    : '',
			  '-ms-transform'     : '',
			  '-o-transform'      : '',
			  'transform'         : '',
			  'opacity' : '',
			});
			$('#social').css('display','none');
		}, 300);
	}
	else
	{
		$(this).addClass("is-active");
		$('.header').css('display','block');
		var ratio = ($('.header').width()>$('.header').height()?$('.header').width():$('.header').height())/250;
		$('.fill').css({
		  '-webkit-transform' : 'scale(' + ratio + ')',
		  '-moz-transform'    : 'scale(' + ratio + ')',
		  '-ms-transform'     : 'scale(' + ratio + ')',
		  '-o-transform'      : 'scale(' + ratio + ')',
		  'transform'         : 'scale(' + ratio + ')',
		  'opacity' : '1',
		});
		setTimeout(function() {
			$('.head_content').fadeIn();
			$('.but_head').css('opacity','1');
			$('.but_head').css('top','0');
		}, 300);
		setTimeout(function() {
			$('.header').css('background-color',$('.fill').css('background-color'));
			$('#social').fadeIn(500);
		}, 1000);
	}
});

$('.but_head > span').click(function(){
	if(spk_details_on){
		spk_details_init();
	}
	$(divname[cur_con]).css('display','none');
	cur_con = $(this).parent().index();
	$('#nav_but').click();
	$('#fulltransit').css('background-color',colors[7-cur_con]);
	divanim();
});

function divanim()
{
	setTimeout(function(){
		$('#ta_anim').css('display','block');
		$('#halftransit').animate({'left':'-250vw'},800);
		$('#fulltransit').animate({'left':'-150vw'},800,function(){
			$('#ta_anim').css('display','none');
			$('#halftransit').css({'left':'0vw'});
			$('#fulltransit').css({'left':'100vw'});
		});
		$(divname[cur_con]).css('display','block');
	}, 250);

}


$(document).on('click', '.speaker', function(){
	spk_details_on = true;
	var spk = $(this);
	spk.find('.speakerdet').fadeOut();
	var spk_cir = spk.find('.spk_imgc');
	spk_cir.css({
		  '-webkit-transform' : 'scale(0.07)',
		  '-moz-transform'    : 'scale(0.07)',
		  '-ms-transform'     : 'scale(0.07)',
		  '-o-transform'      : 'scale(0.07)',
		  'transform'         : 'scale(0.07)'
	});
	spk.find('.spk_imga').css('background-position','center 150%').fadeOut(250);
	$('#spk_details').css('display','block');
	setTimeout(function()
	{
		spk.siblings().css('visibility','hidden');
		$('#thinkagain').css({'overflow':'hidden'});
		spk_cir.css({'z-index':'10'});
		var ratio = ($(window).width()>$(window).height()?$(window).width():$(window).height())/500;
			spk_cir.css({
			  '-webkit-transform' : 'scale(' + ratio + ')',
			  '-moz-transform'    : 'scale(' + ratio + ')',
			  '-ms-transform'     : 'scale(' + ratio + ')',
			  '-o-transform'      : 'scale(' + ratio + ')',
			  'transform'         : 'scale(' + ratio + ')'
			});
	},400);
	setTimeout(function(){
		$('#spk_details').css('background-color',spk_cir.css('background-color'));
		thinkagain_reset(spk);
		$('#spk_content_cont').animate({'left':'0'},400);
		$('#spk_details_img').css('display','block');
		currentSpk = spk.index();
		var spk_detail = speaker_data[spk.index()];
		$('#spk_head').html(spk_detail["name"]);
		$('#spk_desc').html(spk_detail["description"]);
		$('#name_spk').html(spk_detail["name"]);
		$('.spk_sta_imga').css('background-image','url("'+spk_detail["img"]+'")');
		setTimeout(function(){

			$('.spk_sta_imgc').css({	
			  '-webkit-transform' : 'scale(1)',
			  '-moz-transform'    : 'scale(1)',
			  '-ms-transform'     : 'scale(1)',
			  '-o-transform'      : 'scale(1)',
			  'transform'         : 'scale(1)',
			  'opacity':'1'
			});
			setTimeout(function(){

				$('.spk_sta_imga').fadeIn().css({'background-position': 'center bottom'});
			},350);
			$('#spk_head').css('color',$('#spk_details').css('background-color'));
			$('#spk_content').fadeIn(500);
			$('#spk_back').fadeIn(500);
			$('#name_slide').fadeIn(500);
		},450);
	},1000);


});
$('#spk_back').click(function(){
	spk_details_init();
	cur_con = 3;
	divanim();
});
function spk_details_init(){
	$('#spk_details').css('display','none');
	$('#spk_details').css('background-color','');
	$('#spk_content_cont').css('left','');
	$('#spk_details_img').css('display','');
	$('.spk_sta_imgc').css({	
	  '-webkit-transform' : '',
	  '-moz-transform'    : '',
	  '-ms-transform'     : '',
	  '-o-transform'      : '',
	  'transform'         : '',
	  'opacity':''
	});
	$('.spk_sta_imga').css({'background-position': '','display':'none'});		
	$('#spk_content').css('display','none');
	$('#spk_back').css('display','none');
	$('#name_slide').css('display','none');
	spk_details_on=false;
}
var spk_details_on = false;
function changeSpk(forward){
	if(forward){
		currentSpk++;
		if(currentSpk==speaker_data.length)
		{
			currentSpk = 0;
		}
	}
	else{
		currentSpk--;
		if(currentSpk<0)
		{
			currentSpk = speaker_data.length-1;
		}
	}
	var ratio = ($(window).width()>$(window).height()?$(window).width():$(window).height())/500;
	$('#spk_det_fill').css({
	  'background-color' : colors[currentSpk],
	  '-webkit-transform' : 'scale('+ratio+')',
	  '-moz-transform'    : 'scale('+ratio+')',
	  '-ms-transform'     : 'scale('+ratio+')',
	  '-o-transform'      : 'scale('+ratio+')',
	  'transform'         : 'scale('+ratio+')',
	});
	$('.spk_sta_imgc').css({	
	  '-webkit-transform' : 'scale(0)',
	  '-moz-transform'    : 'scale(0)',
	  '-ms-transform'     : 'scale(0)',
	  '-o-transform'      : 'scale(0)',
	  'transform'         : 'scale(0)',
	  'opacity':'0.2'
	});
	$('.spk_sta_imga').css('opacity','0');
	$('#name_slide').fadeOut(100);
	$('#spk_head').css('opacity','0');
	$('#spk_desc').css('opacity','0');
	setTimeout(function() {
		$('.spk_sta_imgc').css({	
			  '-webkit-transform' : 'scale(1)',
			  '-moz-transform'    : 'scale(1)',
			  '-ms-transform'     : 'scale(1)',
			  '-o-transform'      : 'scale(1)',
			  'transform'         : 'scale(1)',
			  'opacity':'1'
			});
		$('#spk_det_fill').css({
		  'background-color' : '',
		  '-webkit-transform' : '',
		  '-moz-transform'    : '',
		  '-ms-transform'     : '',
		  '-o-transform'      : '',
		  'transform'         : '',
		});
		$('#spk_details').css('background-color',colors[currentSpk]);
		$('.spk_sta_imga').css({'background-position': ''});
		var spk_detail = speaker_data[currentSpk];
		$('#spk_head').html(spk_detail["name"]);
		$('#spk_desc').html(spk_detail["description"]);
		$('#name_spk').html(spk_detail["name"]);
		$('.spk_sta_imga').css('background-image','url("'+spk_detail["img"]+'")');
		setTimeout(function() {
			$('#name_slide').stop(true,true).fadeIn();
			$('#spk_head').css('color',$('#spk_details').css('background-color'));

			$('#spk_head').css('opacity','1');
			setTimeout(function() {
				$('#spk_desc').css('opacity','1');
			}, 150);
			$('.spk_sta_imga').css('opacity','1');
			$('.spk_sta_imga').css({'background-position': 'center bottom'});
		}, 250);
	}, 300);
}
function thinkagain_reset(spk) 
{
	$('#thinkagain').css('display','none');
	spk.find('.speakerdet').css('display','block');
	var spk_cir = spk.find('.spk_imgc');
	spk_cir.css({
		  '-webkit-transform' : '',
		  '-moz-transform'    : '',
		  '-ms-transform'     : '',
		  '-o-transform'      : '',
		  'transform'         : ''
	});
	spk_cir.css({'z-index':''});
	spk.find('.spk_imga').css('background-position','center bottom').css('display','block');
	$('#spk_details').css('display','block');
	spk.siblings().css('visibility','visible');
	$('#thinkagain').css({'overflow':'auto'});
}

var imgpre = "/2016"

var speaker_data = 
[
	{
		name:'(Late) Dr. APJ Abdul Kalam',
		description:'<b>The ‘Missile Man of India’</b><br><br></p> Dr. APJ Abdul Kalam was a great leader, an accomplished scientist, a passionate teacher and a true patriot. An aeronautics engineer from Madras Institute of Technology, Kalam was considered the brain of missile programme in India. He contributed in great measures to the development of ballistic missile and the launch of vehicle technology, making India one of the forerunners in missile technology in the world. His work got him several accolades including the Padma Bhushan, Padma Vibhushan and Bharat Ratna, India\'s highest civilian honour</p>',
		img:imgpre+'/static/cover/intro/images/speaker/apj.png',
	},
	{
		name:'Jimmy Wales',
		description:'<b>Fouder of the ‘WIKIPEDIA‘</b><br><br></p> Today Wikipedia is the fifth most popular website in the world, and leading technology futurist and Wikipedia founder, Jimmy Wales, is one of the most sought after visionaries in business and technology. Named among the Time Magazine\'s "100 Most Influential People,"[2006] Jimmy Wales has also been acknowledged by the World Economic Forum as one of the top 250 young leaders across the world for his professional accomplishments, his commitment to society, and his potential to contribute to shaping the future of the world.</p>',
		img:imgpre+'/static/cover/intro/images/speaker/wales.png',
	},
	{
		name:'Jeff Lieberman',
		description:'<b>Host of the popular TV Series ‘Time Warp‘</b><br><br></p> We consciously perceive less than one trillionth of the reality in which we live. Our senses are doorways with invisible edges, compressing the infinite complexity of the universe into a manageable finite form. Jeff Lieberman, the host of the popular “Time Warp” series on Discovery Channel, is an avid explorer who has taken the scientific path into solving the enigma that is human consciousness. His work is an enlightening foray that exploits the edges, making us conscious of our doors of perception, and questioning the nature of perception and the universe itself.</p>',
		img:imgpre+'/static/cover/intro/images/speaker/jeff.png',
	},
	{
		name:'Dr. Pawan Agrawal',
		description:'<b>‘Mumbai Dabbawalas‘</b><br><br></p> "Believe me friends after I have spoken, you won\'t be able to move from your chair. This is my guarantee." These were the opening words of Dr. Pawan Agrawal at Think Again Conclave 2013. The CEO of Mumbai Dabbawalas, Dr. Pawan exuded sheer confidence as he spoke at length about the six-sigma and ISO certified organisation. Having scripted history with by showcasing excellence in customer care for more than a century, the dabbawalas have piqued interest and earned repute at the global level.</p>',
		img:imgpre+'/static/cover/intro/images/speaker/pawan.png',
	},
	{
		name:'Prof. Walter Lewin',
		description:'<b>Physics Nobel Laureate</b><br><br></p> Prof. Walter Lewin is a renowned astrophysicist and emeritus professor at MIT, is a figure well known across the globe for his video lectures on Physics. A widely acclaimed professor, Lewin is considered to be in the same league as Feynman and Pauli when it comes to teaching.</p><p>He is popular for his riveting online lectures and courses in physics. For about 15 years, Lewin was on MIT Cable TV, with every week a different 1-hour program. His lectures appeal to a vast majority of students because of his idea of using demonstrations to provide vivid clarity of the concept. His lectures are viewed over 2 million times yearly.</p>',
		img:imgpre+'/static/cover/intro/images/speaker/lewin.png',
	},
	{
		name:'Elena Bodnar',
		description:'<b>Designer of the Emergency Bra</b><br><br></p> For Dr. Elena Bodnar, the director of the Chicago-based Trauma Risk Management Research Institute, the inspiration for designing the Emergency Bra, a traditional-looking brassiere that converts into two respiratory face masks in case of fire, natural disaster or terrorist attack came from two disasters. Fresh out of med school in Ukraine (then the Soviet Union) in 1986, she helped treat victims of the Chernobyl nuclear explosion. Years later, after Bodnar moved to Chicago, footage of September 11 victims using shirts to filter out debris got her thinking again about the Emergency Bra.</p>',
		img:imgpre+'/static/cover/intro/images/speaker/elena.png',
	},
	{
		name:'Dr. Walter Bender',
		description:'<b>Renowned Alumnus of the MIT Media Labs</b><br><br></p> Dr. Walter Bender is an alumnus of MIT, a technologist and researcher who works in the field of electronic publishing, media and technology for learning. He is founder of Sugar Labs, which develops educational software used by more than three-million children in more than forty countries. He launched the era of digital news in 1992 by forming the MIT News in the Future consortium. In 2006, Bender co-founded the One Laptop per Child, a non-profit association with Nicholas Negroponte and Seymour Papert. He is the person behind the Open Leaning Program which would enable collaborative research among universities globally.</p>',
		img:imgpre+'/static/cover/intro/images/speaker/bender.png',
	},
	{
		name:'Dr. Bindeshwar Pathak',
		description:'<b>Founder of the Sulabh International</b><br><br></p> Dr. Bindeshwar Pathak is an Indian sociologist and the founder of Sulabh International, a social service organization which works to promote human rights, environmental sanitation, non-conventional sources of energy, waste management and social reforms through education. His work is considered one of the pioneer in social reform especially in the field of sanitation and hygiene, for which he has received various national and international awards.</p>',
		img:imgpre+'/static/cover/intro/images/speaker/bin_pat.png',
	},
];


var spons_data=
[
	{
		img_url:imgpre+'/static/cover/intro/images/sponsors/askme.png',
		site_url:'http://www.askme.com/'
	},
	{
		img_url:imgpre+'/static/cover/intro/images/sponsors/benq.png',
		site_url:'http://www.benq.co.in/'
	},
	{
		img_url:imgpre+'/static/cover/intro/images/sponsors/caravan.png',
		site_url:'http://www.caravanmagazine.in/'
	},
	{
		img_url:imgpre+'/static/cover/intro/images/sponsors/ebay.png',
		site_url:'http://www.ebay.in/‎'
	},
	{
		img_url:imgpre+'/static/cover/intro/images/sponsors/ibm.png',
		site_url:'http://www.ibm.com/in-en/'
	},
	{
		img_url:imgpre+'/static/cover/intro/images/sponsors/informos.png',
		site_url:'http://informossys.com/'
	},
	{
		img_url:imgpre+'/static/cover/intro/images/sponsors/microsoft.png',
		site_url:'https://www.microsoft.com/en-in/'
	},
	{
		img_url:imgpre+'/static/cover/intro/images/sponsors/philips.png',
		site_url:'http://www.philips.co.in/'
	},
	{
		img_url:imgpre+'/static/cover/intro/images/sponsors/robosapiens.png',
		site_url:'http://www.robosapi.com/'
	},
	{
		img_url:imgpre+'/static/cover/intro/images/sponsors/tata_tiscon.png',
		site_url:'http://www.tatatiscon.co.in/'
	},
	{
		img_url:imgpre+'/static/cover/intro/images/sponsors/the_open_car.png',
		site_url:'#'
	},
	{
		img_url:imgpre+'/static/cover/intro/images/sponsors/tplink.jpg',
		site_url:'http://www.tp-link.in/'
	},
	{
		img_url:imgpre+'/static/cover/intro/images/sponsors/airtel.png',
		site_url:'http://www.airtel.in/'
	},
	{
		img_url:imgpre+'/static/cover/intro/images/sponsors/redbus.png',
		site_url:'https://www.redbus.in/'
	},
	{
		img_url:imgpre+'/static/cover/intro/images/sponsors/week.jpg',
		site_url:'http://www.theweek.in/'
	}
];

function sponsload()
{
	var dt="";
	for(i=0;i<spons_data.length;++i)
	{
		dt+= '<a href="'+spons_data[i].site_url+'" target="_blank"><div class="spons_cont">'+'<img src="'+spons_data[i].img_url+'" class="spons_img abs_center"></div></a>';
	}

	$('#sponsdata').html(dt);
}
sponsload();

 var contacts_data = 
 [
	{
		dept:'President',
		img_url:imgpre+'/static/cover/intro/images/contacts/prez.jpg',
		fb_link:'https://www.facebook.com/akhil.reddy.148',
		cname:'AKHIL REDDY',
		phone:'+91-7728835792',
		email:'president[at]pilani.bits-pilani.ac.in',
	},
	{
		dept:'General Secretary',
		img_url:imgpre+'/static/cover/intro/images/contacts/gen.jpg',
		fb_link:'https://www.facebook.com/rijul.dutta',
		cname:'RIJUL DUTTA',
		phone:'+91-8427686647',
		email:'gensec[at]pilani.bits-pilani.ac.in',
	},
	{
		dept:'For sponsorship and marketing',
		img_url:imgpre+'/static/cover/intro/images/contacts/spons.jpg',
		fb_link:'https://www.facebook.com/mohammed.motiwala1',
		cname:'MOHAMMED MOTIWALA',
		phone:'+91-7728086752',
		email:'sponsorship[at]bits-apogee[dot]org',
	},
	{
		dept:'For reception and accommodation',
		img_url:imgpre+'/static/cover/intro/images/contacts/recnacc.jpg',
		fb_link:'https://www.facebook.com/aditya.gogri',
		cname:'ADITYA GOGRI',
		phone:'+91-9772229698',
		email:'recnacc[at]bits-apogee[dot]org',
	},
	{
		dept:'For invites and correspondence',
		img_url:imgpre+'/static/cover/intro/images/contacts/pcr.jpg',
		fb_link:'https://www.facebook.com/profile.php?id=100006361090120',
		cname:'ADITYA CHAUHAN',
		phone:'+91-8239822574',
		email:'pcr[at]bits-apogee[dot]org',
	},
	{
		dept:'For Publicity and Online Partnership',
		img_url:imgpre+'/static/cover/intro/images/contacts/adp.jpg',
		fb_link:'https://www.facebook.com/kunal.barapatre.31',
		cname:'KUNAL BARAPATRE',
		phone:'+91-7728095594',
		email:'adp[at]bits-apogee[dot]org',
	},
	{
		dept:'For projects, events and registration',
		img_url:imgpre+'/static/cover/intro/images/contacts/controls.jpg',
		fb_link:'https://www.facebook.com/falguni.agrawal.965',
		cname:'FALGUNI AGARWAL',
		phone:'+91-9928089204',
		email:'controls[at]bits-apogee[dot]org',
	},
	{
		dept:'For paper presentations and Guest Lectures',
		img_url:imgpre+'/static/cover/intro/images/contacts/pep.jpg',
		fb_link:'https://www.facebook.com/adivijaykumar',
		cname:'ADITYA V KUMAR',
		phone:'+91-8385857855, +91-8058722661',
		email:'pep[at]bits-apogee[dot]org, guestlectures[at]bits-apogee[dot]org',
	},
	{
		dept:'For website and online registration queries',
		img_url:imgpre+'/static/cover/intro/images/contacts/dvm.jpg',
		fb_link:'https://www.facebook.com/pranjalONfb',
		cname:'PRANJAL GUPTA',
		phone:'+91-8094076999',
		email:'webmaster[at]bits-apogee[dot]org',
	}
 ];

 function contactsload()
{
	var dt="";
	for(i=0;i<contacts_data.length;++i)
	{
		dt+= '<div class="contactinfo"><div class="contact_dept">'+contacts_data[i].dept+'</div><div style="position:relative"><img src="'+ contacts_data[i].img_url+'" class="contact_img" /><a href="'+ contacts_data[i].fb_link +'" target="_blank"><div class="fb_link" ><?xml version="1.0" ?><!DOCTYPE svg  PUBLIC "-//W3C//DTD SVG 1.1//EN"  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd"><svg  class="confb" enable-background="new 0 0 56.693 56.693" height="30px" id="Layer_1" version="1.1" viewBox="0 0 56.693 56.693" width="30px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><style type="text/css"><![CDATA[svg .confb{ cursor: pointer;transition: 150ms;transition-timing-function: ease-in-out;-webkit-transition: 150ms;-webkit-transition-timing-function: ease-in-out;fill:#fff;} .confb:hover{ fill: #3b5998;}]]></style><path d="M40.43,21.739h-7.645v-5.014c0-1.883,1.248-2.322,2.127-2.322c0.877,0,5.395,0,5.395,0V6.125l-7.43-0.029  c-8.248,0-10.125,6.174-10.125,10.125v5.518h-4.77v8.53h4.77c0,10.947,0,24.137,0,24.137h10.033c0,0,0-13.32,0-24.137h6.77  L40.43,21.739z"/></svg></div></a></div><div class="contact_det"><b>'+contacts_data[i].cname +'</b><br>'+contacts_data[i].phone +'<br>'+contacts_data[i].email+'</div></div>';
	}

	$('#c_data').html(dt);
}

contactsload();




$('.header .but_head>span').hover(function(){
	var i = $(this).parent().index();
	$(this).css('color',colors[i]);
},function(){
	$(this).css('color','#000');
})



function projmasteranim(){
	$('#red0 , #blue0').css({display:"block"});
	$('#red0').animate({left:"0%"},600,function() {
		
	});
	setTimeout(function() {
		$('#blue0').animate({right:"0%"},300,function(){
			projectanimate();
		});
	},300);
	
}

function projectanimate(){
	$('#tile1').addClass('tile1anim');
	$('#tile2').addClass('tile2anim');
}
function pnpinit()
{
	$('#red0 , #blue0').css({display:"none"});
	setTimeout(function(){projmasteranim()},1000);
	$('#red0').css({left:"-100%"});
	$('#blue0').css({right:"-50%"});
	$('#tile1').removeClass('tile1anim');
	$('#tile2').removeClass('tile2anim');	
}

function formup()
{
	$('#regform').css({'opacity':'','margin-top':''});
	setTimeout(function(){
		$('#regform').animate({'opacity':'1','margin-top':'0'},800);
	},1100);
}

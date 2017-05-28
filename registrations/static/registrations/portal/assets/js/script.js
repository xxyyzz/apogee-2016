
status_query = {
	'ref' : '',
	'cat' : ''
}

routes = {
	'papers' : {
		'sub' : {
			'instr' : {
				'func' : init_papers_instr
			},
			'form' : {
				'func' : init_papers_form
			},
			'status' : {
				'func' : init_papers_status
			}
		},
		'prep' : prep_papers,
	},
	'projects' : {
		'sub' : {
			'instr' : {
				'func' : init_projects_instr
			},
			'form' : {
				'func' : init_projects_form
			},
			'status' : {
				'func' : init_projects_status
			}
		},
		'prep' : prep_projects,
	},
	'check' : {
		'sub' : {
			'form' : {
				'func' : init_check_form
			},
			'status' : {
				'func' : init_check_status
			}
		},
		'prep' : prep_check,
	},
	'campus-ambassador' : {
		'func' : init_CampusAmbassadorForm
	},
	'' : {
		'func' : init_Default
	},
	'contact' : {
		'func' : init_Contact
	},
}

click = {
	'x' : 0,
	'y' : 0
}

window.addEventListener("hashchange", function() {
	setTimeout(urlparse(), 100);
});

function wrapLink(link) {
	var base = String(location).substring(0,(String(location).indexOf("#")));
	var route = String(location).substring(String(location).indexOf("#")+1);
	if(route != link ) {
		var construct = base + "#" + link;
		location = construct;
	}
}

function urlparse() {
	var route = String(location).indexOf("#");
	if(route == -1) {
		location = location + "#/";
		urlparse();
	}
	else {
		route = String(location).substring(route+2,String(location).length-1);
		route = route.split("/");
		var p = 0;
		var base = routes;
		while(p<route.length) {
			var found = 0;
			var node = 0;
			for(var r in base) {
				if(r == route[p]) {
					found = 1;
					if(base[r].hasOwnProperty('sub')) {
						base[r]['prep']();
						base = base[r]['sub'];
					}
					else {
						close_body_box();
						base[r]['func'](routes[r]);
						node = 1;
					}
					p++;
					break;
				}
			}
			if(found == 0) {
				wrapLink("/");
				break;
			}
			if(node == 1) {
				break;
			}
		}
	}
}

/* ------------------------ FUNCTION FOR PAPERs --------------------------------*/

function prep_papers() {
	changeLinkFocus('papers');
	createRipple('#5D4037');
}

function init_papers_instr(obj) {
	$.ajax({
		url : 'papers/instructions/',
		method : 'GET',
		success : function(data) {
			$(".body-box").html(data);
			open_body_box();
		}
	});
}

function init_papers_form(obj) {
	$.ajax({
		url : 'papers/form/',
		method : 'GET',
		success : function(data) {
			$(".body-box").html(data);
			open_body_box();
		}
	})
}

function init_papers_status(obj) {
	console.log("init paper");
}


/* ------------------------ FUNCTION FOR PROJECTs --------------------------------*/

function prep_projects() {
	changeLinkFocus('projects');
	createRipple('#0277BD');
}

function init_projects_instr(obj) {
	$.ajax({
		url : 'projects/instructions/',
		method : 'GET',
		success : function(data) {
			$(".body-box").html(data);
			open_body_box();
		}
	});
}

function init_projects_form(obj) {
	$.ajax({
		url : 'projects/form/',
		method : 'GET',
		success : function(data) {
			$(".body-box").html(data);
			open_body_box();
		}
	});
}

function init_projects_status(obj) {
	console.log("init projects");
}


/* ------------------------ FUNCTION FOR CHECK STATUS --------------------------------*/

function prep_check() {
	changeLinkFocus('check');
	createRipple('#c92b3c');
}

function init_check_form(obj) {
	$.ajax({
		url : 'check/form/',
		method : 'GET',
		success : function(data) {
			$(".body-box").html(data);
			open_body_box();
		}
	});
}

function init_check_status(obj) {
	$.ajax({
		url : 'check/status/',
		method : 'POST',
		data : status_query,
		success : function(data) {
			$(".body-box").html(data);
			open_body_box();
		}
	});
}

function init_CampusAmbassadorForm(obj) {
	console.log("init campus-ambassador");
	createRipple('#1565C0');
}

function init_Contact(obj) {
	changeLinkFocus('contacts');
	createRipple('#455A64');
}

function init_Default(obj) {
	changeLinkFocus('');
	createRipple('#546E7A');
	$.ajax({
		url : 'updates/',
		method : 'GET',
		success : function(data) {
			$(".body-box").html(data);
			open_body_box();
		}
	})
}

/*-------------------------------- BODY BOX FUNCTIONS ----------------------------*/

function close_body_box() {
	$(".body-box").html("").css({
		'padding-top' : '200px',
		'opacity' : 0
	});
}

function open_body_box() {
	setTimeout(function() {
		$(".body-box").animate({
			'padding-top' : '140px',
			'opacity' : 1
		}, 400);
	}, 400);
}


/*------------------------------------ ANIMATION --------------------------------*/

function createRipple(color) {
	$ref = $('<div/>', {
		class : 'ripple'
	}).appendTo($(".head-cover")).css({
		'left' : click['x']+'px', 
		'top' : click['y']+'px',
		'background-color' : color
	});

	setTimeout(function() {
		$(".head-cover").css({
			'background-color' : color
		});
	}, 900);

	setTimeout(function() {
		$(".ripple").remove();
	}, 1000);
}



/*------------------------------------------- HEAD LINKS --------------------------*/

$(".right-link").click(function(e) {
	var lnk = $(this).attr("value");
	click['x'] = e.pageX; 
	click['y'] = e.pageY;
	wrapLink(lnk);
});

function changeLinkFocus(str) {
	$(".right-link").removeClass('right-link-active');
	$(".link-"+str).addClass('right-link-active');
}



urlparse();



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


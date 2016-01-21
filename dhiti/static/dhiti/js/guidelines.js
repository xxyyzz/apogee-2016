$("#r2").click(function() {
	$("#r1c").delay(200).fadeOut();
}).click(function() {
	$("#r1").delay(500).animate({
		width: "5%",
	}, {
		duration: 500,
		specialEasing: {
			width: "linear",
			height: "easeOutBounce"
		}
	});
}).click(function() {
	$("#r2").delay(500).animate({
		width: "90%",
	}, {
		duration: 500,
		specialEasing: {
			width: "linear",
			height: "easeOutBounce"
		}
	});
}).click(function() {
	$("#r2c").delay(1000).fadeIn();
}).click(function() {
	$("#r2i").fadeOut();
}).click(function() {
	$("#r1i").delay(1000).fadeIn();
});
$("#r1").click(function() {
	$("#r2c").fadeOut();
}).click(function() {
	$("#r2").delay(500).animate({
		width: "5%",
	}, {
		duration: 500,
		specialEasing: {
			width: "linear",
			height: "easeOutBounce"
		}
	});
}).click(function() {
	$("#r1").delay(500).animate({
		width: "90%",
	}, {
		duration: 500,
		specialEasing: {
			width: "linear",
			height: "easeOutBounce"
		}
	});
}).click(function() {
	$("#r1c").delay(1000).fadeIn();
}).click(function() {
	$("#r1i").fadeOut();
}).click(function() {
	$("#r2i").delay(1000).fadeIn();
});
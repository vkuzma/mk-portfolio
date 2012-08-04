$(document).ready(function() {
	$('.roll-over-panel-wrapper').mouseenter(function(event) {
		console.log($(event.currentTarget).parent().find('.preview'));
		$(event.currentTarget).parent().find('.preview').addClass('hover');
	});

	$('.roll-over-panel-wrapper').mouseleave(function(event) {
		console.log($(event.currentTarget).parent().find('.preview'));
		$(event.currentTarget).parent().find('.preview').removeClass('hover');
	});
});
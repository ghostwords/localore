$.ajax($('#juicer-summary-item').data('juicer-summary-item-url'))
	.done(function (data) {
		$('#juicer-summary-item')
			.removeClass('icon-spinner')
			.addClass('icon-site')
			.append(data);
	});

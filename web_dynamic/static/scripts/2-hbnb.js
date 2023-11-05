document.ready(function () {
	const _amenity = {};
	$("li input[type=checkbox]").change(function () {
		if (this.checked) {
			_amenity[this.dataset.name] = this.dataset.id;
		} else {
			delete _amenity[this.dataset.name];
		}
		$(".amenities h4").text(Object.keys(_amenity).sort().join(", "));
	});

	$.getJSON("http://0.0.0.0:5001/api/v1/status/", (data) => {
		if (data.status === "OK") {
			$("div#api_status").addClass("available");
		} else {
			$("div#api_status").removeClass("available");
		}
	});
});
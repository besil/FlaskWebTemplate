"use strict";

class Model {
	constructor(url) {
		this.remote_endpoint = location.origin;
	}

	// Defines here your methods for REST api
	data() {
		return JSON.parse(this.httpGet(this.remote_endpoint+"/example/data"));
	}
		
	httpGet(theUrl) {
		var xmlHttp = new XMLHttpRequest();
		xmlHttp.open("GET", theUrl, false); // false for synchronous request
		xmlHttp.send(null);
		return xmlHttp.responseText;
	}
};


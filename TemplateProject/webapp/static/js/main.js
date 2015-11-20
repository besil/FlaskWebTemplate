"use strict";

var remote_url = window.location.href;
var model = new Model(remote_url);

var example_data = model.data();
alert("Example consuming REST API: "+example_data);
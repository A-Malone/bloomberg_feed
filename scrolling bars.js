var svg = d3.select("#target")
			.append('svg')
			.attr('width', "95%")
			.attr('height', 500)
			.append("g");
var gbar = svg.append('rect')
			 .attr('x',1000)
			 .attr('y',0)
			 .attr('width',100)
			 .attr('height', "100%")
			 .attr('fill','red');
var rbar = svg.append('rect')
			  .attr('x',1100)
			  .attr('y',0)
			  .attr('width',100)
			  .attr('height', "100%")
			  .attr('fill','green');
var ybar = svg.append('rect')
			  .attr('x',1200)
			  .attr('y',0)
			  .attr('width',100)
			  .attr('height', "100%")
			  .attr('fill','yellow');
var rpos = 1100, gpos = 1000,ypos=1200;	//Declare the starting positions of the bars
while (ypos > -105){ //always must be the last value
	rpos--;
	gpos--;
	ypos--;
	gbar.transition().attr('x',gpos).duration(5000).ease('linear');
	rbar.transition().attr('x',rpos).duration(5000).ease('linear');
	ybar.transition().attr('x',ypos).duration(5000).ease('linear');
}
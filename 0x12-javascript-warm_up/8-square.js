#!/usr/bin/node

const x = process.argv[2];

if (!parseInt(x)){
	console.log("Missing size");
}else {
	for (let i = 0; i < x; i++){
		let row = "";
		for (let h = 0; h < x; h++)row+= "X";
		console.log(row);
	}
}

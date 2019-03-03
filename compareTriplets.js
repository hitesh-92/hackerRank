/*
Your task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1] and a[2] with b[2]


if 
	a[i] > b[i] Alice awarded point

	a[i] < b[i] Bob awarded point

	a[i] == b[i] neither person receives a point.
*/


function compareTriplets(a, b) {

	let Alice = 0, Bob = 0

	for(let i = 0; i < a.length; i++) {
		if(a[i]==b[i]) continue
		a[i] > b[i] ? Alice++ : Bob++
	}
	
	console.log(Alice, Bob)
	return [Alice, Bob]
}



// const Alice = [17, 28, 30], Bob = [99, 16, 8]
const A=[5, 6, 7], B=[3,6,10]
compareTriplets(A, B)
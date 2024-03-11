function add(a, b) {
    return a + b;
}

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

if (!isNaN(arg1) && !isNaN(arg2)) {
    console.log("The addition of", arg1, "and", arg2, "is:", add(arg1, arg2));
} else {
    console.log("Please provide valid integer arguments.");
}


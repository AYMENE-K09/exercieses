const the_needed_height = 145;
let user_height = ParseInt(prompt("enter your height by cm: "));
if (the_needed_height < user_height) {
    console.log("you are tall enough to ride");
} else {
    console.log("you need grow some more to ride");
}

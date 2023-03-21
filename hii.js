// function fun_one(){
//     return "Hello";
// }
// function fun_two(){
//     return fun_one();
// }
// console.log( fun_two() );  


// function fun_one(){
//     return "Hello";
// }
// function fun_two(){
//     return fun_one;
// }
// console.log( fun_two()() );  

let fun_one = (arg1,arg2,arg3)=>{
    console.log(arg1,arg2,arg3);
}
fun_one("Angular13","NodeJS","MongoDB");                //Angular13 NodeJS MongoDB
fun_one("ReactJS","NodeJS","MongoDB");                  //Angular13 NodeJS MongoDB
fun_one("VueJS","NodeJS","MongoDB");                    //VueJS NodeJS MongoDB
fun_one();                                              //undefined undefined undefined
fun_one(undefined,"Hello_2");                           //undefined undefined undefined
fun_one(null,null,null);        
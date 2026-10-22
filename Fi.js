//const path=require('path')
//const os=require('os')




//console.log(__dirname)

//console.log(path)

//console.log(path.join(__dirname,"first.txt"))

//const a=path.join(__dirname,"fi7.txt")
//const filepath=path.join(__dirname,"example","fi7.txt")
//console.log(filepath)

//console.log(path.basename("fi7.txt"))

//console.log(path.extname("first.py"))

//console.log(path.dirname('fi2.txt'))

//console.log(path.dirname('/first/fi.txt'))
//console.log(path.parse("my.js"))
//console.log(os.version())
//console.log(os.hostname())
//console.log(os.type())








/*const fs=require("fs").promises;
const path=require("path")



 const project=async()=>{


  try{
    const filepath=path.join(__dirname,"my7","first.txt")

    const file2=path.join(__dirname,"my7","first2.txt")

    //fs.writeFile(path.join(__dirname,"my7","fir.txt"),"hello jav")



     //await fs.writeFile(filepath,"java full stack")
     //console.log("write succeas")

     //const data1=await fs.readFile(filepath,'utf8') //kuu868
     
     
      //console.log("read succeas",data1)  //encoder

       //await fs.appendFile(filepath,",python full stack")
         //    console.log("append succeas")


         await fs.rename(filepath,file2)
           console.log("rename succeas")



  }
  catch(e){
    console.log(e,"error show")
  }


  process.on("uncaughtException",(er)=>{
    console.log("uncaught error",er)
    process.exit(1);  // suuce 0  
  })

 }

project()*/



const http=require("http")



const server=http.createServer((req,res)=>{

    console.log(req.url)  // get /
    console.log(req.method)  //get



    res.setHeader("Content-Type","text/html")

    res.write("<html>")
    res.write("<head><title>shop kart</title></head>")
    res.write("<body><h1>this is node classs</h1></body>")

    res.write("</html>")



    res.end();


    
    
})



server.listen(5000,()=>{
    console.log("server connect 5000 port")
})
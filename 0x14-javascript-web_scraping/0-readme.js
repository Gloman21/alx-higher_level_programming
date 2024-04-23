#!/urs/bin/node
# a script that reads and prints the content of a file

const fs=require('fs'),[path]=process.argv.slice(2);
fs.readFile(path,'utf-8',(err,data)=>err?console.error(err):console.log(data));

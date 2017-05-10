# My ls flavor
unalias ll
function ll(){
  ls -lrtah $@
}
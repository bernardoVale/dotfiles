# Configure Git user email
gmail(){
  if [ $1 = 'avenuecode' ]; then
    git config --global user.email bvale@avenuecode.com
  elif [ $1 = 'wsgc' ]; then
    git config --global user.email bvale@wsgc.com
  elif [ $1 = 'gmail' ]; then
    git config --global user.email bernardosilveiravale@gmail.com
  fi
}
choice=yes
echo $choice

while [ $choice != q ]
do
  echo "1. Vocabulary"
  echo "2. Currency Calculator"
  echo "3. Download Dir cleanup"
  read choice
  echo choice: $choice

  if [ "$choice" == "\n" ]
  then
    echo carriage
    break
  fi  


  if [ $choice == 1 ] 
  then
    echo vocabulary
    cd ./3.vocabulary-com
    sh 1.run.sh
    cd ..

  elif [ $choice == 2 ]
  then
    echo currency
    cd ./5.currency-calculator
    sh 1.run.sh
    cd ..
  elif [ $choice == 3 ]
  then
    echo currency
    cd ./1.os-tasks
    sh 1.run.sh
    cd ..
  fi

done

echo finish


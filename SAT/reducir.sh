#python prueba.py 

a=$1
b=$2

for file in InstanciasSAT/*; do
  path="${file##*/}"
  python Reductor/reductor.py $path $b
done



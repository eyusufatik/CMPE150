test_dir=$2
files=$(ls $test_dir)

for i in $files
do
for j in $(ls $test_dir/$i)
do
extension="${j##*.}"
if [[ ! $extension = "out" ]]
then
    cat $test_dir/$i/$j > calc.in
    python3 $1
    out=$(diff -w calc.out $test_dir/$i/$j.out)
    if [[ ! $out = "" ]]
    then
        echo "error in $test_dir$i$j"
        break
    fi
fi
done
done

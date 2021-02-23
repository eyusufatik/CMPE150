test_dir=$2
files=$(ls $test_dir)

for i in $files
do
echo $i
cat $test_dir/$i/crime_scene.txt > crime_scene.txt
python3 $1

out=$(diff -w solution_part1.txt $test_dir/$i/solution_part1.txt)
if [[ ! $out = "" ]]
then
    echo "error in $test_dir/$i"
    break
fi

out=$(diff -w solution_part2.txt $test_dir/$i/solution_part2.txt)
if [[ ! $out = "" ]]
then
    echo "error in $test_dir/$i"
    break
fi

out=$(diff -w solution_part3.txt $test_dir/$i/solution_part3.txt)
if [[ ! $out = "" ]]
then
    echo "error in $test_dir/$i"
    break
fi

done

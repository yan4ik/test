# Simple testing utility to check against built-int `sort` function.

num_str=10000
str_len=100
ram=1000

for iteration in {1..10}
do
    python3 generator.py input.txt -n $num_str -s $str_len
    
    python3 external_sort.py input.txt output.txt -n $num_str -r $ram -k 10
    
    sort input.txt > output.builtin.txt

    cmp --silent output.txt output.builtin.txt || echo "Ooops! Files are different!"
done

rm input.txt output.txt output.builtin.txt

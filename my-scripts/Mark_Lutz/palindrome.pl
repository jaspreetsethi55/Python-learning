$num = 1221;

sub palindrome
{
    my $n = shift;
    my @new_num;
    my $new_num = 0;
    for (reverse(split('',$n)))
    {
        push(@new_num,$_);
    }
    
    $new_num = join('',@new_num);
    $n == $new_num ? return 'Palindrome' : 'Not palindrome';
}
    

$out = palindrome($num);
print "$out\n";

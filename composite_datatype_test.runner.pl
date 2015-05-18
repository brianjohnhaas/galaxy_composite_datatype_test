#!/usr/bin/env perl

use strict;
use warnings;

#my $ret = system("echo test main file > test.compositeDatatypeTest");
#if ($ret) {
#    die "Error echo cmd died";
#}


for my $num (1, 2, 3) {

    open (my $ofh, ">test_file_$num.txt") or die "Error, cannot write to file";
    print $ofh "testing $num\n";
    close $ofh;
}

print STDERR "my stderr";
print STDOUT "my stdout";

exit(0);


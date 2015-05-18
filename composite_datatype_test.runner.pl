#!/usr/bin/env perl

use strict;
use warnings;

my $usage = "usage: $0 outdir\n\n";

my $outdir = $ARGV[0] or die "\n\n\t$usage\n\n";

unless (-d $outdir) {
    my $ret = system("mkdir -p $outdir");
    if ($ret) {
        die "Error, cannot mkdir -p $outdir";
    }
}


#my $ret = system("echo test main file > test.compositeDatatypeTest");
#if ($ret) {
#    die "Error echo cmd died";
#}


for my $num (1, 2, 3) {

    open (my $ofh, ">$outdir/test_file_$num.txt") or die "Error, cannot write to file";
    print $ofh "testing $num\n";
    close $ofh;
}

print STDERR "my stderr";
print STDOUT "my stdout";

exit(0);


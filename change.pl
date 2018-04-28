#!/usr/bin/perl -w

my $input_file = 'Repo.txt';
my $search_string = 'ReportBatch';
my $add_begin = 'qwe';
my $add_end = '< KPADMINFILE';
# Read file 
open(my $IN, '<', $input_file) or die "cannot open file $input_file";
# Check each line of file
while (my $row = <$IN>) {
  #chomp $row;
  if ($row =~ /$search_string/){
      $row =~ s/$/$add_end/;
  print $row;
}
}